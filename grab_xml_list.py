import httplib2
from lxml import etree

h = httplib2.Http('.cache')
reponse, content = h.request('https://myanimelist.net/malappinfo.php?u=shaliber&status=all&type=anime')

tree = etree.fromstring(content)

title = tree.xpath("//anime[./series_status/text()='1' and ./my_status/text()='1']//series_title/text()")
series_ids = tree.xpath("//anime[./series_status/text()='1' and ./my_status/text()='1']//series_animedb_id/text()")
urls = []
for s_id in series_ids:
    link = "https://myanimelist.net/anime/%s" % s_id
    urls.append(link)

my_dict = dict(zip(title, urls))
print(my_dict)
# for elem in tree.iter():
#     air_status = tree.xpath("//anime//series_status")
#     my_status = tree.xpath("//anime//my_status")
#     if air_status == "1" and my_status == "1":
#         print("test")
#         series_title = tree.xpath("//anime//series_title/text()")
#         series_id  = tree.xpath("//anime//series_animedb_id/text()")
#         link = "https://myanimelist.net/anime/%s" % series_id
#         airing_dict = {"title": series_title,
#                         "link": link}
