import sys
sys.path.append("../")
import os

import pytest
from bilibili.comment_api import *

NULL_PATH = "02D20BBD7E394A/"
AV_NUMBER = "av27436999"
TEST_XML_RES = "chat_xml_res"

def test_get_av_comments_list():
    os.chdir(__file__ + "/../")
    CHAT_XML_DIR = TEST_XML_RES
    x = get_av_comments_list(AV_NUMBER)
    assert x[1][1] == "9ee3cac2"
