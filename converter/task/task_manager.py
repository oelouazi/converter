from threading import Thread, RLock


class TaskManager(Thread):

    def __init__(self):
        super().__init__()
        self.__lock = RLock()
        self.__tasks = []

    def add_task(self, task):
        with self.__lock:
            self.__tasks.append(task)
        return task

    def run(self):
        # Run each task in order
        with self.__lock:
            for task in self.__tasks:
                task.run()
