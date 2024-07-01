#-- AIO433: Lê Ngọc Huân
import numpy as np

#Bài 1. Tạo hàm evaluate_classification_model
def evaluate_classification_model(TruePositive, FalsePositive, FalseNegative):
    if not isinstance(TruePositive, int):
        print('TruePositive must be int!')
        return None

    if not isinstance(FalsePositive, int):
        print('TruePositive must be int!')
        return None

    if not isinstance(FalseNegative, int):
        print('TruePositive must be int!')
        return None

    if TruePositive < 0 or FalsePositive <0  or FalseNegative < 0:
        print('Error:TruePositive and FalsePositive and FalseNegative must be greater than zero')

    try:
        precision = TruePositive / (TruePositive + FalsePositive)
        recall = TruePositive / (TruePositive + FalseNegative)
        f1_score = 2 * (precision * recall) / (precision + recall)
    except ZeroDivisionError as e:
        print(f'Error in calculation: {e}')
        return

    print(f'recall is {recall}')
    print(f'precision is {precision}')
    print(f'f1 score is {f1_score}')

#Bài 2. 3 Tạo hàm Activate function
import math
def validate_activate_function_name(fname):
    if fname.str.lower().strip() == 'sigmoid' or fname.str.lower().strip() == 'relu' or fname.str.lower().strip() == 'elu':
        return True
    else:
        return False

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return True

def calculate_activate_function():
    alpha = 0.01
    number = input('Please input x to calculate: ')
    if not is_number(number):
        print(f'{number} must be an integer, please try again!')
        return
    float(number)

    activation_function = input('Input Activation Function (sigmoid|relu|elu): ')
    if not validate_activate_function_name(activation_function):
        print(f'{activation_function} is not supported')
        return

    try:
        if activation_function == 'sigmoid':
            result = 1/(1 + (math.e**number))

        if activation_function == 'relu':
            result = 0 if number <= 0 else number

        if activation_function == 'elu':
            result = alpha*(math.e**number - 1) if number <= 0 else number
    except ZeroDivisionError as e:
        print(f'Error in calculation: {e}')
        return

    print(f'{activation_function}: f({number}): {result}')

#--------Bài 3. Tạo hàm regression loss function--------
import random
def regression_loss_function():
    num_sample = input('Please input number of generated samples: ')
    try:
        num_sample.isnumeric()
    except ValueError:
        print('Number must be an integer.')

    loss_name = input('Please input loss name (MAE|MSE): ')
    if not loss_name.lower().strip() == 'MAE' or loss_name.lower().strip() == 'MSE':
        print('Wrong loss name')
        return

    for sample_ith in range(num_sample):
        pred = random.uniform(1, 10)
        formatted_pred = "{:.15f}".format(pred)
        target = random.uniform(1, 10)
        formatted_target = "{:.15f}".format(target)
        loss_sum_MAE = 0
        loss_sum_MSE = 0
        if loss_name == 'MAE':
            loss_ith = abs(target - pred)
            loss_sum_MAE = loss_sum_MAE + loss_ith
            print(f'loss name: {loss_name}, sample: {sample_ith}, pred: {formatted_pred}, target: {formatted_target}, loss: {loss_ith}')

        if loss_name == 'MSE':
            loss_ith = (target - pred)**2
            loss_sum_MSE = loss_sum_MSE + loss_ith
            print(f'loss name: {loss_name}, sample: {sample_ith}, pred: {formatted_pred}, target: {formatted_target}, loss: {loss_ith}')

    if loss_name == 'MAE':
        final_loss_MAE = loss_sum_MAE/num_sample
        print(f'final MAE: {final_loss_MAE}')
    elif loss_name == 'MSE':
        final_loss_MSE = loss_sum_MSE/num_sample
        print(f'final MSE: {final_loss_MSE}')


#--------- Bài 4. Ước lượng các hàm số---------
def factorial(number):
    if number == 0 or number == 1:
        return 0
    else:
        result = 1
        for i in range(2, number +1):
            result = result*i
        return result

def approx_sin(x, n):
    sin_x = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        sin_x += term
    return sin_x

def approx_cos(x, n):
    cos_x = 0
    for i in range(n):
        temp = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
        cos_x = cos_x + temp
    return cos_x

def approx_sinh(x, n):
    sinh_x = 0
    for i in range(n):
        term = (x ** (2 * i + 1)) / factorial(2 * i + 1)
        sinh_x = sinh_x + term
    return sinh_x

def approx_cosh(x, n):
    cosh_x = 0
    for i in range(n):
        term = (x ** (2 * i)) / factorial(2 * i)
        cosh_x = cosh_x+ term
    return cosh_x

#----- bài 5. Mean Difference of single Root Error
def Mean_Difference_single_RootError(y, y_hat, n, p):
    y_root = y ** (1 / n)
    y_hat_root = y_hat ** (1 / n)
    difference = y_root - y_hat_root
    loss = difference ** p
    return loss
