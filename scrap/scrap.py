import requests
from readability import Document
import html2text
def getreadabledata(url):
    response = requests.get(url)
    doc = Document(response.text)
    h = html2text.HTML2Text()
    h.ignore_images=True
    h.ignore_links=True
    return h.handle(doc.summary())