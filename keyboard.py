from keyboard_listener import KeyboardListener, Combo, KeyWord
import pyperclip
from pynput.keyboard import Key, Controller
import time
import random

def copy_text():
	keyboard = Controller()
	keyboard.press(Key.ctrl_l)
	keyboard.press('c')
	keyboard.release(Key.ctrl_l)
	time.sleep(0.1)
	
def paste_text():
	keyboard = Controller()
	keyboard.press(Key.ctrl_l)
	keyboard.press('v')
	keyboard.release(Key.ctrl_l)
	
def delete(string):
	keyboard = Controller()
	for char in string:
		keyboard.press(Key.backspace)
		keyboard.release(Key.backspace)
		time.sleep(0.05)

def modifyText(modification):
	data = pyperclip.paste()
	print(f'current: {data}')
	copy_text()
	data = pyperclip.paste()
	print(f'copied: {data}')

	if(modification == 'upper'):
		data = data.upper()
	
	elif(modification == 'lower'):
		data = data.lower()

	elif modification == 'capitalize' :
		data = data.capitalize()

	elif modification == 'reverse' :
		data = data[::-1]

	elif modification == 'eval':
		try:
			data = eval(data)
		except:
			data = data

	elif modification == 'same_line':
		data = data + '\n' + data

	elif modification == "html":
		array = data.split('>')
		data = ' '
		for info in array:
			if '.' in info:
				temp = info.split('.')
				data += '<' + temp[0] + " class='" + temp[1] + "'>\n"
			else:
				data += '<' + info + '>\n'
		for info in reversed(array):
			if '.' in info:
				temp = info.split('.')
				data += '</' + temp[0] + '>\n'
			else:
				data += '</' + info + '>\n'
    
	print(f'changed to: {data}')
	pyperclip.copy(data)
	paste_text()
	print(f'pasted: {data}')
	print(f'{modification} done')

def help_function():
	pyperclip.copy(' *Instead of printing this message, the function called emergency')
	paste_text()
	
def replace(old, new):
	pyperclip.copy(new)
	delete(old)
	paste_text()

combinations = {

	'lower': Combo(['alt'], 'l', modifyText, modification="lower"), 
	'upper': Combo(['alt'], 'u', modifyText, modification="upper"),
	'capitalize': Combo(['alt'], 'c', modifyText, modification="capitalize"),
	'reverse': Combo(['alt'],']', modifyText, modification="reverse"),
	'eval': Combo(['alt'], '/', modifyText, modification="eval"),
	'html': Combo(['alt'], '[', modifyText, modification="html"),
	'same': Combo(['alt'], 'd', modifyText, modification="same_line")
}

keywords = {

    'keyword_1': KeyWord('-sig', replace, '-sig', 'Kind Regards,\nSarthak \nMentor of Change'),
    'keyword_3': KeyWord('-toprincipal', replace, '-toprincipal', 'To\nThe Principal\nCCET\nSector 26\nDated 26 Jan, 2020\nRespected Sir,\n')

}

keyboard_listener = KeyboardListener(combinations=combinations, keywords=keywords)
keyboard_listener.run()
