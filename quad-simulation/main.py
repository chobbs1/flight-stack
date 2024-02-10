from quad_model import QuadCopter, Environment
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    inertial = Environment()

    x_init = 0
    y_init = 0
    z_init = -1
    roll_deg = 0 
    pitch_deg = 0
    yaw_deg = 0

    quad = QuadCopter(x_init, y_init, z_init, roll_deg, pitch_deg, yaw_deg)

    quad.update_state()
    # quad.plot_quad(ax)

    quad.simulate_physics()

    # quad.plot_body_frame_axes(ax) # Broken
    inertial.plot_inertial_frame_axes(ax)

    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()