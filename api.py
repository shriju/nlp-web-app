
import paralleldots
paralleldots.set_api_key('ZQiTYypOkh3klaDQDtCmZueWRI1Osc1o3Ov65RDEY9g')

def ner(text):
    ner = paralleldots.ner(text)
    return ner