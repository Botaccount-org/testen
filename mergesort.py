import matplotlib.pyplot as plt  # Import war an falscher stelle

def merge_sort(sort_list):   #Zu langer Variablen Name + Funktionen in Snake Case und lowercase
    if (len(sort_list) > 1): # Selbe spezifizierungen
        mid = len(sort_list) // 2
        left_half = sort_list[:mid]
        right_half = sort_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        l = 0
        r = 0
        i = 0

        while l < len(left_half) and r < len(right_half):
            if left_half[l] <= right_half[r]:
                sort_list[i] = left_half[l]     # Assignment Funktion war überflüssig
                l += 1
            else:
                sort_list[i] = right_half[r]
                r += 1
            i += 1

        while l < len(left_half):
            sort_list[i] = left_half[l]
            l += 1
            i += 1

        while r < len(right_half):
            sort_list[i] = right_half[r]
            r += 1
            i += 1

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list)) # x-Vorher 2mal definiert
plt.plot(x, my_list)
plt.show()
y = merge_sort(my_list)
plt.plot(x, my_list)
plt.show()