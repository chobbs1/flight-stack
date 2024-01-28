from scipy.spatial.transform import Rotation
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class QuadCopter:

    arm_length = 1
    color = "lightcoral"
    thick = 4

    def __init__(self, x, y, z):
        self.r_O_O1_f_inertial = np.array([x, y, z])

        self.O1_body = np.array([0, 0, 0])
        self.A_body = np.array([self.arm_length, 0, 0])
        self.B_body = np.array([0, self.arm_length, 0])
        self.C_body = np.array([0, -self.arm_length, 0])
        self.D_body = np.array([-self.arm_length, 0, 0])

        self.euler_angles = np.array([0, 0, 30])
        
    def plot_quad(self, ax):
        R_body2inertial = Rotation.from_euler('ZYX', self.euler_angles, degrees=True).as_matrix()

        self.O1_inert = np.dot(R_body2inertial, self.O1_body)
        self.A_inert = np.dot(R_body2inertial, self.A_body)
        self.B_inert = np.dot(R_body2inertial, self.B_body)
        self.C_inert = np.dot(R_body2inertial, self.C_body)
        self.D_inert = np.dot(R_body2inertial, self.D_body)

        r_O1_A_inert = np.array([[self.O1_inert[0], self.A_inert[0]], 
                    [self.O1_inert[1], self.A_inert[1]], 
                    [self.O1_inert[2], self.A_inert[2]]])

        r_O1_B_inert = np.array([[self.O1_inert[0], self.B_inert[0]], 
                    [self.O1_inert[1], self.B_inert[1]], 
                    [self.O1_inert[2], self.B_inert[2]]])

        r_O1_C_inert = np.array([[self.O1_inert[0], self.C_inert[0]], 
                    [self.O1_inert[1], self.C_inert[1]], 
                    [self.O1_inert[2], self.C_inert[2]]])

        r_O1_D_inert = np.array([[self.O1_inert[0], self.D_inert[0]], 
                    [self.O1_inert[1], self.D_inert[1]], 
                    [self.O1_inert[2], self.D_inert[2]]])

        ax.plot(r_O1_A_inert[0], r_O1_A_inert[1], r_O1_A_inert[2], color=self.color, linewidth=self.thick)
        ax.plot(r_O1_B_inert[0], r_O1_B_inert[1], r_O1_B_inert[2], color=self.color, linewidth=self.thick)
        ax.plot(r_O1_C_inert[0], r_O1_C_inert[1], r_O1_C_inert[2], color=self.color, linewidth=self.thick)
        ax.plot(r_O1_D_inert[0], r_O1_D_inert[1], r_O1_D_inert[2], color=self.color, linewidth=self.thick)

        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_zlabel('Z Axis')

        axes_length = 2
        ax.set_xlim(-axes_length, axes_length)
        ax.set_ylim(-axes_length, axes_length)
        ax.set_zlim(0, 2 * axes_length)

class InertialFrame:

    def __init__(self):
        self.axes_length = 2
        self.color = "black" 
        self.thick = 1

    def plot_axes(self, ax):
        ax.quiver(0, 0, 0, self.axes_length, 0, 0, color=self.color)
        ax.quiver(0, 0, 0, 0, self.axes_length, 0, color=self.color)
        ax.quiver(0, 0, 0, 0, 0, -self.axes_length, color=self.color)
    

