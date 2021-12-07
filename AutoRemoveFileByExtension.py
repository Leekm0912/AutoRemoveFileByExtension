from os import remove, walk
from os.path import splitext
from time import sleep


class AutoRemoveFileByExtension:
    def __init__(self, dir_list, ignore_dir_list):
        self.dir_list = dir_list
        self.ignore_dir_list = ignore_dir_list

    def search(self, remove_file_extension, remove_file=False):
        if remove_file_extension == "*" and remove_file == True:
            for _ in range(100):
                print("주의!! 모든 파일이 삭제됩니다!")
                sleep(0.1)
            if input("작업을 수행하려면 remove를 입력하세요 : ") != "remove":
                return
        for dir in self.dir_list:
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
                    if remove_file_extension == "*":
                        print(file_pull_path)
                        if remove_file:
                            remove(file_pull_path)
                    elif file_extension == remove_file_extension:
                        print(file_pull_path)
                        if remove_file:
                            remove(file_pull_path)


if __name__ == '__main__':
    dir_list = [
        "c:/",
        "d:/"
        # os.path.expanduser('~')
        # os.path.join(os.path.expanduser('~'), 'Desktop'),
        # os.path.join(os.path.expanduser('~'), 'Documents')
    ]

    ignore_dir_list = [
        "Program Files",
        "AppData",
        "Lib"
    ]
    obj = AutoRemoveFileByExtension(dir_list, ignore_dir_list)
    obj.search("*", remove_file=False)
