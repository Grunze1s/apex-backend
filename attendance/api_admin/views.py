from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from attendance.api_admin.serializers import StudentAttendanceAdminRetrieveSerializer
from attendance.filters import AttendanceFilter
from attendance.models import StudentAttendance


class StudentAttendanceListAPIView(ListAPIView):
    """View for listing admin student attendance."""

    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = StudentAttendanceAdminRetrieveSerializer
    queryset = StudentAttendance.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["name"]
    filterset_class = AttendanceFilter
