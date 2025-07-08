import tds_sample_id
import tds_qr_code


if __name__ == "__main__":
    id = tds_sample_id.tds_gen_new_id()
    tds_qr_code.tds_gen_qr_code(id)
