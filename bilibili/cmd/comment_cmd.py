import argparse
import os
import sys
sys.path.append("../../")

from bilibili.bilibili_comment_content_api import get_comment_data

DEFAULT_DIR = ''

def main():
    parser = argparse.ArgumentParser(description="用於獲取bilibili站一般視頻內的彈幕，獲取後的資料將會以原始xml的方式儲存")
    parser.add_argument('-a', '--avnumbers', nargs='*', help="下載AV號 -a av123456 av...")
    parser.add_argument('-o', '--output', help="輸出位置", default="chat_xml_res/")
    # TODO: 加入可以從檔案讀取avnumber

    DEFAULT_DIR = os.getcwd()
    args = parser.parse_args()
    

    if args.avnumbers != None:
        print(str.format("下載xml至{0}{1}:",os.getcwd().replace('\\','/'), args.output))
        for av in args.avnumbers:
            try:
                get_comment_data([av], args.output)
                print("    " + av + "下載完成")
            except Exception as e:
                print("    " + av + "下載失敗")
                os.chdir(DEFAULT_DIR)
            
            



if __name__ == "__main__":
    main()