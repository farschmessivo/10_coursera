import requests
import argparse
from lxml import etree
from bs4 import BeautifulSoup
from openpyxl import Workbook


def create_parser():
    parser = argparse.ArgumentParser(
        description='Module get courses info.')
    parser.add_argument(
        '-am', '--amount', default=3, type=int,
        help='How many courses check for info.')
    parser.add_argument(
        '-out', '--output', default='courses_info.xlsx',
        help='Where to put the file.')
    return parser

#fetch_page
def fetch_the_page(url):
    url = 'https://www.coursera.org/sitemap~www~courses.xml'
    response = requests.get(url).content
    xml_tree = etree.fromstring(response)
    return xml_tree

#parse_courses_list
def parse_courses_page(xml_tree, amount):
    url_list = []
    for url in xml_tree.getchildren():
        for loc in url.getchildren():
            url_list.append(loc.text)
    print(url_list[:amount])
    return url_list[:amount]


#def get_courses_pages_list(courses_url_list):
#    return [requests.get(courses_url).text for courses_url in courses_url_list]


def get_course_info(page):
    course_info = {}
    page = requests.get(page).text                  ######################
    soup = BeautifulSoup(page, 'lxml')

    course_info['course_name'] = soup.find(
        'h1', attrs={'class': 'title display-3-text'}).get_text()
    course_info['language'] = soup.find(
        'div', attrs={'class': 'rc-Language'}).get_text()
    course_info['startdate'] = soup.find(
        'div', attrs={'class': 'startdate'}).get_text()
    course_info['amount_weeks'] = len(soup.find_all(
        'div', attrs={'class': 'week-heading'}))
    try:
        course_info['rating'] = soup.find(
            'div',
            attrs={'class': 'ratings-text'}
        ).get_text()
    except AttributeError:
        course_info['rating'] = 'No Data'

    return course_info


def output_courses_info_to_xlsx(courses_info):
    wb = Workbook()
    sheet = wb.active
    sheet.title = 'Coursera'
    head_table = [
        'Course Name',
        'Language',
        'Start Date',
        'Duration (weeks)',
        'Rating'
    ]
    ws.append(head_table)
    for course in courses_info:
        ws.append([
            course['course_name'],
            course['language'],
            course['startdate'],
            course['amount_weeks'],
            course['rating']
        ])
    return wb


def save_courses_info_to_xlsx(dest_filename, wb):
    wb.save(dest_filename)


if __name__ == '__main__':
    url = 'https://www.coursera.org/sitemap~www~courses.xml'
    courses_info_list = []
    parser = create_parser()
    namespace = parser.parse_args()
    dest_filename = namespace.output
    amount = namespace.amount
    etree_object = fetch_the_page(url)
    course_pages = parse_courses_page(etree_object, amount)

    for page in course_pages:
        course_page = fetch_the_page(page)
        course_info = get_course_info(course_page)
        course_info['url'] = url
        courses_info_list.append(output_courses_info_to_xlsx)
    save_courses_info_to_xlsx(dest_filename, wb)