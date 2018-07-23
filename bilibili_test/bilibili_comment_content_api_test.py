import sys
sys.path.append("../")

import pytest
import xml.etree.ElementTree as ET
from bilibili.bilibili_comment_content_api import *


AV_NUMBER_ERROR_FORMATTING = "aa12345666d"
AV_NUMBER_ONE_P = "av23315808"
AV_NUMBER_MANY_P = "av7010272"
CID = '38842914'

def test_find_cid_with_error_formatting():
    with pytest.raises(Exception, match=r'av號格式錯誤'):
        find_cid_with_aid(AV_NUMBER_ERROR_FORMATTING)


def test_find_cid_with_aid_one_p():
    assert find_cid_with_aid(AV_NUMBER_ONE_P) == ["38842914"]


def test_find_cid_with_aid_many_p():
    assert find_cid_with_aid(AV_NUMBER_MANY_P) == [
        '11241604', '11267060', '11285238', '11305727', '11325525', '11392206', '11428311']


def test_cid_xml_file():
    CID_PATH = CID + ".xml"
    cid_xml_file(CID)
    tree = ET.parse(CID_PATH)
    root = tree.getroot()
    os.remove(CID_PATH)
    assert root[1].text == "38842914"


def test_get_comment_with_null_data():
    with pytest.raises(Exception, match=r"不需要爬取資料，資料已存在或沒有輸入av號"):
        get_comment_data("")
    os.chdir('../')
    os.rmdir('chat_xml_res')


def test_get_comment_data():
    get_comment_data([AV_NUMBER_MANY_P])
    os.chdir('chat_xml_res')
    os.chdir(AV_NUMBER_MANY_P)
    need = ['11241604.xml', '11267060.xml', '11285238.xml', '11305727.xml', '11325525.xml', '11392206.xml', '11428311.xml']

    now = os.listdir(".")
    assert [i for i in now if i not in need] == []
    for rm in os.listdir('.'):
        os.remove(rm)
    os.chdir('../')
    os.rmdir(AV_NUMBER_MANY_P)
    os.chdir('../')
    os.rmdir('chat_xml_res')
