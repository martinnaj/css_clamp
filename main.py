from fractions import Fraction

MIN_RESOLUTION = 320  # The resolution at which MIN_SIZE will be used
MAX_RESOLUTION = 1050  # The resolution at which MAX_SIZE will be used
MIN_SIZE = 10  # The smallest size value, will be shown at MIN_RESOLUTION
MAX_SIZE = 20  # The largest size value, will be shown at MAX_RESOLUTION
UNIT = 'px'  # The unit for MIN_SIZE and MAX_SIZE

a_f = Fraction(MAX_SIZE - MIN_SIZE, MAX_RESOLUTION - MIN_RESOLUTION)
a = float(a_f)
b = str(Fraction(MIN_SIZE) - (Fraction(MIN_RESOLUTION) * a_f).limit_denominator()).split('/')
negative = b[0].startswith('-')

sign = '- ' if negative else '+ '
part = sign + b[0][1:] if negative else sign + b[0]

print(f"clamp({MIN_SIZE}{UNIT}, calc({a} * 100vw {part}{UNIT} / {b[1]}), {MAX_SIZE}{UNIT})")
