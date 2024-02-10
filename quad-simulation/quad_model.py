from scipy.spatial.transform import Rotation as R
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.integrate as spi

gravity = 9.81
dt = 0.01

class QuadCopter:
    arm_length = 1
    mass = 1
    inertia = np.array([0.1, 0.1, 1])

    color = "lightcoral"
    x_pos_ax_color = "red"
    thick = 4

    def __init__(self, x, y, z, roll_deg, pitch_deg, yaw_deg):
        self.rOG_inert = np.array([x, y, z])

        # Using ZYX euler angle conventions, so order is yaw -> roll -> pitch
        self.euler_angles = np.array([yaw_deg, pitch_deg, roll_deg])

        self.A_body = np.array([self.arm_length, 0, 0])
        self.B_body = np.array([0, self.arm_length, 0])
        self.C_body = np.array([0, -self.arm_length, 0])
        self.D_body = np.array([-self.arm_length, 0, 0])

    def update_state(self):
        R_body2inertial = R.from_euler('ZYX', self.euler_angles, degrees=True).as_matrix()

        self.A_inert = np.dot(R_body2inertial, self.A_body) + self.rOG_inert
        self.B_inert = np.dot(R_body2inertial, self.B_body) + self.rOG_inert
        self.C_inert = np.dot(R_body2inertial, self.C_body) + self.rOG_inert
        self.D_inert = np.dot(R_body2inertial, self.D_body) + self.rOG_inert

        self.axes = np.dot(R_body2inertial, np.identity(3))
        
        # print(f"R_body2inertial = \n{R_body2inertial}")
        # print(f"axes = \n{self.axes}")
        # print(f"axes = \n{self.axes[2]}")
        # print(f"self.A_inert = \n{self.A_inert}")
        # print(f"R_body2inert/ial = \n{R_body2inertial}")
        # print(f"self.C_inert = \n{self.C_inert}")
        # print(f"{np.dot(self.axes[2],self.C_inert)}")
        # print(f"R_body2inertial = \n{R_body2inertial}")
        
    def simulate_physics(self):
        t = np.linspace(0, dt, 2)

        F = np.zeros(3)
        F[2] = -9.81

        x_dot = 0
        y_dot = 0
        z_dot = 0

        L = np.zeros(3)

        X = np.zeros(12)
        X[0] = self.rOG_inert[0]
        X[1] = x_dot
        X[2] = self.rOG_inert[1]
        X[3] = y_dot
        X[4] = self.rOG_inert[2]
        X[5] = z_dot

        roll_rate = 0
        pitch_rate = 0
        yaw_rate = 0

        X[6] = self.euler_angles[2] # Roll
        X[7] = roll_rate
        X[8] = self.euler_angles[1] # Pitch
        X[9] = pitch_rate
        X[10] = self.euler_angles[0] # Yaw
        X[11] = yaw_rate

        print(f"State Vector (t0) = {X}")
        X1 = spi.odeint(self.eqn_of_motion, X, t, args=(F, self.mass, L, self.inertia))

        X = X1[1]
        print(f"State Vector (t1) = {X}")


        return 1
    
    def eqn_of_motion(self, X, t, F, mass, L, I):

        # Linear Equations of Motion
        x_dot = X[1] 
        x_ddot = F[0]
        y_dot = X[3] 
        y_ddot = F[1]
        z_dot = X[5] 
        z_ddot = mass * gravity + F[2]

        linear_eom = [x_dot, x_ddot, y_dot, y_ddot, z_dot, z_ddot]
     
        # Angular Equations of Motion
        I11 = self.inertia[0]
        I22 = self.inertia[1]
        I33 = self.inertia[2]

        w1 = X[7]
        w2 = X[9]
        w3 = X[11]
        w1_dot = -(I33 - I22) * w2 * w3  / I11 + L[0] / I11
        w2_dot = -(I11 - I33) * w3 * w1  / I22 + L[1] / I22
        w3_dot = -(I22 - I11) * w1 * w2  / I33 + L[2] / I33

        angular_eom = [w1, w1_dot, w2, w2_dot, w3, w3_dot]

        return linear_eom + angular_eom


    def plot_quad(self, ax):
        rGA_inert = np.array([[self.rOG_inert[0], self.A_inert[0]], 
                    [self.rOG_inert[1], self.A_inert[1]], 
                    [self.rOG_inert[2], self.A_inert[2]]])

        rGB_inert = np.array([[self.rOG_inert[0], self.B_inert[0]], 
                    [self.rOG_inert[1], self.B_inert[1]], 
                    [self.rOG_inert[2], self.B_inert[2]]])

        rGC_inert = np.array([[self.rOG_inert[0], self.C_inert[0]], 
                    [self.rOG_inert[1], self.C_inert[1]], 
                    [self.rOG_inert[2], self.C_inert[2]]])

        rGD_inert = np.array([[self.rOG_inert[0], self.D_inert[0]], 
                    [self.rOG_inert[1], self.D_inert[1]], 
                    [self.rOG_inert[2], self.D_inert[2]]])

        line1 = ax.plot(rGA_inert[0], rGA_inert[1], -rGA_inert[2], color=self.x_pos_ax_color, linewidth=self.thick)
        ax.plot(rGB_inert[0], rGB_inert[1], -rGB_inert[2], color=self.color, linewidth=self.thick)
        ax.plot(rGC_inert[0], rGC_inert[1], -rGC_inert[2], color=self.color, linewidth=self.thick)
        ax.plot(rGD_inert[0], rGD_inert[1], -rGD_inert[2], color=self.color, linewidth=self.thick)
                
        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_zlabel('Z Axis')

        axes_length = 2
        ax.set_xlim(-axes_length, axes_length)
        ax.set_ylim(-axes_length, axes_length)
        ax.set_zlim(0, 2 * axes_length)

    def plot_body_frame_axes(self, ax):
        axes_length = 2

        ax.quiver(self.rOG_inert[0], self.rOG_inert[1], -self.rOG_inert[2], 
                  self.axes[0][0], self.axes[1][0], self.axes[2][0],
                  color=self.color, linewidth=3.0, linestyle='--')
        
        ax.quiver(self.rOG_inert[0], self.rOG_inert[1], -self.rOG_inert[2], 
                  self.axes[0][1], self.axes[1][1], -self.axes[2][1],
                  color=self.color, linestyle='-.')
        
        ax.quiver(self.rOG_inert[0], self.rOG_inert[1], -self.rOG_inert[2], 
                  self.axes[0][2], self.axes[1][2], -self.axes[2][2],
                  color=self.color)

class Environment:

    def __init__(self):
        self.axes_length = 2
        self.color = "black" 
        self.thick = 1

    def plot_inertial_frame_axes(self, ax):
        ax.quiver(0, 0, 0, self.axes_length, 0, 0, color=self.color, linestyle='--', linewidth=3.0, label="X-Axis")
        ax.quiver(0, 0, 0, 0, self.axes_length, 0, color=self.color, linestyle='-.', label="Y-Axis")
        ax.quiver(0, 0, 0, 0, 0, -self.axes_length, color=self.color, label="Z-Axis")
    

