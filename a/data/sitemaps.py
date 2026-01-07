from django.contrib.sitemaps import Sitemap
from django.utils.module_loading import import_string
from .abc import SUFFIX
ProjectModel = import_string(f'data.models.Project{SUFFIX}')
class ProjectSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6
    def items(self):
        return ProjectModel.objects.all()