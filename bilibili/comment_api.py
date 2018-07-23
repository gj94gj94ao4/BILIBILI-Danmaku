import os
import xml.etree.ElementTree as ET


CHAT_XML_DIR = "chat_xml_res"
CHAT_RES_LIST = []


def checked(fn):
    def rf(*args, **kwargs):
        if len(CHAT_RES_LIST) == 0:
            _get_all_av()
        return fn(*args, **kwargs)
    return rf


def _get_all_av():
    os.chdir(CHAT_XML_DIR)
    CHAT_RES_LIST = os.listdir('.')
    if len(CHAT_RES_LIST) == 0:
        raise Exception("資料陣列無內容")

# TODO:返還{"time":"comment", ... }
@checked
def get_av_comments_list(av, cid=""):
    """
    用av號找尋該影片所有的留言與時軸
    若有多p則必須給cid，不然就會返還
    第一個
    (sec,user,text)
    """
    print(os.getcwd())
    os.chdir(av)
    try:
        if len(cid) == 0:
            cid = os.listdir(".")[0]
        else:
            cid += ".xml"
    except IndexError as e:
        print("該AV資料夾中無檔案")
    tree = ET.parse(cid)
    root = tree.getroot()
    users = []
    texts = []
    secs = []
    for c in root:
        if c.tag == "d":
            secs.append(c.attrib["p"].split(",")[0])
            users.append(c.attrib["p"].split(",")[6])
            texts.append(c.text)
    return (secs,users,texts)

if __name__ == "__main__":
    c = get_av_comments_list("av27436999")
    for sec, user, text in zip(c[0], c[1], c[2]):
        print(sec,user,text)