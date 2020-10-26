from threading import RLock

from PIL import Image


class ImageConvertTask:
    """
    Represents a task able to convert an image format to jpg format.
    """

    def __init__(self, input_path, output_path):
        """
        Create a new image convert task.
        :param input_path: input path to file.
        :param output_path: output path to file.
        """
        self.__input_path = input_path
        self.__output_path = output_path
        self.__lock = RLock()
        self.__on_update = None
        self.__progress = 0

    def input_path(self):
        """
        Returns input path file.
        :return: input path file.
        """
        return self.__input_path

    def output_path(self):
        """
        Returns output path file.
        :return: output path file.
        """
        return self.__output_path

    def progress(self):
        """
        Returns task progression in pourcentage.
        :return: task progression in pourcentage.
        """
        return self.__progress

    def __set_progress(self, progress):
        """
        Set task progression.
        This method is thread-safe.
        :param progress: new progress pourcentage.
        :return:
        """
        assert 0 <= progress <= 100
        with self.__lock:
            self.__progress = progress
        if self.__on_update:
            self.__on_update()

    def on_update(self, callback):
        """
        Call a function on each progress step.
        :param callback: callback to call.
        """
        self.__on_update = callback

    def run(self):
        """
        Run image convert task logic.
        """
        try:
            self.__set_progress(0)
            with Image.open(self.__input_path) as im:
                self.__set_progress(50)
                im.convert('RGB').save(self.__output_path)
                self.__set_progress(100)
        except OSError:
            print("Cannot convert", self.__input_path, self.__output_path)
