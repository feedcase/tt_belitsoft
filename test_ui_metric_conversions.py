from time import sleep

import pytest


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    fahrenheit = '{:.7f}'.format(fahrenheit)
    fahrenheit = fahrenheit[:8]
    result = f'{celsius}°C= {fahrenheit}°F'
    return result


def meters_to_feet(meters):
    feet = int(meters // .3048)
    inches = meters / .3048 % 1 * 12
    inches = '{:.7f}'.format(inches)
    inches = float(inches[:8])
    inches += 0.000001
    result = f'{meters}m= {feet}ft {inches}in'
    return result


def ounces_to_grams(ounces):
    gram = ounces / 0.0352739596166073
    gram = '%.4f' % gram
    gram = gram[:8]
    result = f'{ounces}oz= {gram}g'
    return result


@pytest.mark.parametrize(
    'url, type_, value',
    [
        ('https://www.metric-conversions.org/temperature/celsius-to-fahrenheit.htm', 'celsius', 5),
        ('https://www.metric-conversions.org/length/meters-to-feet.htm', 'meters', 1),
        ('https://www.metric-conversions.org/weight/ounces-to-grams.htm', 'ounces', 24)
    ]
)
def test_metric_conversion(url, type_, value, get_driver):
    get_driver.get(url)
    get_driver.find_element_by_id('argumentConv').send_keys(value)
    answer = get_driver.find_element_by_id('answer').text
    if type_ == 'celsius':
        result = celsius_to_fahrenheit(value)
    if type_ == 'meters':
        result = meters_to_feet(value)
    if type_ == 'ounces':
        result = ounces_to_grams(value)
    assert answer == result
