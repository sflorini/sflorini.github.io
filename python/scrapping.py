domain = "http://walshbr.com/"

pages = ["about" , "blog" , "pedagogy" , "projects" , "cv"]

new_list = []

for page in pages:
    new_list.append(domain + page)

print(new_list )
