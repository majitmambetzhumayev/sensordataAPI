from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.method in ['GET','HEAD','OPTIONS']:
            return True
        return request.user.is_staff
    def has_object_permission(self, request, view, obj) -> bool:
        if request.method in ['GET','HEAD','OPTIONS']:
            return True
        return request.user.is_staff
            
class IsSensorOperator(BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user and request.user.is_authenticated