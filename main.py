import tkinter
from tkinter import messagebox

import pynput

root = tkinter.Tk()
root.title('Counter')
root.geometry('280x150')

__count = 0

font_schema = (
  'Menlo',
  50
)

with open('count') as file:
  __count = int(file.read())

def updateFile(n):
  f = open('count', 'w')
  f.write(str(n))
  f.close()

def switch_key(key):
  switcher = {
    'Key.f7': 'F7', # Increment
    'Key.f8': 'F8'  # Decrement
  }
  return switcher.get(str(key), 'ERR_NO_KEY_FOUND')

def key_press(key):
  global __count
  action = switch_key(key)
  if action == 'F7':
    if __count == 99999:
      return
    __count += 1
    increment()
  else:
    if __count == 0:
      return
    __count -= 1
    decrement()
  if action != 'ERR_NO_KEY_FOUND':
    updateFile(__count)

# Command functions
def show_hotkeys():
  messagebox.showinfo('Hotkeys', 'F7: Increment\nF8: Decrement')

def padCount(n, d):
  return '0' * (d - len(str(n))) + str(n)

def reset_count():
  global __count
  __count = 0
  countLabel['text'] = padCount(__count, 5)
  updateFile(0)

def increment():
  countLabel['text'] = padCount(__count, 5)

def decrement():
  countLabel['text'] = padCount(__count, 5)

listener = pynput.keyboard.Listener(on_press=key_press)
listener.start()


menu = tkinter.Menu(root)
root.config(menu = menu)

file_menu = tkinter.Menu(menu)
menu.add_cascade(label = 'File', menu = file_menu)
file_menu.add_command(label = 'Hotkeys', command = show_hotkeys)
file_menu.add_command(label = 'Reset', command = reset_count)
file_menu.add_command(label = 'Exit', command = root.quit)

countLabel = tkinter.Label(root, text = padCount(__count, 5))
countLabel.config(font = font_schema)
countLabel.pack(side = tkinter.TOP)

incBtn = tkinter.Button(root, text = '+', command = lambda : key_press('Key.f7'))
resBtn = tkinter.Button(root, text = '0', command = reset_count)
helpBtn = tkinter.Button(root, text = '?', command = show_hotkeys)
decBtn = tkinter.Button(root, text = '-', command = lambda : key_press('Key.f8'))

incBtn.config(font = font_schema)
resBtn.config(font = font_schema)
helpBtn.config(font = font_schema)
decBtn.config(font = font_schema)

incBtn.pack(side = tkinter.LEFT)
resBtn.pack(side = tkinter.LEFT)
decBtn.pack(side = tkinter.RIGHT)
helpBtn.pack(side = tkinter.RIGHT)

root.mainloop()