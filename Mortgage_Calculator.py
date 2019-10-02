interest_rate = int(input('Процентная ставка (% годовых):'))
initial_loan_amount = int(input("изначальная сумма займа:"))
number_of_periods = int(input('количество периодов:'))

interest_rate = interest_rate / 100
number_of_periods = number_of_periods * 12

annuity_payment = (initial_loan_amount * interest_rate * (1 + interest_rate) ** number_of_periods) / (
        (1 + interest_rate) ** number_of_periods - 1)

total_payout = (annuity_payment * 12) * number_of_periods
print(f'Месячные выплаты составляют : {annuity_payment}')

# Рассчитать выплаты по кредиту
# Рассчитать месячные выплаты (m) и суммарную выплату (s) по кредиту.
#
# О кредите известно, что он составляет n рублей, берется на y лет, под p процентов.
#
# Месячные выплаты находятся по формуле:
# m = (n * p * (1 + p)y) / (12 * ((1 + p)y – 1)), где p выражается в долях единицы, а не процентах.
#
# Суммарная выплата представляет собой выплаты за все месяцы каждого года:
# s = (m * 12) * y
