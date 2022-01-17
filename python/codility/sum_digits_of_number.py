# For n = 29, the output should be
# solution(n) = 11.

def solution(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum