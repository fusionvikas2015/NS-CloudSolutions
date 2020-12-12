from django.urls import path
from .views import AstroAPIView, AstroDetails, AndroidIOSAutomation,PortResetJob, ScreenshotsView,ParallelJobView

urlpatterns = [
    path('astro/', AstroAPIView.as_view()),
    path('astro/<int:id>/', AstroDetails.as_view()),
    path('automationjob/', AndroidIOSAutomation.as_view()),
    path('resetjob/', PortResetJob.as_view()),
    path('getscreenshots/', ScreenshotsView.as_view()),
    path('paralleljob/', ParallelJobView.as_view()),
]