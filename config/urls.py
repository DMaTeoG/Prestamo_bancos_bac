from django.contrib import admin
from django.urls import path, include

from apps.accounts.views import AdminUserListView, AdminUserDetailView
from apps.companies.views import AdminMembershipListView, AdminMembershipUpdateView
from apps.scoring.views import AdminModelVersionListView, AdminModelActivateView
from apps.audit.views import AdminAuditLogListView

urlpatterns = [
    path("admin/", admin.site.urls),
    # API v1 core endpoints
    path("api/v1/auth/", include("apps.accounts.urls")),
    path("api/v1/companies/", include("apps.companies.urls")),
    path("api/v1/evaluations/", include("apps.scoring.urls")),
    # API v1 Admin endpoints (docs.md §8)
    path("api/v1/admin/users/", AdminUserListView.as_view(), name="admin-user-list"),
    path("api/v1/admin/users/<int:pk>/", AdminUserDetailView.as_view(), name="admin-user-detail"),
    path("api/v1/admin/memberships/", AdminMembershipListView.as_view(), name="admin-membership-list"),
    path("api/v1/admin/memberships/<int:pk>/", AdminMembershipUpdateView.as_view(), name="admin-membership-update"),
    path("api/v1/admin/models/", AdminModelVersionListView.as_view(), name="admin-model-list"),
    path("api/v1/admin/models/<int:pk>/activate/", AdminModelActivateView.as_view(), name="admin-model-activate"),
    path("api/v1/admin/audit/", AdminAuditLogListView.as_view(), name="admin-audit-list"),
]
