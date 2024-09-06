from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import CharField


class HTMLToPDFSerializer(ModelSerializer):
    html_content = CharField(style={"base_template": "textarea.html"})
