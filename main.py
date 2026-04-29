import numpy as np
from nicegui import ui

inputs = []
first_diff = []
second_diff = []
third_diff = []
common_ratio = []
sequence = []

def init_data():
    global first_diff
    first_diff = np.empty(np.size(sequence) - 1)  if np.size(sequence) > 1 else np.array([])

    global second_diff
    second_diff = np.empty(np.size(first_diff) - 1) if np.size(first_diff) > 1 else np.array([])

    global third_diff
    third_diff = np.empty(np.size(second_diff) - 1) if np.size(second_diff) > 1 else np.array([])

    global common_ratio
    common_ratio = np.empty(np.size(sequence) - 1) if np.size(sequence) > 1 else np.array([])


def process_data():
    global first_diff, second_diff, third_diff, common_ratio
    try:
        first_diff = np.diff(sequence)
        second_diff = np.diff(first_diff)
        third_diff = np.diff(second_diff)
    except ValueError:
        pass

    calculate_common_ratio()


def calculate_common_ratio():
    global common_ratio
    _sequence = np.asanyarray (sequence)
    common_ratio = _sequence[1:] / _sequence[:-1]


def it_is_linear_sequence():
    return np.size(first_diff) > 0 and np.allclose(first_diff, first_diff[0])


def it_is_quadratic_sequence():
    second_diff_same = True

    for i in range(np.size(second_diff) - 1):
        if second_diff[i] != second_diff[i + 1]:
            second_diff_same = False
            break

    if second_diff_same:
        return True
    else:
        return False

     
def it_is_cubic_sequence():
    third_diff_same = True

    for i in range(np.size(third_diff) - 1):
        if third_diff[i] != third_diff[i + 1]:
            third_diff_same = False
            break

    if third_diff_same:
        return True
    else:
        return False


def it_is_geometric_sequence():
    common_ratio_same = True

    for i in range(np.size(common_ratio) - 1):
        if common_ratio[i] != common_ratio[i + 1]:
            common_ratio_same = False
            break

    if common_ratio_same:
        return True
    else:
        return False


def get_linear_nth_term():
    d = first_diff[0]
    print(sequence)
    a = sequence[0]
    nth_term = ""

    if d == 1:
        nth_term = "n"
    else:
        nth_term = str(d) + "n"

    if (a - d) > 0:
        nth_term = nth_term + "+" + str(a - d)
    else:
        if (a - d) != 0 and (a - d < 0):
            nth_term = nth_term + str(a - d)

    return nth_term


def get_quadratic_nth_term():
    a = second_diff[0] / 2.0
    b = first_diff[0] - (3.0 * a)
    c = sequence[0] - (a + b)
    nth_term = ""

    if a == 1:
        nth_term = "n^2"
    elif a == -1:
        nth_term = "-n^2"
    else:
        nth_term = str(a)

    if b == 1:
        nth_term = nth_term + "+n"
    elif b == -1:
        nth_term = nth_term + "-n"
    elif b > 1:
        nth_term = nth_term + "+" + str(b) + "n"
    else:
        if b < -1:
            nth_term = nth_term + str(b) + "n"

    if c < 0:
        nth_term = nth_term + str(c)
    else:
        if c != 0:
            nth_term = nth_term + "+" + str(c)
    
    return nth_term


def get_cubic_nth_term():
    a = third_diff[0] / 6.0
    b = (second_diff[0] - (12.0 * a)) / 2.0
    c = first_diff[0] - (3.0 * b) - (7.0 * a)
    d = sequence[0] - (a + b + c)
    nth_term = ""

    if a == 1:
        nth_term = "n^3"
    elif a == -1:
        nth_term =  "-n^3"
    else:
        nth_term = str(a) + "n^3"
    if b == 1:
        nth_term = nth_term + "+n^2"
    elif b == -1:
        nth_term = nth_term + "-n^2"
    elif b > 1:
        nth_term = nth_term  + "+" + str(b) + "n^2"
    else:
        if b < -1:
            nth_term = nth_term + str(b) + "n^2"

    if c == 1:
        nth_term = nth_term + "+n"
    elif c == -1:
        nth_term = nth_term + "-n"
    elif c > 1:
        nth_term = nth_term + "+" + str(c) + "n"
    else:
        if c < -1:
            nth_term = nth_term + str(c) + "n"

    if d < 0:
        nth_term = nth_term + str(d)
    else:
        if d != 0:
            nth_term = nth_term + "+" + str(d)

    return nth_term


def get_geometric_nth_term():
    pass


def update():
    global sequence
    sequence = np.array([inp.value for inp in inputs], dtype=float)

    init_data()
    process_data()

    if it_is_linear_sequence():
        result_label.set_text(f'Nth Term: {get_linear_nth_term()}')

    elif it_is_quadratic_sequence():
        result_label.set_text(f'Nth Term: {get_quadratic_nth_term()}')

    elif it_is_cubic_sequence():
        result_label.set_text(f'Nth Term: {get_cubic_nth_term()}')

    elif it_is_geometric_sequence():
        result_label.set_text(f'Nth Term: {get_geometric_nth_term()}')

    else:
        result_label.set_text(f'Nth Term: {"Generator Failed"}')


def generate_fields(count):
    input_container.clear()
    inputs.clear()
    
    with input_container:
        for i in range(int(count)):
            new_input = ui.number(label=f'value {i+1}', value=0, on_change=update).classes('w-20')
            inputs.append(new_input)
    
    update()

   
if __name__ in {"__main__", "__mp_main__"}:
    ui.query('body')

    ui.label('Nth Term Generator').classes('text-h4')
    with ui.row().classes('items-center'):
        count_input = ui.number(label='Sequence Length', value=5, min=2, step=1)
        ui.button('Reset Slots', on_click=lambda: generate_fields(count_input.value))

    input_container = ui.row().classes('flex-wrap')
    result_label = ui.label('Nth Term: ...').classes('text-h5 q-mt-md text-primary')
    generate_fields(count_input.value)

    ui.run()