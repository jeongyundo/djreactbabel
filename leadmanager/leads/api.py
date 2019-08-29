from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer


# Lead Viewset


class LeadViewSet(viewsets.ModelViewSet):
    permission_classes = [
        #permissions.IsAuthenticated,
        permissions.AllowAny,
    ]
    #이를 통해 권한 있는 사람만 사용 가능

    serializer_class = LeadSerializer

    #1. 전체 확인이 가능한 쿼리셋
    queryset = Lead.objects.all()
    
    #2. 오직 유저만 사용 가능하게 쿼리를 제공
    # def get_queryset(self):
    #     return self.request.user.leads.all()
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    