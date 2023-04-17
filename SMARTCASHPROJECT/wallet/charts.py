import matplotlib.pyplot as plt
plt.switch_backend('agg')
from django.http import HttpResponse


def create_charts(movements):
    return [line_chart_date(movements), pie_chart_movements(movements)]


def pie_chart_movements(movements):
    categories = {}
    for movement in movements:
        if movement[-1] in categories:
            categories[movement[-1]] += movement[4]
        else:
            categories[movement[-1]] = movement[4]
    values, labels = categories.values(), categories.keys()
    plt.figure()
    plt.pie(values, labels=labels)
    plt.title('Gastos en categorías')
    plt.savefig('static/images/pie_chart.png')


def pie_chart_movements_direction(movements, direction):
    categories = {}
    for movement in movements:
        if movement[-1] in categories:
            categories[movement[-1]] += movement[4]
        else:
            categories[movement[-1]] = movement[4]
    values, labels = categories.values(), categories.keys()
    plt.figure()
    plt.pie(values, labels=labels, autopct='%1.0f%%')
    plt.title(f'{direction.capitalize()}s en categorías')
    plt.savefig(f'static/images/pie_chart_{direction}.png')


def line_chart_date(movements):
    dates = {}
    for movement in movements:
        if movement[5] in dates:
            dates[movement[5]] += movement[4]
        else:
            dates[movement[5]] = movement[4]
    figure = plt.figure()
    values, labels = dates.values(), [x.strftime("%m/%d/%Y") for x in dates.keys()]
    plt.plot(labels, values, figure=figure)
    plt.title('Gastos en el tiempo')
    plt.xlabel('Fecha', figure=figure)
    plt.ylabel('Dinero gastado', figure=figure)
    plt.savefig('static/images/line_chart.png')


def line_chart_date_direction(movements, direction):
    dates = {}
    for movement in movements:
        if movement[5] in dates:
            dates[movement[5]] += movement[4]
        else:
            dates[movement[5]] = movement[4]
    figure = plt.figure()
    values, labels = dates.values(), [x.strftime("%m/%d/%Y") for x in dates.keys()]
    plt.plot(labels, values, figure=figure, color='blue' if direction == 'entrada' else 'red')
    plt.title(f'{direction.capitalize()}s en el tiempo')
    plt.xlabel('fecha', figure=figure)
    plt.ylabel(f'{direction.capitalize()}', figure=figure)
    plt.savefig(f'static/images/line_chart_{direction}.png')
