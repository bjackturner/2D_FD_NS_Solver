import numpy as np
import matplotlib.pyplot as plt
import time

## Three point finite difference (first and second order) error = O(h^2)

# Solves a five point, first order, finite difference of a scalar field in x direction 
def ddx_3(field, dx):

    field_new = np.zeros_like(field) # Preallocate memory


    return field_new

# Solves a five point, first order, finite difference of a scalar field in y direction 
def ddy_3(field, dy):

    field_new = np.zeros_like(field) # Preallocate memory


    return field_new

# Solves a five point, second order, finite difference of a scalar field in x direction 
def d2dx_3(field, dx):

    field_new = np.zeros_like(field) # Preallocate memory


    return field_new

# Solves a five point, second order, finite difference of a scalar field in y direction 
def d2dy_3(field, dy):

    field_new = np.zeros_like(field) # Preallocate memory

    return field_new


## Five point finite difference (first and second order) error = O(h^4)

# Solves a five point, first order, finite difference of a scalar field in x direction 
def ddx_5(field, dx):

    field_new = np.zeros_like(field) # Preallocate memory

    # Partial derivative in the x direction of first two columns using forward 5 point method
    field_new[:2,:] = (-25*field[:2,:] + 48*field[1:3,:] - 36*field[2:4,:] + 16*field[3:5,:] - 3*field[4:6,:]) / (12 * dx)

    # Partial derivative in the x direction of middle columns using central 5 point method
    field_new[2:-2,:] = (field[:-4,:] - 8*field[1:-3,:] + 8*field[3:-1,:] - field[4:,:]) / (12 * dx)

    # Partial derivative in the x direction of last two columns using backward 5 point method
    field_new[-2:,:] = (25*field[-2:,:] - 48*field[-3:-1,:] + 36*field[-4:-2,:] - 16*field[-5:-3,:] + 3*field[-6:-4,:]) / (12 * dx)

    return field_new

# Solves a five point, first order, finite difference of a scalar field in y direction 
def ddy_5(field, dy):

    field_new = np.zeros_like(field) # Preallocate memory

    # Partial derivative in the y direction of first two rows using forward 5 point method
    field_new[:,:2] = (-25*field[:,:2] + 48*field[:,1:3] - 36*field[:,2:4] + 16*field[:,3:5] - 3*field[:,4:6]) / (12 * dy)

    # Partial derivative in the y direction of middle rows using central 5 point method
    field_new[:,2:-2] = (field[:,:-4] - 8*field[:,1:-3] + 8*field[:,3:-1] - field[:,4:]) / (12 * dy)

    # Partial derivative in the y direction of last two rows using backward 5 point method
    field_new[:,-2:] = (25*field[:,-2:] - 48*field[:,-3:-1] + 36*field[:,-4:-2] - 16*field[:,-5:-3] + 3*field[:,-6:-4]) / (12 * dy)

    return field_new

# Solves a five point, second order, finite difference of a scalar field in x direction 
def d2dx_5(field, dx):

    field_new = np.zeros_like(field) # Preallocate memory

    # 2nd partial derivative in the x direction of first two columns using forward 5 point method
    field_new[:2,:] = (35*field[:2,:] - 104*field[1:3,:] + 114*field[2:4,:] - 56*field[3:5,:] + 11*field[4:6,:]) / (12 * dx**2)

    # 2nd partial derivative in the x direction of middle columns using central 5 point method
    field_new[2:-2,:] = (-field[:-4,:] + 16*field[1:-3,:] - 30*field[2:-2,:] + 16*field[3:-1,:] - field[4:,:]) / (12 * dx**2)

    # 2nd partial derivative in the x direction of last two columns using backward 5 point method
    field_new[-2:,:] = (35*field[-2:,:] - 104*field[-3:-1,:] + 114*field[-4:-2,:] - 56*field[-5:-3,:] + 11*field[-6:-4,:]) / (12 * dx**2)

    return field_new

# Solves a five point, second order, finite difference of a scalar field in y direction 
def d2dy_5(field, dy):

    field_new = np.zeros_like(field) # Preallocate memory

    # 2nd partial derivative in the y direction of first two rows using forward 5 point method
    field_new[:,:2] = (35*field[:,:2] - 104*field[:,1:3] + 114*field[:,2:4] - 56*field[:,3:5] + 11*field[:,4:6]) / (12 * dy**2)

    # 2nd partial derivative in the y direction of the middle rows using central 5 point method
    field_new[:,2:-2] = (-field[:,:-4] + 16*field[:,1:-3] - 30*field[:,2:-2] + 16*field[:,3:-1] - field[:,4:]) / (12 * dy**2)

    # 2nd partial derivative in the y direction of last two rows using backward 5 point method
    field_new[:,-2:] = (35*field[:,-2:] - 104*field[:,-3:-1] + 114*field[:,-4:-2] - 56*field[:,-5:-3] + 11*field[:,-6:-4]) / (12 * dy**2)

    return field_new


