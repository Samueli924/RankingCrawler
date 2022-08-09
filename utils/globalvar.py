

HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/103.0.0.0 Safari/537.36"}

Topuniversities_raw_path = "saves/topuniversities/"


def fs(text: str):
    return text.replace("\n", "").replace("\r", "").replace("\t", "").lstrip().rstrip()