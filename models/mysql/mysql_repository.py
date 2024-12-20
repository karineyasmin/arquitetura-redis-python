class MysqlRepository:
    def __init__(self):
        self.__data = {"José": "José Silva"}

    def select_by_name(self, name: str):
        if name in self.__data:
            return self.__data[name]
        return None
