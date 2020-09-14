class File:
    VALID_EXTENSIONS = None

    def __init__(self, filename):
        self.filename = filename
        _, _, self.extension = filename.rpartition('.')
        if self.filename == self.extension:
            self.extension = None

    def is_valid_extension(self):
        return self.extension in self.VALID_EXTENSIONS if self.extension and self.VALID_EXTENSIONS else False


class VideoFile(File):
    VALID_EXTENSIONS = ("avi", "mkv", "mpg", "mpeg")



