import bs4 as bs

with open('data.html') as file:
    data = file.read().rstrip()

soup = bs.BeautifulSoup(data, 'lxml')

courses = soup.findAll('div', class_="product product-detail")

for course in courses:
    if course.find('div', class_='course-details-credits'):
        course_credits = course.find('div', class_='course-details-credits').p.get_text().split(': ')[1]
    else:
        continue
    course_title = course.find('div', class_='course-details-title').h2.a['title']
    course_price = course.find('span', class_='sales').span['content']
    ppc = float(course_price) / int(course_credits)
    print(f'{course_title},{course_price},{course_credits},${ppc:.2f}')