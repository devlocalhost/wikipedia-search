import wikipedia
import os
import time
import sys
from time import sleep

def kill():
	sleep(0.4)
	sys.exit()
	
def search():
	while True:
		sleep(0.4)
	
		searchF = input('[Search] Search for something, or type ,exit, to go back to the menu\n// ')
	
		if searchF == ',exit,':
			sleep(0.4)
			os.system('clear')
			main()
	
		elif searchF != '':
			sleep(0.4)
		
			srch = (wikipedia.search(searchF))
			sleep(0.4)
			print('Heres what i found: ' + ', '.join(srch))
			
			sleep(0.4)
			askC = input('Would you like to get the content (summary) from one of those results? (y, n)\n// ')
			
			if askC == 'y':
				sleep(0.4)
				content()
				
			elif askC == 'n':
				sleep(0.4)
				os.system('clear')
				pass
		
		elif searchF == '':
			sleep(0.4)
			print('Input cannot be none/empty!')
			sleep(1)
			os.system('clear')
			search()
			
def content():
	while True:
		sleep(0.4)
		
		searchC = input('[Summary] Search for something, or type ,exit, to go back to the menu\n// ')
		
		if searchC == ',exit,':
			sleep(0.4)
			os.system('clear')
			main()
			
		elif searchC != '':
			sleep(0.4)
			srch = (wikipedia.summary(searchC))
			sleep(0.4)
			print(f'Heres what i found, \n{srch}')
			
		elif searchC == '':
			sleep(0.4)
			print('Input cannot be none/empty!')
			sleep(1)
			os.system('clear')
			content()
	
def main():
	sleep(0.4)
	askF = input('[Main] Type search to search about something, summary to get the content about something, or ,exit, to exit the program\n// ')
	
	if askF == 'search':
		sleep(0.4)
		os.system('clear')
		search()
		
	elif askF == 'summary':
		sleep(0.4)
		os.system('clear')
		content()
		
	elif askF == ',exit,':
		sleep(0.4)
		kill()
		
	else:
		sleep(0.4)
		print(f'Invalid input "{askF}", try again')
		sleep(1)
		os.system('clear')
		main()
	
def menu():
	sleep(0.4)
	ask = input('[Menu] Press enter to continue, or e to exit\n// ')
	
	if ask == '':
		sleep(0.4)
		os.system('clear')
		main()
		
	elif ask == 'e':
		sleep(0.5)
		os.system('clear')
		kill()
		
	else:
		print(f'Invalid input "{ask}", try again')
		sleep(1)
		os.system('clear')
		menu()

menu()