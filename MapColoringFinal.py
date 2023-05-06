import random
import tkinter as tk

colors = ['Red', 'Blue', 'Green']
states = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V']


neighbors = {}
neighbors['WA'] = ['NT', 'SA']


neighbors['NT'] = ['WA', 'SA', 'Q']
neighbors['SA'] = ['WA', 'NT', 'Q', 'NSW', 'V']
neighbors['Q'] = ['NT', 'SA', 'NSW']
neighbors['NSW'] = ['Q', 'SA', 'V']
neighbors['V'] = ['SA', 'NSW']

state_color = {}

def mapcoloring(state, color):
    for neighbor in neighbors.get(state):
        neighbor_color = state_color.get(neighbor)
        if neighbor_color == color:
            return False
    return True

def get_color_for_state(state):
    available_colors = colors.copy()
    for neighbor in neighbors.get(state):
        neighbor_color = state_color.get(neighbor)
        if neighbor_color in available_colors:
            available_colors.remove(neighbor_color)
    if not available_colors:
        raise ValueError("No Solution {}".format(state))
    return random.choice(available_colors)

def main():
    for state in states:
        state_color[state] = get_color_for_state(state)

    return state_color

def generate_new_map():
    global state_color
    state_color = {}
    try:
        state_color = main()
        map_canvas.delete("all")
        for state, color in state_color.items():
            x, y = state_positions[state]
            map_canvas.create_rectangle(x-30, y-30, x+30, y+30, fill=color, outline='black')
    except ValueError as e:
        status_label.config(text=str(e))

def reset_map():
    global state_color
    state_color = {}
    map_canvas.delete("all")
    status_label.config(text="")

state_positions = {
    'WA': (50, 50),
    'NT': (250, 100),
    'SA': (150, 200),
    'Q': (350, 100),
    'NSW': (450, 200),
    'V': (350, 300)
}

# GUI implementation
root = tk.Tk()
root.title("Map Coloring")

map_canvas = tk.Canvas(root, width=500, height=400)
map_canvas.pack(side=tk.TOP)


# View and Reset
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP)
generate_button = tk.Button(button_frame, text="View Map", command=generate_new_map)
generate_button.pack(side=tk.LEFT)
reset_button = tk.Button(button_frame, text="Reset Map", command=reset_map)
reset_button.pack(side=tk.LEFT)

status_label = tk.Label(root, fg="red")
status_label.pack(side=tk.TOP)

root.mainloop()
