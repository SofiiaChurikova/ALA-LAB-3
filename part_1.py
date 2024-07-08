import numpy as np


def svd(matrix):
    eigenvalues_AAT, eigenvectors_AAT = np.linalg.eig(np.dot(matrix, matrix.T))
    sorted_values = np.argsort(eigenvalues_AAT)[::-1]
    eigenvalues_AAT = eigenvalues_AAT[sorted_values]
    U = eigenvectors_AAT[:, sorted_values]
    singular_values = np.sqrt(eigenvalues_AAT)
    E = np.diag(singular_values)
    V = np.dot(matrix.T, U) / singular_values
    print("U: \n", U)
    print("Σ: \n", E)
    print("V: \n", V.T)
    print("Reconstructed matrix: \n", np.dot(U, np.dot(E, V.T)).round(1))


matrix = np.array([[1, -3], [-3, 2]])
svd(matrix)

