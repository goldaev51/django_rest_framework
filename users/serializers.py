from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Post, Comment


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(view_name='posts-detail', many=True, queryset=Post.objects.all())
    comments = serializers.HyperlinkedRelatedField(view_name='comments-detail', many=True,
                                                   queryset=Comment.objects.all())

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'posts', 'comments']
