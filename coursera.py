import requests
import argparse
from lxml import etree
from bs4 import BeautifulSoup
from openpyxl import Workbook
from collections import namedtuple


def create_parser():
    parser = argparse.ArgumentParser(
        description='Module get courses info.')
    parser.add_argument(
        '-am', '--amount', default=20, type=int,
        help='How many courses check for info.')
    parser.add_argument(
        '-out', '--output', default='courses_info.xlsx',
        help='Where to put the file.')
    return parser


def get_courses_url_list(amount):
    url = 'https://www.coursera.org/sitemap~www~courses.xml'
    response = requests.get(url).content
    root = etree.fromstring(response)
    url_list = []
    for url in root.getchildren():
        for loc in url.getchildren():
            url_list.append(loc.text)
    return url_list[:amount]


def get_courses_pages_list(courses_url_list):
    return [requests.get(courses_url).text for courses_url in courses_url_list]


def get_course_info(course_page):
    course = namedtuple('course', [
        'Course_name',
        'Grade',
        'Language',
        'Start_date',
        'Amount_week',
    ])

    for page in course_page:
        soup = BeautifulSoup(page, "lxml")

        grade = getattr(soup.find(
            "div", class_="ratings-text"), 'text', '0 stars')
        course_name = getattr(soup.find(
            "h1", class_="title display-3-text"), 'text', 'No data')
        startdate = getattr(soup.find(
            "div", class_="startdate"), 'text', 'No data')
        language = soup.find(
            "div", class_="rc-Language").findAllNext(text=True)[1]
        amount_week = len(soup.find_all(
            "div", class_="week-heading"))

        courses_tuple = course(Course_name=course_name,
                               Grade=grade,
                               Language=language,
                               Start_date=startdate,
                               Amount_week='{} weeks'.format(amount_week))

        print(courses_tuple)
        yield courses_tuple


def output_courses_info_to_xlsx(courses_tuple):
    wb = Workbook()
    sheet = wb.active
    for row in courses_tuple:
        sheet.append(row)
    return wb


def save_courses_info_to_xlsx(dest_filename, wb):
    wb.save(dest_filename)


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    dest_filename = namespace.output
    amount = namespace.amount
    course_page = get_courses_pages_list(get_courses_url_list(amount))
    course_info = get_course_info(course_page)
    output_courses_info = output_courses_info_to_xlsx(course_info)
    save_courses_info_to_xlsx(dest_filename, output_courses_info)