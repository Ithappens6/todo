from rest_framework import serializers
from django.contrib.auth import authenticate
from .models.user import CustomUser
from .models.task import Task
from .models.tag import Tag

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid username or password")
    

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'created_by']
        read_only_fields = ['id', 'created_by']


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)  # Return full tag objects in the response
    add_tag_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        write_only=True,
        required=False,
        help_text="IDs of tags to add to the task"
    )
    remove_tag_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        write_only=True,
        required=False,
        help_text="IDs of tags to remove from the task"
    )
    subtasks = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        help_text="IDs of subtasks related to this task"
    )
    parent_task = serializers.PrimaryKeyRelatedField(
        queryset=Task.objects.all(),
        required=False,
        allow_null=True,
        help_text="ID of the parent task"
    )

    class Meta:
        model = Task
        fields = [
            'id', 'user', 'title', 'description', 'status', 'due_date', 'created_at', 'updated_at',
            'parent_task', 'subtasks', 'tags', 'add_tag_ids', 'remove_tag_ids'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'user', 'tags', 'subtasks']

    def validate_add_tag_ids(self, value):
        user = self.context['request'].user
        for tag in value:
            if tag.created_by != user:
                raise serializers.ValidationError(f"Tag {tag.id} does not belong to you.")
        return value

    def validate_remove_tag_ids(self, value):
        user = self.context['request'].user
        for tag in value:
            if tag.created_by != user:
                raise serializers.ValidationError(f"Tag {tag.id} does not belong to you.")
        return value

    def validate_parent_task(self, value):
        # Ensure a task cannot be its own parent
        if self.instance and value == self.instance:
            raise serializers.ValidationError("A task cannot be its own parent.")
        return value

    def update(self, instance, validated_data):
        # Retrieve tag objects directly from validated_data
        add_tags = validated_data.pop('add_tag_ids', [])
        remove_tags = validated_data.pop('remove_tag_ids', [])

        # Add tags to the task
        if add_tags:
            instance.tags.add(*add_tags)

        # Remove tags from the task
        if remove_tags:
            instance.tags.remove(*remove_tags)

        # Update other fields in the task
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance






