import os
import shutil
import time
class Remove:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.time = time.time()

class FileManager:
    def __init__(self):
        self.remove_list = []
        self.trash = "./trash"
    def create_dir(self, name, address):
        if not os.path.exists(address + '/' + name):
            os.mkdir(address + '/' + name)

    def create_file(self, name, address):
        if not os.path.exists(address + '/' + name):
            os.mknod(address + '/' + name)
    
    def delete(self, name, address):
        if os.path.exists(address + '/' + name):
            self.create_dir(self.trash, '.')
            self.remove_list.append(Remove(name, address))
            shutil.move(address + '/' + name, "./trash/" + str(self.remove_list[-1].time) + name)
        # os.remove(address + '/' + name)
    
    def find(self, name, address):
        result = []
        for root, _, files in os.walk(address):
            if name in files:
                result.append(str(root) + "/" + name)
        return result
    
    def restore(self, name):
        tmp = []
        min_time = float("inf")
        for r in self.remove_list:
            if r.name == name:
                tmp.append(r)
        for t in tmp:
            if t.time <= min_time:
                min_time = t.time
        for t in tmp:
            if t.time == min_time:
                shutil.move("./trash/" + str(t.time) + t.name, t.address + '/' + t.name)
                self.remove_list.remove(t)
