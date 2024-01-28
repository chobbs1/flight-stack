from quad_model import QuadCopter, InertialFrame
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    inertial = InertialFrame()
    quad = QuadCopter(0, 0, 0)

    quad.plot_quad(ax)
    inertial.plot_axes(ax)

    plt.show()

if __name__ == "__main__":
    main()