import sys
sys.path.append("../")

import pytest
import xml.etree.ElementTree as ET
from bilibili.bilibili_comment_content_api import *


AV_NUMBER_ERROR_FORMATTING = "aa12345666d"
AV_NUMBER_ONE_P = "av23315808"
AV_NUMBER_MANY_P = "av25233957"
CID = '38842914'

def test_find_cid_with_error_formatting():
    with pytest.raises(Exception, match=r'av號格式錯誤'):
        find_cid_with_aid(AV_NUMBER_ERROR_FORMATTING)


def test_find_cid_with_aid_one_p():
    assert find_cid_with_aid(AV_NUMBER_ONE_P) == ["38842914"]


def test_find_cid_with_aid_many_p():
    assert find_cid_with_aid(AV_NUMBER_MANY_P) == [
        '42786429', '42786438', '42787134', '42787848', '42788354', '42789167', '42789594', '42790088', '42790624', '46865395', '46802587', '46803698','46804889']


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
    os.chdir(AV_NUMBER_MANY_P)
    need = ['42786429.xml', '42786438.xml', '42787134.xml', '42787848.xml',
                               '42788354.xml', '42789167.xml', '42789594.xml', '42790088.xml', '42790624.xml',
                               '46865395.xml', '46802587.xml', '46803698.xml','46804889.xml']
    now = os.listdir(".")
    assert [i for i in now if i not in need] == []
    for rm in os.listdir('.'):
        os.remove(rm)
    os.chdir('../')
    os.rmdir(AV_NUMBER_MANY_P)
    os.chdir('../')
    os.rmdir('chat_xml_res')
