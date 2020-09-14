import inspect
from classes import files


class FileFactory:
    @classmethod
    def create_file(cls, filename):
        members = inspect.getmembers(files, inspect.isclass)
        file_classes = [m[1] for m in members if m[1].__module__ == 'classes.files']
        for file_class in file_classes:
            file_object = file_class(filename)
            if file_object.is_valid_extension():
                return file_object
