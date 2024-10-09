import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.reshape(list, (3,3))

    def calc_rows(matrix, func):
        result = []
        for row in matrix:
            result.append(func(row))
        return result
    
    def calc_cols(matrix, func):
        result = []
        for column in matrix.T:
            result.append(func(column))
        return result


    calculations = {
        'mean': [calc_cols(matrix, np.mean), calc_rows(matrix, np.mean), np.mean(matrix)],
        'variance': [calc_cols(matrix, np.var), calc_rows(matrix, np.var), np.var(matrix)],
        'standard deviation': [calc_cols(matrix, np.std), calc_rows(matrix, np.std), np.std(matrix)],
        'max': [calc_cols(matrix, np.max), calc_rows(matrix, np.max), np.max(matrix)],
        'min': [calc_cols(matrix, np.min), calc_rows(matrix, np.min), np.min(matrix)],
        'sum': [calc_cols(matrix, np.sum), calc_rows(matrix, np.sum), np.sum(matrix)]
    }

    return calculations