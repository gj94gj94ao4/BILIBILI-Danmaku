import os, sys
sys.path.append(os.path.dirname(__file__))

from bilibili.bilibili_comment_content_api import get_comment_data
from bilibili.comment_api import get_av_comments_list
import bilibili.bilibili_info

AV_NUMBER = "av27837553"
print("get_comment_data(\"{0}\")",AV_NUMBER)
get_comment_data(AV_NUMBER)
os.chdir("chat_xml_res")
cs = get_av_comments_list(AV_NUMBER)
for c in cs[5:10]:
    print(str(cs))
os.chdir(AV_NUMBER)
os.remove(os.listdir(AV_NUMBER)[0])
os.chdir("..")
os.rmdir(AV_NUMBER)