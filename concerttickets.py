# ----------------------------------------------megoldas---------------------------------------
import bisect
import random


def jegyeladas(n, m, jegyarak, maximum_arak):
    # Rendezés növekvő sorrendben
    jegyarak.sort()
    eredmenyek = []

    for max_ar in maximum_arak:
        # Keresés bináris kereséssel
        index = bisect.bisect_right(jegyarak, max_ar) - 1

        if index >= 0 and jegyarak[index] <= max_ar:
            eredmenyek.append(jegyarak[index])
            # Jegy eltávolítása
            jegyarak.pop(index)
        else:
            eredmenyek.append(-1)

    return eredmenyek


# ------------------------------------------ Tesztesetek ---------------------------------------------

# Teszt 1
n1, m1 = 4, 3
jegyarak1 = [10, 30, 20, 40]
maximum_arak1 = [25, 35, 10]
print(jegyeladas(n1, m1, jegyarak1, maximum_arak1))  # Elvárt eredmény: [20, 30, 10]

# Teszt 2
n2, m2 = 5, 5
jegyarak2 = [50, 20, 40, 60, 30]
maximum_arak2 = [30, 60, 25, 50, 10]
print(
    jegyeladas(n2, m2, jegyarak2, maximum_arak2)
)  # Elvárt eredmény: [30, 60, 20, 40, -1]

# Teszt 3
n3, m3 = 3, 2
jegyarak3 = [10, 20, 30]
maximum_arak3 = [15, 25]
print(jegyeladas(n3, m3, jegyarak3, maximum_arak3))  # Elvárt eredmény: [10, 20]

# Teszt 4
n4, m4 = 3, 3
jegyarak4 = [100, 200, 300]
maximum_arak4 = [150, 250, 350]
print(jegyeladas(n4, m4, jegyarak4, maximum_arak4))  # Elvárt eredmény: [100, 200, 300]

# Teszt 5
n5, m5 = 6, 3
jegyarak5 = [5, 10, 20, 30, 40, 50]
maximum_arak5 = [15, 25, 45]
print(jegyeladas(n5, m5, jegyarak5, maximum_arak5))  # Elvárt eredmény: [10, 20, 40]

# Teszt 6
n6, m6 = 5, 2
jegyarak6 = [100, 200, 300, 400, 500]
maximum_arak6 = [150, 250]
print(jegyeladas(n6, m6, jegyarak6, maximum_arak6))  # Elvárt eredmény: [100, 200]

# Teszt 7
n7, m7 = 2, 3
jegyarak7 = [10, 15]
maximum_arak7 = [10, 20, 5]
print(jegyeladas(n7, m7, jegyarak7, maximum_arak7))  # Elvárt eredmény: [10, 15, -1]

# Teszt 8
n8, m8 = 4, 4
jegyarak8 = [60, 50, 40, 30]
maximum_arak8 = [50, 40, 30, 20]
print(jegyeladas(n8, m8, jegyarak8, maximum_arak8))  # Elvárt eredmény: [50, 40, 30, -1]

# Teszt 9
n9, m9 = 3, 2
jegyarak9 = [7, 3, 5]
maximum_arak9 = [6, 8]
print(jegyeladas(n9, m9, jegyarak9, maximum_arak9))  # Elvárt eredmény: [5, 7]

# Teszt 10
n10, m10 = 5, 5
jegyarak10 = [random.randint(20, 60) for i in range(1000)]
maximum_arak10 = [random.randint(20, 60) for i in range(1000)]
print(jegyeladas(n10, m10, jegyarak10, maximum_arak10))
