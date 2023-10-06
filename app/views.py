from rest_framework import generics
from rest_framework import permissions
from .models import Post
from .permissions import IsOwnerOrSuperuser
from .serializers import PostSerializer
# Create your views here.
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Create a new post with the authenticated user as the author.

        This method is called when a new post is being created via the API.
        It ensures that the author of the post is set to the currently
        authenticated user before saving the new post to the database.
        """
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrSuperuser]
