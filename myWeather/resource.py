from .models import *
from import_export import resources
class cityResource(resources.ModelResource):
	class Meta:
		model = CityNames