import numpy as np 
def compute_vector_length(vector):
    len_of_vector = np.sqrt(sum(vector**2))
    return len_of_vector

def compute_dot_product(vector1, vector2):
    result = np.dot(vector1*vector2)
    return result

def maxtrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result

def inverse_matrix(matrix):
    result = np.linalg.inv(matrix)
    return result

def compute_eigenvalues_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues,eigenvectors

def compute_cosine(vector1, vector2):
    cosine_result = compute_dot_product(vector1, vector2) / (compute_vector_length(vector1)*compute_vector_length(vector2))
    return cosine_result


def main():
    return


if __name__ == '__main__':
    main()
