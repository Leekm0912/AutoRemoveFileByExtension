from os import remove, walk
from os.path import splitext
from time import sleep


class AutoRemoveFileByExtension:
    def __init__(self, search_dir_list=None, ignore_dir_list=None):
        if search_dir_list is None:
            self.search_dir_list = self.readSetting("search_dir_list")
        else:
            self.search_dir_list = search_dir_list
        if ignore_dir_list is None:
            self.ignore_dir_list = self.readSetting("ignore_dir_list")
        else:
            self.ignore_dir_list = ignore_dir_list

    def readSetting(self, dir):
        result = []
        with open(dir, "r") as r:
            temp = r.readlines()
            for t in temp:
                result.append(t.strip())
        return result

    def search(self, remove_file_extension, remove_file="False"):
        remove_file = remove_file.lower()
        if remove_file_extension == "*" and remove_file == "true":
            for _ in range(100):
                print("주의!! 모든 파일이 삭제됩니다!")
                sleep(0.1)
            if input("작업을 수행하려면 remove를 입력하세요 : ") != "remove":
                return
        for dir in self.search_dir_list:
            for (path, _, files) in walk(dir):
                breaker = False
                for ignore in self.ignore_dir_list:
                    if path.find(ignore) != -1:
                        breaker = True
                        # print(path)
                        break
                for filename in files:
                    if breaker:
                        break
                    file_extension = splitext(filename)[-1]
                    file_pull_path = f"{path}\\{filename}"
                    try:
                        if remove_file_extension == "*":
                            print(file_pull_path)
                            if remove_file == "true":
                                remove(file_pull_path)
                        elif file_extension == remove_file_extension:
                            print(file_pull_path)
                            if remove_file == "true":
                                remove(file_pull_path)
                    except Exception as e:
                        print(f"\t파일 삭제 실패 : {file_pull_path} --- {e.__cause__} ")


if __name__ == '__main__':
    from configparser import ConfigParser
    obj = AutoRemoveFileByExtension()
    config = ConfigParser()
    config.read("setting.ini")

    obj.search(
        remove_file_extension=config["search"]["remove_file_extension"],
        remove_file=config["search"]["remove_file"]
    )
