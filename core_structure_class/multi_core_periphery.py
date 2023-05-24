from abc import ABC, abstractmethod

import networkx as nx


class AbstractCorePeriphery(ABC):

    @abstractmethod
    def __init__(self):
        ...

    @property
    @abstractmethod  # The innermost decorator
    def graph(self):  # Abstract getter
        pass

    @graph.setter
    @abstractmethod  # The innermost decorator
    def graph(self, graph: nx.Graph):  # Abstract setter
        pass

    @property
    @abstractmethod
    def algorithm(self):
        pass

    @algorithm.setter
    @abstractmethod
    def algorithm(self, algorithm):
        pass

    @property
    @abstractmethod
    def core_ness(self):
        pass

    @core_ness.setter
    def core_ness(self, core_ness):
        pass

    @property
    @abstractmethod
    def pair_id(self):
        pass

    @pair_id.setter
    def pair_id(self, pair_id):
        pass


class CorePeriphery(AbstractCorePeriphery):

    def __init__(self):
        pass

    @property
    def graph(self):
        return self.graph

    @graph.setter
    def graph(self, graph: nx.Graph):
        self.graph = graph

    @property
    def algorithm(self):
        return self.algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        self.algorithm = algorithm

    @property
    def core_ness(self):
        return self.core_ness

    @core_ness.setter
    def core_ness(self, core_ness):
        self.core_ness = core_ness

    @property
    def pair_id(self):
        return self.pair_id

    @pair_id.setter
    def pair_id(self, pair_id):
        self.pair_id = pair_id


class MultiCorePeriphery(AbstractCorePeriphery):

    def __init__(self, graph: nx.Graph, algorithm):
        ...

    @property
    def graph(self):
        return self.graph

    @graph.setter
    def graph(self, graph):
        self.graph = graph

    @property
    def algorithm(self):
        return self.algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        self.algorithm = algorithm

    @property
    def core_ness(self):
        return self.core_ness

    @core_ness.setter
    def core_ness(self, core_ness):
        self.core_ness = core_ness

    @property
    def pair_id(self):
        return self.pair_id

    @pair_id.setter
    def pair_id(self, pair_id):
        self.pair_id = pair_id
