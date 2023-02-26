# write your code here
import math
import sys
import argparse

parser = argparse.ArgumentParser(description="Calculator!")
parser.add_argument("-t", "--type", choices=["annuity", "diff"])
parser.add_argument("-p1", "--principal")
parser.add_argument("-p2", "--periods")
parser.add_argument("-i", "--interest")
parser.add_argument("-p3", "--payment")

args = parser.parse_args()

if args.interest:
    interest = float(args.interest)
else:
    print('Incorrect parameters')
    sys.exit()

if args.type == 'diff':
    loan_principal = int(args.principal)
    periods = int(args.periods)
    print('Your loan principal is :', loan_principal)
    print('Your number of periods: ', periods)
    print('Your interest rate is: ', interest)
    nominal_interest_rate = interest / (12 * 100)
    total_amount = 0
    for i in range(1, periods + 1):
        payment = math.ceil((loan_principal / periods) \
                            + nominal_interest_rate * (loan_principal - (loan_principal * (i - 1) / periods)))
        total_amount += payment
        print(f'Month {i}: payment is {payment}')
    overpayment = total_amount - loan_principal
    print()
    print(f'Overpayment = {overpayment}')

elif args.type == 'annuity':

    # Same as parameter p
    if args.payment and args.periods and args.interest:
        periods = int(args.periods)
        payment = int(args.payment)
        nominal_interest_rate = interest / (12 * 100)

        loan_principal = math.ceil(payment
                                   / ((nominal_interest_rate * (1 + nominal_interest_rate) ** periods)
                                      / ((1 + nominal_interest_rate) ** periods - 1)))

        print(f'Your loan principal = {loan_principal}!')
        print(f'Overpayment = ')
        sys.exit()

    # Same as parameter a
    elif args.principal and args.periods and args.interest:
        periods = int(args.periods)
        loan_principal = int(args.principal)
        nominal_interest_rate = interest / (12 * 100)
        monthly_payment = math.ceil(loan_principal * (nominal_interest_rate * (1 + nominal_interest_rate) ** periods)
                                    / ((1 + nominal_interest_rate) ** periods - 1))

        print(f'Your annuity payment = {monthly_payment}!')
        print(f'Overpayment = ')

    # Same as parameter n
    elif args.principal and args.payment and args.interest:
        payment = int(args.payment)
        loan_principal = int(args.principal)

        nominal_interest_rate = interest / (12 * 100)

        number_of_monthly_payments = math.log(payment / (payment - nominal_interest_rate * loan_principal),
                                              1 + nominal_interest_rate)
        months = math.ceil(number_of_monthly_payments)
        years = math.floor(months / 12)

        total_amount = payment * months
        overpayment = total_amount - loan_principal

        if months < 12 and months & 12 != 0:
            if months == 1:
                print(f'It will take {months} month to repay this loan!')
            else:
                print(f'It will take {months} months to repay this loan!')
        elif months == 12:
            print(f'It will take {years} year to repay this loan!')
        elif months > 12 and months % 12 == 0:
            print(f'It will take {years} years to repay this loan!')
        else:
            months = months % 12
            print(f'It will take {years} years and {months} months to repay this loan!')
        print(f'Overpayment = ', overpayment)
