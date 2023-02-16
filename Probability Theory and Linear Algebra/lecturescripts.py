import numpy

def gs_cofficient(v1, v2):
    return numpy.dot(v2, v1) / numpy.dot(v1, v1)

def multiply(cofficient, v):
    return map((lambda x : x * cofficient), v)

def proj(v1, v2):
    return multiply(gs_cofficient(v1, v2) , v1)

# gram-schmidt algoritmen
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
        