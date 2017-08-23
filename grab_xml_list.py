import httplib2
from lxml import etree

h = httplib2.Http('.cache')
reponse, content = h.request('https://myanimelist.net/malappinfo.php?u=shaliber&status=all&type=anime')

tree = etree.fromstring(content)

# Series status = 1 means currently airing
# My status = 1 means currently watching
title = tree.xpath("//anime[./series_status/text()='1' and ./my_status/text()='1']//series_title/text()")
series_ids = tree.xpath("//anime[./series_status/text()='1' and ./my_status/text()='1']//series_animedb_id/text()")
urls = []
for s_id in series_ids:
    link = "https://myanimelist.net/anime/%s" % s_id
    urls.append(link)

my_dict = dict(zip(title, urls))
print(my_dict)
