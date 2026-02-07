#!/usr/bin/env python3
import sys

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

print("<h3>Python Script Result</h3>")

print("<b>Original Values:</b><br>")
print(f"x: {x}<br>")
print(f"y: {y}<br>")
print(f"z: {z}<br><br>")

print("<b>Calculation Steps:</b><br>")

print(f"Initial value of x: {x}<br>")

x += y
print(f"After x += y: {x}<br>")

x -= z
print(f"After x -= z: {x}<br>")

x *= y
print(f"After x *= y: {x}<br>")

if z != 0:
    x %= z
    print(f"After x %= z: {x}<br>")

    x /= z
    print(f"After x /= z: {x}<br>")
else:
    print("Skipping modulo and division (z = 0)<br>")

result = x + y + z
print(f"<br><b>Result:</b> x + y + z = {result}")
