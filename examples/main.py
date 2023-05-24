import cpnet
import matplotlib
import matplotlib.pyplot as plt
import networkx as nx

from core_structure_class.multi_core_periphery import MultiCorePeriphery

DISPLAY1 = 'GTK3Agg'
DISPLAY2 = 'GTK3Cairo'
WEB_DISPLAY1 = 'WebAgg'
matplotlib.use(DISPLAY2)


class ExampleKarateClub:
    G = nx.karate_club_graph()


if __name__ == '__main__':
    test = ExampleKarateClub()
    a = MultiCorePeriphery(nx.karate_club_graph(), cpnet.KM_config())
    nx.draw_networkx(G=test.G)
    plt.show()
