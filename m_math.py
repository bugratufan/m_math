pi = 3.14159265358979
rad = pi / 180.0

#########################MATHEMATICAL FUNCTIONS BEGIN#########################

fac3 = 6.0
fac5 = 120.0
fac7 = 5040.0
fac9 = 362880.0
fac11 = 39916800

def m_sign(x,y):
    sign = x*y
    if sign < 0:
        return -1
    else:
        return 1

def m_acos(x):
    negate = float(x < 0)
    x = abs(x)
    ret = -0.0187293
    ret = ret * x
    ret = ret + 0.0742610
    ret = ret * x
    ret = ret - 0.2121144
    ret = ret * x
    ret = ret + 1.5707288
    ret = ret * (1.0 - x) ** 0.5
    ret = ret - 2 * negate * ret
    return negate * 3.14159265358979 + ret


def m_asin(x):
    return (pi / 2.0) - m_acos(x)


def m_atan2(y, x):
    sign = m_sign(y,x)
    h = (y ** 2 + x ** 2) ** 0.5
    if x == 0 and y == 0:
        val = 0
    else:
        cosVal = x / h
        val = m_acos(abs(cosVal))

    if x > 0:
        return val*sign
    elif x < 0:
        if y > 0:
            return (val - pi)*sign
        elif y == 0:
            return pi
        else:
            return (val - pi)*sign
    elif x == 0:
        if y > 0:
            return (pi/2.0)*sign
        elif y < 0:
            return -1*(pi/2.0)*sign
        else:
            return 0.0

def m_sinx(rad):
    rad = rad % (2 * pi)
    if rad > pi:
        rad = rad - pi
        return -1 * (rad - ((rad ** 3) / fac3) + ((rad ** 5) / fac5) - ((rad ** 7) / fac7) + ((rad ** 9) / fac9) - (
                (rad ** 11) / fac11))
    else:
        return rad - ((rad ** 3) / fac3) + ((rad ** 5) / fac5) - ((rad ** 7) / fac7) + ((rad ** 9) / fac9) - (
                (rad ** 11) / fac11)


def m_cosx(rad):
    return m_sinx((pi / 2) - rad)


def m_tanx(rad):
    return m_sinx(rad) / m_cosx(rad)
