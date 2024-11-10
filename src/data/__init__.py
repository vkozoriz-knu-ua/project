import abc


class DataSource(abc.ABC):
    @abc.abstractmethod
    def get_data(self):
        pass
