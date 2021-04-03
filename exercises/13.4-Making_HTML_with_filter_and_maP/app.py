all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def generate_li(arr):
    tagLi = ""
    for color in arr:
        tagLi += "<li>" + color["label"] + "</li>"

    return tagLi 



def filter_colors(color):
    return color['sexy']== True


sexyColorList = list(filter(filter_colors, all_colors))
liList = generate_li(sexyColorList)


print(liList)