from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Video
from .serializers import VideoSerializer

class VideoPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'

    def get_paginated_response(self, data):
        return Response({
            'videos': data, 
            'pagination': {
                'page': self.page.number,  
                'limit': self.page.paginator.per_page,  
                'total_pages': self.page.paginator.num_pages, 
                'total_videos': self.page.paginator.count, 
                'next_cursor': self.get_next_link(),  
            }
        })

@method_decorator(cache_page(60 * 15), name='dispatch')  # Cache for 15 minutes
class VideoListAPIView(ListAPIView):
    queryset = Video.objects.all().select_related('user', 'music').prefetch_related(
        'products__store', 'products__variants'
    ).order_by('-created_at')
    serializer_class = VideoSerializer
    pagination_class = VideoPagination

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)

            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response({'videos': serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

