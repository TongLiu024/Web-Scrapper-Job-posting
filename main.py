from bs4 import BeautifulSoup

with open("sampleWebPage.html", 'r') as html_file:
    content = html_file.read()
    # lxml package is a parser for html file content
    soup = BeautifulSoup(content, "lxml")

    # prettify() will format the html file
    # print(soup.prettify())
    course_html_tags = soup.find_all("div", class_="card")

    for course in course_html_tags:
        course_price = course.a.text.split()[-1]
        course_name = course.h5.text

        print(f'{course_name} costs {course_price} to purchase')
