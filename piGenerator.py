def calculate_pi_standard():
    """ A generator function to calculate the digits of Pi without additional dots. """
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4*q+r-t < n*t:
            yield n
            nr = 10*(r-n*t)
            n = ((10*(3*q+r))//t)-10*n
            q *= 10
            r = nr
        else:
            nr = (2*q+r)*l
            nn = (q*(7*k+2)+r*l)//(t*l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr

# Print the digits of Pi in standard format until interrupted
for digit in calculate_pi_standard():
    print(digit, end='')
