from quad_model import QuadCopter
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    quad = QuadCopter(0, 0, 0)

    quad.plot_quad(ax)
    plt.show()

if __name__ == "__main__":
    main()