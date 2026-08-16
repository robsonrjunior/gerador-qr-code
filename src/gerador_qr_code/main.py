from typing import Annotated

import qrcode
from fastapi import Body, FastAPI
from fastapi.responses import Response
from qrcode.image.svg import SvgImage

app = FastAPI(title="Gerador de QR Code")


@app.post(
    "/qr-code",
    response_class=Response,
    responses={200: {"content": {"image/svg+xml": {}}}},
)
def generate_qr_code(value: Annotated[str, Body(media_type="text/plain")]) -> Response:
    image = qrcode.make(value, image_factory=SvgImage)

    return Response(content=image.to_string(), media_type="image/svg+xml")
