import numpy
import numpy as np
import matplotlib.pyplot as plt

def gs_cofficient(v1, v2):
    return numpy.dot(v2, v1) / numpy.dot(v1, v1)

def multiply(cofficient, v):
    return map((lambda x : x * cofficient), v)

def proj(v1, v2):
    return multiply(gs_cofficient(v1, v2) , v1)

# Gram-schmidt algorithm
def gs(X, row_vecs=True, norm = True):
    if not row_vecs:
        X = X.T
    Y = X[0:1,:].copy()
    for i in range(1, X.shape[0]):
        proj = numpy.diag((X[i,:].dot(Y.T)/numpy.linalg.norm(Y,axis=1)**2).flat).dot(Y)
        Y = numpy.vstack((Y, X[i,:] - proj.sum(0)))
    if norm:
        Y = numpy.diag(1/numpy.linalg.norm(Y,axis=1)).dot(Y)
    if row_vecs:
        return Y
    else:
        return Y.T
    
def w1o16():
    A = np.array([[1, 0, 0, 0, 0],
                    [1, np.pi/6, (np.pi/6)**2, (np.pi/6)**3, (np.pi/6)**4],
                    [1, np.pi/4, (np.pi/4)**2, (np.pi/4)**3, (np.pi/4)**4],
                    [1, np.pi/3, (np.pi/3)**2, (np.pi/3)**3, (np.pi/3)**4],
                    [1, np.pi/2, (np.pi/2)**2, (np.pi/2)**3, (np.pi/2)**4]])

    b = np.array([1, np.sqrt(3)/2, np.sqrt(2)/2, 1/2, 0])

    x = np.linalg.solve(A, b)

    print(x)

    x_vals = np.linspace(-1, 2, 1000)
    y_vals_p = 1 + 0.16405728 * x_vals - 0.97340685 * x_vals**2 - 0.29122656 * x_vals**3 + 1.11665148 * x_vals**4
    y_vals_cos = np.cos(x_vals)

    plt.plot(x_vals, y_vals_p, label="Interpolating Polynomial")
    plt.plot(x_vals, y_vals_cos, label="cos(x)")
    plt.legend()
    plt.show()

# Define the Lagrange polynomials
def lagrange_poly(i, x, t):
    n = len(t)
    num = 1
    den = 1
    for j in range(n):
        if j != i:
            num *= (x - t[j])
            den *= (t[i] - t[j])
    return num / den

def w1o17():
    # Define the dataset
    t = np.array([1, 2, 3])
    y = np.array([4, 0, 12])

    # Create a grid of x values to plot the polynomials
    x = np.linspace(t.min(), t.max(), 100)

    # Compute the Lagrange polynomials and plot them
    fig, ax = plt.subplots()
    for i in range(len(t)):
        ax.plot(x, lagrange_poly(i, x, t), label=f"$L_{i+1}(t)$")
    
    ax.scatter(t, y, color='red', label='Data points')
    ax.legend()
    plt.show()
