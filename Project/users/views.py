from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import StudentSerializer, TeacherSerializer, ParentSerializer
# Create your views here.
class TeacherRegisterView(APIView):
    permission_classes = [AllowAny,]

    def get(self, request):
        pass

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            

