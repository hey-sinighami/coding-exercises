"""Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.

Hour angle from 12:00
    Ha = 0.5 * (60 * H + M)
Minute angle from 12:00
    Ma = 6 * M

Where
    H = hours
    M = minutes

    A = |Ha - Ma|
    A = |0.5 * (60 * H - 11 * M)|

Eg:
    T = 2:20
    A = 50

    T = 10:16
    A = 148


Bonus: When, during the course of a day, will the angle be zero?

"""


def get_minute_angle(minutes):
    return 6 * minutes


def get_hour_angle(hours, minutes):
    return (0.5 * (60 * hours + minutes))


def get_angle(str_time):
    h, m = map(int, str_time.split(':'))
    angle = abs(get_hour_angle(h, m) - get_minute_angle(m))
    angle = angle % 360 if angle > 360 else angle

    return 360 - angle if angle > 180 else angle


assert(get_angle('2:20') == 50)
assert(get_angle('10:16') == 148)

assert(get_angle('2:20') == get_angle('14:20'))
assert(get_angle('10:16') == get_angle('22:16'))
assert(get_angle('1:05') == get_angle('13:05'))
assert(get_angle('7:54') == get_angle('19:54'))
assert(get_angle('12:00') == get_angle('00:00'))
assert(get_angle('23:38') == get_angle('11:38'))
assert(get_angle('08:43') == get_angle('20:43'))


def get_zero_angle_times():
    zero_angle_times = []
    for i in range(24):
        for j in range(60):
            str_time = '{}:{}'.format(i, j)
            if get_angle(str_time) == 0:
                zero_angle_times.append(str_time)

    print(zero_angle_times)

get_zero_angle_times()


