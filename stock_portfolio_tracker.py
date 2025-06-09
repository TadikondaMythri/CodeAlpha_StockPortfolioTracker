import os

def get_user_portfolio():
    stock_prices = {
        'TCS': 3405.05,
        'HDFC': 1925.25,
        'INFOSYS': 1542.35,
        'ITC': 416.80,
        'NESTLE': 2393.55,
        'TECH MAHINDRA': 1543.35,
        'ICIC': 416.80
    }

    print('Welcome to the Stock Portfolio Tracker!')
    print('Available stock prices:', ', '.join(stock_prices.keys()))
    portfolio = {}

    num_stocks = int(input('How many different stocks do you want to enter? : '))

    while num_stocks > 0:
        stock = input('Enter stock name: ').upper()
        if stock in stock_prices:
            quantity = int(input(f'Enter quantity of {stock}: '))
            portfolio[stock] = quantity
            num_stocks -= 1
        else:
            print('Invalid stock name! Please choose from the available list.')
    return stock_prices, portfolio


def display_portfolio_report(stock_prices, portfolio):
    print('\nPortfolio Summary:\n')
    total_val = 0.0
    report_lines = []

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total_val += value
        line = f"{stock}: {qty} shares × ₹{price:.2f} = ₹{value:.2f}"
        print(line)
        report_lines.append(line)

    print(f'\n Total Investment Value: ₹{total_val:.2f}')
    return report_lines, total_val


def save_to_file(report_lines, total_val):
    filename = "stock_report.txt"
    with open(filename, 'w', encoding = 'utf-8') as file:
        file.write('Stock Portfolio Report\n')
        file.write('---------------------------\n')
        for line in report_lines:
            file.write(line + '\n')
        file.write(f'\nTotal Investment Value: ₹{total_val:.2f}')
    print(f'\nReport saved to {filename} successfully.')

    filepath = os.path.abspath(filename)
    print(f'Opening file: {filepath}')
    os.startfile(filepath)


if __name__ == '__main__':
    stock_prices, portfolio = get_user_portfolio()
    report_lines, total_val = display_portfolio_report(stock_prices, portfolio)

    choice = input('\nDo you want to save this report to a .txt file? (yes/no): ').lower()
    if choice == 'yes':
        save_to_file(report_lines, total_val)
    else:
        print('Report not saved.')