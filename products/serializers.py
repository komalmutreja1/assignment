from django.utils.translation import ugettext_lazy as _
from utils.core.customModelSerializer import CustomDynamicFieldsModelSerializer, CustomNestedSerializerField
from products.models import Product



class ProductSerializer(CustomDynamicFieldsModelSerializer):
    """
    Product Serializer 
    Validates product data provided by user and creates product object accordingly.
    It also ensures that fields are made required according to selected type,
    ie screen_size and color for type Mobile and hd_capacity for type Laptop.
    """

    class Meta:
        model = Product
        fields = '__all__'


    def get_fields(self, *args, **kwargs):
        fields = super(ProductSerializer, self).get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        
        if request:
            product_type = request.data.get('type')
            if getattr(request, 'method', None) == "POST":
                product_type = request.data.get('type')

            elif getattr(request, 'method', None) in ["PUT", "PATCH"]:
                product_type = self.instance.type

            if product_type == "Mobile":
                fields['color'].required = True
                fields['screen_size'].required = True
                del fields['hd_capacity']
            else:
                fields['hd_capacity'].required = True
                del fields['color']
                del fields['screen_size']
        return fields