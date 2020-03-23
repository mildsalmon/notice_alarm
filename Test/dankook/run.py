# def run():
import sys
from module.halla import *
from module.dankook import *

univ_name = {'한라': 'halla',
             '단국': 'dankook',
             'test': 'test'}
notice_type = {'일반': 'normal',
               '학사': 'academic',
               '죽전': 'jukjeon',
               '천안': 'cheonan',
               '공통': 'common'}

def start():
    dankook('dankook', 'cheonan')
    dankook('dankook', 'common')

def test(input_univ_name, input_notice_type):
    if input_univ_name == univ_name['test']:
        if input_notice_type == notice_type['일반']:
            Halla(re_notice_type=notice_type['일반'], re_univ_name="test")
        elif input_notice_type == notice_type['학사']:
            Halla(re_notice_type=notice_type['학사'], re_univ_name="test")
        elif input_notice_type == notice_type['죽전']:
            Dankook(re_notice_type=notice_type['죽전'], re_univ_name="test")
        elif input_notice_type == notice_type['천안']:
            Dankook(re_notice_type=notice_type['천안'], re_univ_name="test")
        elif input_notice_type == notice_type['공통']:
            Dankook(re_notice_type=notice_type['공통'], re_univ_name="test")


def halla(input_univ_name, input_notice_type):
    if input_univ_name == univ_name['한라']:
        if input_notice_type == notice_type['일반']:
            Halla(re_notice_type=notice_type['일반'])
        elif input_notice_type == notice_type['학사']:
            Halla(re_notice_type=notice_type['일반'])

def dankook(input_univ_name, input_notice_type):
    if input_univ_name == univ_name['단국']:
        if input_notice_type == notice_type['죽전']:
            Dankook(re_notice_type=notice_type['죽전'])
        elif input_notice_type == notice_type['천안']:
            Dankook(re_notice_type=notice_type['천안'])
        elif input_notice_type == notice_type['공통']:
            Dankook(re_notice_type=notice_type['공통'])

if __name__ == "__main__":
    start()