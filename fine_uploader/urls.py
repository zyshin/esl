from django.conf.urls import url, include
from .views import UploadView

urlpatterns = [
	url(r'^corpus/upload/(?P<cid>[^\s/]+?)/(?:(?P<pid>[^\s/]+?)/)?$', UploadView.as_view(), name='upload'),
	# url(r'^corpus/upload_done/(?P<cid>\S+?)/(?:(?P<pid>\S+?)/)?$', upload_done, name='upload_done'),
]
