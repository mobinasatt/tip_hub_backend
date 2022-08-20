from . import jalali


def persian_number(t_str):
    numbers = {
        "0": "۰",
        "1": "۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
    }
    for e, p in numbers.items():
        t_str = t_str.replace(e, p)
    return t_str


def jalali_converter(time):
    jalali_month = [
        'فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان',
        'آذر', 'دی', 'بهمن', 'اسفند'
    ]

    time_str = "{},{},{}".format(time.year, time.month, time.day)
    time_tuple = jalali.Gregorian(time_str).persian_tuple()

    time_list = list(time_tuple)
    for index, month in enumerate(jalali_month):
        if time_list[1] == index + 1:
            time_list[1] = month
            break

    output = "{} {} {}".format(time_list[2], time_list[1], time_list[0])

    return persian_number(output)
