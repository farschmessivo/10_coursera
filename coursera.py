import requests
import argparse
from lxml import etree
from bs4 import BeautifulSoup
from openpyxl import Workbook


def create_parser():
    parser = argparse.ArgumentParser(
        description='Module get courses info.')
    parser.add_argument(
        '-am', '--amount', default=5, type=int,
        help='How many courses check for info.')
    parser.add_argument(
        '-out', '--output', default='courses_info.xlsx',
        help='Where to put the file.')
    return parser


def fetch_the_xml_tree(url):
    content = requests.get(url).content
    xml_tree = etree.fromstring(content)
    return xml_tree


def get_courses_list(xml_tree, amount):
    url_list = []
    for url in xml_tree.getchildren():
        for loc in url.getchildren():
            url_list.append(loc.text)
    return url_list[:amount]


def get_course_info(page):
    course_info = {}
    soup = BeautifulSoup(page, 'html.parser')

    course_info['course_name'] = soup.find(
        'h1', attrs={'class': 'title display-3-text'}
    ).get_text()
    course_info['language'] = soup.find(
        'div', attrs={'class': 'rc-Language'}
    ).get_text()
    course_info['startdate'] = soup.find(
        'div', attrs={'class': 'startdate'}
    ).get_text()
    course_info['amount_weeks'] = len(soup.find_all(
        'div', attrs={'class': 'week-heading'}
    ))
    try:
        course_info['rating'] = soup.find(
            'div',
            attrs={'class': 'ratings-text'}
        ).get_text()
    except AttributeError:
        course_info['rating'] = None

    return course_info


def output_courses_info_to_xlsx(courses_info):
    wb = Workbook()
    sheet = wb.active
    sheet.title = 'Coursera'
    head_table = [
        'Course Name',
        'Language',
        'Start Date',
        'Duration (in weeks)',
        'Rating'
    ]
    sheet.append(head_table)
    for course in courses_info:
        sheet.append([
            course['course_name'],
            course['language'],
            course['startdate'],
            course['amount_weeks'],
            course['rating'] or "No data"
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
    etree_object = fetch_the_xml_tree(url)
    course_pages = get_courses_list(etree_object, amount)

    for page in course_pages:
        course_page = requests.get(page).text
        course_info = get_course_info(course_page)
        courses_info_list.append(course_info)
    save_courses_info_to_xlsx(
        dest_filename,
        output_courses_info_to_xlsx(courses_info_list)
    )
    print('The courses dump is saved to the {}'.format(dest_filename)
          )
