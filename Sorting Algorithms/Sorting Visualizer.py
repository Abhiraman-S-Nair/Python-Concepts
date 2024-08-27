import tkinter as tk
import random
import time

# Sorting Algorithms
def bubble_sort(data, draw_data, delay):
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(data, ['red' if x == j or x == j + 1 else 'white' for x in range(len(data))])
                time.sleep(delay)
    draw_data(data, ['green' for x in range(len(data))])


def insertion_sort(data, draw_data, delay):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            draw_data(data, ['yellow' if x == j or x == j + 1 else 'white' for x in range(len(data))])
            time.sleep(delay)
        data[j + 1] = key
    draw_data(data, ['green' for x in range(len(data))])


def selection_sort(data, draw_data, delay):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        draw_data(data, ['red' if x == i or x == min_idx else 'white' for x in range(len(data))])
        time.sleep(delay)
    draw_data(data, ['green' for x in range(len(data))])


def merge_sort(data, draw_data, delay):
    merge_sort_alg(data, 0, len(data) - 1, draw_data, delay)
    draw_data(data, ['green' for x in range(len(data))])


def merge_sort_alg(data, left, right, draw_data, delay):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, draw_data, delay)
        merge_sort_alg(data, middle + 1, right, draw_data, delay)
        merge(data, left, middle, right, draw_data, delay)


def merge(data, left, middle, right, draw_data, delay):
    left_part = data[left:middle + 1]
    right_part = data[middle + 1:right + 1]

    left_idx = right_idx = 0
    for data_idx in range(left, right + 1):
        if left_idx < len(left_part) and (right_idx >= len(right_part) or left_part[left_idx] <= right_part[right_idx]):
            data[data_idx] = left_part[left_idx]
            left_idx += 1
        else:
            data[data_idx] = right_part[right_idx]
            right_idx += 1
        draw_data(data, ['yellow' if x >= left and x <= right else 'white' for x in range(len(data))])
        time.sleep(delay)


def quick_sort(data, draw_data, delay):
    quick_sort_alg(data, 0, len(data) - 1, draw_data, delay)
    draw_data(data, ['green' for x in range(len(data))])


def quick_sort_alg(data, low, high, draw_data, delay):
    if low < high:
        pivot_index = partition(data, low, high, draw_data, delay)
        quick_sort_alg(data, low, pivot_index - 1, draw_data, delay)
        quick_sort_alg(data, pivot_index + 1, high, draw_data, delay)


def partition(data, low, high, draw_data, delay):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            draw_data(data, ['red' if x == i or x == j else 'white' for x in range(len(data))])
            time.sleep(delay)
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1


def heap_sort(data, draw_data, delay):
    n = len(data)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, draw_data, delay)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]  # swap
        draw_data(data, ['red' if x == i or x == 0 else 'white' for x in range(len(data))])
        time.sleep(delay)
        heapify(data, i, 0, draw_data, delay)

    draw_data(data, ['green' for x in range(len(data))])


def heapify(data, n, i, draw_data, delay):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if left < n and data[i] < data[left]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and data[largest] < data[right]:
        largest = right

    # Change root, if needed
    if largest != i:
        data[i], data[largest] = data[largest], data[i]  # swap
        draw_data(data, ['red' if x == i or x == largest else 'white' for x in range(len(data))])
        time.sleep(delay)
        # Heapify the root.
        heapify(data, n, largest, draw_data, delay)


# Function to create the GUI
def create_gui():
    # Main window
    window = tk.Tk()
    window.title("Sorting Algorithm Visualizer")
    window.maxsize(900, 600)
    window.config(bg='black')

    # Variables
    selected_algorithm = tk.StringVar()
    data = []

    # Functions for GUI
    def draw_data(data, color_array):
        canvas.delete("all")
        c_height = 380
        c_width = 600
        x_width = c_width / (len(data) + 1)
        offset = 30
        spacing = 10
        normalized_data = [i / max(data) for i in data]
        for i, height in enumerate(normalized_data):
            x0 = i * x_width + offset + spacing
            y0 = c_height - height * 340
            x1 = (i + 1) * x_width + offset
            y1 = c_height
            canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
        window.update_idletasks()

    def generate_data():
        global data
        data = [random.randint(1, 100) for _ in range(50)]
        draw_data(data, ['white' for x in range(len(data))])

    def start_sorting():
        global data
        if not data:
            return
        if selected_algorithm.get() == 'Bubble Sort':
            bubble_sort(data, draw_data, 0.01)
        elif selected_algorithm.get() == 'Insertion Sort':
            insertion_sort(data, draw_data, 0.01)
        elif selected_algorithm.get() == 'Selection Sort':
            selection_sort(data, draw_data, 0.01)
        elif selected_algorithm.get() == 'Merge Sort':
            merge_sort(data, draw_data, 0.01)
        elif selected_algorithm.get() == 'Quick Sort':
            quick_sort(data, draw_data, 0.01)
        elif selected_algorithm.get() == 'Heap Sort':
            heap_sort(data, draw_data, 0.01)

    # UI Frame
    ui_frame = tk.Frame(window, width=600, height=200, bg='grey')
    ui_frame.grid(row=0, column=0, padx=10, pady=5)

    # Dropdown menu for selecting sorting algorithm
    tk.Label(ui_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    alg_menu = tk.OptionMenu(ui_frame, selected_algorithm, 'Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort')
    alg_menu.grid(row=0, column=1, padx=5, pady=5)
    selected_algorithm.set('Bubble Sort')

    # Buttons
    tk.Button(ui_frame, text="Generate Data", command=generate_data, bg='red').grid(row=1, column=0, padx=5, pady=5)
    tk.Button(ui_frame, text="Start Sorting", command=start_sorting, bg='green').grid(row=1, column=1, padx=5, pady=5)

    # Canvas for visualization
    canvas = tk.Canvas(window, width=600, height=380, bg='black')
    canvas.grid(row=1, column=0, padx=10, pady=5)

    window.mainloop()

# Main Driver Function
def main():
    create_gui()

if __name__ == "__main__":
    main()
