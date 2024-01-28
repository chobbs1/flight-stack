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

        # self.O_body = np.array([0, 0, 0])
        # self.A_body = np.array([self.arm_length, 0, 0])
        # self.B_body = np.array([0, self.arm_length, 0])
        # self.C_body = np.array([0, -self.arm_length, 0])
        # self.D_body = np.array([-self.arm_length, 0, 0])

        self.O_inert = np.array([0, 0, 0])
        self.A_inert = np.array([self.arm_length, 0, 0])
        self.B_inert = np.array([0, self.arm_length, 0])
        self.C_inert = np.array([0, -self.arm_length, 0])
        self.D_inert = np.array([-self.arm_length, 0, 0])


    # euler_angles = np.array([0, 0, 0])
    # rotation = Rotation.from_euler('ZYX', euler_angles, degrees=True)

    def plot_quad(self, ax):

        r_OA = np.array([[self.O_inert[0], self.A_inert[0]], 
                    [self.O_inert[1], self.A_inert[1]], 
                    [self.O_inert[2], self.A_inert[2]]])

        r_OB = np.array([[self.O_inert[0], self.B_inert[0]], 
                    [self.O_inert[1], self.B_inert[1]], 
                    [self.O_inert[2], self.B_inert[2]]])

        r_OC = np.array([[self.O_inert[0], self.C_inert[0]], 
                    [self.O_inert[1], self.C_inert[1]], 
                    [self.O_inert[2], self.C_inert[2]]])

        r_OD = np.array([[self.O_inert[0], self.D_inert[0]], 
                    [self.O_inert[1], self.D_inert[1]], 
                    [self.O_inert[2], self.D_inert[2]]])

        ax.plot(r_OA[0], r_OA[1], r_OA[2], color=self.color, linewidth=self.thick)
        ax.plot(r_OB[0], r_OB[1], r_OB[2], color=self.color, linewidth=self.thick)
        ax.plot(r_OC[0], r_OC[1], r_OC[2], color=self.color, linewidth=self.thick)
        ax.plot(r_OD[0], r_OD[1], r_OD[2], color=self.color, linewidth=self.thick)

        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_zlabel('Z Axis')

        axes_length = 2
        ax.set_xlim(-axes_length, axes_length)
        ax.set_ylim(-axes_length, axes_length)
        ax.set_zlim(0, 2 * axes_length)



    

