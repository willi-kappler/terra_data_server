import io
from PIL import Image
import segno

# URL:
# https://terra-data.guz.uni-tuebingen.de/update_sample/xxxx
# https://teda.guz.uni-tuebingen.de/update_sample/xxxx


def tds_gen_qr_code(id: str) -> None:
    out = io.BytesIO()

    qrcode = segno.make_qr(f"https://134.2.5.41/terra/{id}", error="H")
    qrcode.save(out, scale=5, kind="png")
    img = Image.open(out)
    img = img.convert('RGB')
    img_width, img_height = img.size
    logo_img = Image.open("./logo_embed.png")
    logo_width, logo_height = logo_img.size
    box = ((img_width - logo_width) // 2, (img_height - logo_height) // 2)
    img.paste(logo_img, box)
    img.save(f"{id}.png")
