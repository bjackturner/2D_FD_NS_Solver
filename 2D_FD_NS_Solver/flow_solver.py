import numpy as np

from finite_difference import ddx_5
from finite_difference import ddy_5
from finite_difference import d2dx_5
from finite_difference import d2dy_5

density = 1.225

def euler_step(u_velocity, v_velocity, pressure, temperature, density, kinematic_viscosity, gravity, dx, dy, dt):

    u_velocity_dt = np.zeros_like((u_velocity))
    v_velocity_dt = np.zeros_like((v_velocity))

    phi = np.zeros_like((temperature))
    temperature_dt = np.zeros_like((temperature))

    pressure_dt = np.zeros_like((pressure))

    u_velocity_dt[:,:] = u_velocity[:,:] + dt*(-u_velocity[:,:]*ddx_5(u_velocity[:,:], dx) - v_velocity[:,:]*ddy_5(u_velocity[:,:], dy) - ddx_5(pressure[:,:], dx)/density + kinematic_viscosity*(d2dx_5(u_velocity[:,:], dx) + d2dy_5(v_velocity[:,:], dy)) + gravity[0])

    v_velocity_dt[:,:] = v_velocity[:,:] + dt*(-u_velocity[:,:]*ddx_5(v_velocity[:,:], dx) - v_velocity[:,:]*ddy_5(v_velocity[:,:], dy) - ddy_5(pressure[:,:], dy)/density + kinematic_viscosity*(d2dx_5(u_velocity[:,:], dx) + d2dy_5(v_velocity[:,:], dy)) + gravity[1])

    phi[:,:] = kinematic_viscosity*(2*ddx_5(u_velocity[:,:], dx)**2 + 2*ddy_5(v_velocity[:,:], dy)**2 + 2*ddx_5(v_velocity[:,:], dx)*ddy_5(u_velocity[:,:], dy) + ddx_5(v_velocity[:,:], dx)*ddx_5(u_velocity[:,:], dx) + ddy_5(v_velocity[:,:], dy)*ddy_5(u_velocity[:,:], dy))

    return u_velocity_dt, v_velocity_dt, pressure_dt