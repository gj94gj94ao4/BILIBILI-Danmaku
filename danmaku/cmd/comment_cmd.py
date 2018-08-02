import argparse
import traceback
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "../"))

print(sys.path)

from bilibili.bilibili_comment_content_api import get_comment_data

DEFAULT_DIR = ''

def main():
    parser = argparse.ArgumentParser(description="用於獲取bilibili站一般視頻內的彈幕，獲取後的資料將會以原始xml的方式儲存")
    parser.add_argument('-a', '--avnumbers', nargs='*', help="下載AV號 -a av123456 av...")
    parser.add_argument('-o', '--output', help="輸出位置", default="chat_xml_res/")
    # TODO: 加入可以從檔案讀取avnumber
    # 像是csv檔案用\t切開的文字檔

    args = parser.parse_args()
    

    if args.avnumbers != None:
        print(str.format("下載xml至{0}:",os.path.abspath(args.output)))
        for av in args.avnumbers:
            try:
                get_comment_data(av, args.output)
                print(str.format("\t{0} 下載完成", av))
                
            except FileExistsError:
                os.chdir("../")
                print(str.format("\t{0} 檔案已存在", av))
            except Exception as e:
                print(str.format("\t{0} 錯誤:{1}", av, e.args[0]))


if __name__ == "__main__":
    main()