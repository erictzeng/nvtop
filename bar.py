from __future__ import division
from __future__ import print_function

from termcolor import colored

def color_scale(val, max, reverse=False, s=None):
    if s is None:
        s = str(val)
    ratio = val / max
    if reverse:
        ratio = 1 - ratio
    if ratio < 0.25:
        return colored(s, 'green')
    elif 0.25 <= ratio < 0.75:
        return colored(s, 'yellow')
    else:
        return colored(s, 'red')

def bar(ratio, width=30, full='|', empty=' ', caps='[]', color=True):
    buf = []
    if caps:
        width -= 2
        buf.append(caps[0])
    num_full = int(round(width * ratio))
    bars = full * num_full + empty * (width - num_full)
    if color:
        bars = color_scale(ratio, 1, s=bars)
    buf.append(bars)
    if caps:
        buf.append(caps[1])
    return ''.join(buf)


if __name__ == '__main__':
    print(bar(0.0), '0.0%')
    print(bar(0.2), '20.0%')
    print(bar(0.4), '40.0%')
    print(bar(0.6), '60.0%')
    print(bar(0.8), '80.0%')
    print(bar(1.0), '100.0%')
