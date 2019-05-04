import webbrowser

values = {"Tide+Pods","Mercedes+Benz","Apple+Watch","Dell+Computer","Bose+Headphones","Stride+Gum","Colt+AR15","American+Spirits","Sunglasses","Condoms","Colorado+Springs+Roofing"}

for var in values:
	for i in range(0,50):
		webbrowser.open('https://www.google.com/search?q='+var,2)

