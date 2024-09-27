
import segno

# URL:
# https://terra-data.guz.uni-tuebingen.de/update_sample/xxxx
# https://teda.guz.uni-tuebingen.de/update_sample/xxxx


def tds_gen_qr_code(id: str) -> None:
    url = f"https://scripts.guz.uni-tuebingen.de/terra/update_sample/{id}"
    qrcode = segno.make_qr(url, error="H")
    qrcode.save(f"{id}.png", scale=5)

