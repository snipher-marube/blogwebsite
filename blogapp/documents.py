from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry

from .models import Post

# define the index
post_index = Index('posts')

@registry.register_document
class PostDocument(Document):
    body = fields.TextField()

    class Index:
        name = 'posts'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}
        
    class Django:
        model = Post
        fields = [
            'title',
            'publish',
        ]

    def prepare_body(self, instance):
        # Custom logic to convert RichTextUploadingField to text
        return instance.body  # Or apply any custom logic needed