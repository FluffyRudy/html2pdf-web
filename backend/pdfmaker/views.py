from rest_framework.decorators import api_view
from rest_framework.parsers import BaseParser
from rest_framework.exceptions import ParseError
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.http import HttpResponse
from weasyprint.text.fonts import FontConfiguration
from weasyprint import HTML, CSS
from .serializers import HTMLToPDFSerializer
from .utils.hexgen import get_random_hex


class HTMLParser(BaseParser):
    media_type = "text/html"
    format = "html"

    def parse(self, stream, media_type=None, parse_context=None):
        try:
            return [stream.read().decode("utf-8")]
        except Exception as error:
            return [str(error)]


@api_view(["GET"])
def home_view(request: Request) -> Response:
    # pdf_instance = HTML(string=)
    print(request.data)
    return Response({"api": reverse("create-pdf", request=request)})


class HTMLToPDFMaker(APIView):
    parser_classes = [HTMLParser]

    def post(self, request, *args, **kwargs):
        html_data = str(request.data[0])
        pdf_content = HTML(string=html_data).write_pdf(font_config=FontConfiguration())
        response = HttpResponse(content=pdf_content, content_type="application/pdf")
        filename = f"{get_random_hex(4)}.pdf"
        response["Content-Disposition"] = f'attachment; filename="{filename}"'
        return response
