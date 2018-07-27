import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "../"))

import pytest
import xml.etree.ElementTree as ET
from bilibili import bilibili_comment_content_api


AV_NUMBER_ERROR_FORMATTING = "aa12345666d"
AV_NUMBER_ONE_P = "av23315808"
AV_NUMBER_MANY_P = "av7010272"
CID = '38842914'

def test_find_cid_with_error_formatting():
    with pytest.raises(Exception, match=r'av號格式錯誤'):
        bilibili_comment_content_api.find_cid_with_aid(AV_NUMBER_ERROR_FORMATTING)


def test_find_cid_with_aid_one_p():
    assert bilibili_comment_content_api.find_cid_with_aid(AV_NUMBER_ONE_P) == ["38842914"]


def test_find_cid_with_aid_many_p():
    assert bilibili_comment_content_api.find_cid_with_aid(AV_NUMBER_MANY_P) == [
        '11241604', '11267060', '11285238', '11305727', '11325525', '11392206', '11428311']


def test_cid_xml_file():
    CID_PATH = CID + ".xml"
    bilibili_comment_content_api.cid_xml_file(CID)
    tree = ET.parse(CID_PATH)
    root = tree.getroot()
    os.remove(CID_PATH)
    assert root[1].text == "38842914"


def test_get_comment_data():
    bilibili_comment_content_api.get_comment_data(AV_NUMBER_MANY_P, os.path.dirname(__file__) + "/chat_xml_res")
    os.chdir('bilibili_test/chat_xml_res')
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
