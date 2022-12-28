from rest_framework import serializers
from blog.models import Post, Comment


class PostSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField(source='pk')
    owner = serializers.ReadOnlyField(source='author.username')
    creation_date = serializers.ReadOnlyField(source='pubdate')
    comments = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='comments-detail')

    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'owner', 'creation_date', 'comments']
        extra_kwargs = {
            'url': {'view_name': 'posts-detail'}
        }


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post_id = serializers.ReadOnlyField(source='post.id')
    owner = serializers.ReadOnlyField(source='author.username')
    # owner = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='users-detail')
    creation_date = serializers.ReadOnlyField(source='pubdate')

    class Meta:
        model = Comment
        fields = ['url', 'id', 'text', 'post_id', 'owner', 'creation_date']
        extra_kwargs = {
            'url': {'view_name': 'comments-detail'}
        }
