# def run():
import sys
from module.halla import *

univ_name = {'한라': 'halla',
             '단국': 'dankook',
             'test': 'test'}
notice_type = {'일반': 'normal',
               '학사': 'academic',
               '죽전': 'jukjeon',
               '천안': 'cheonan',
               '공통': 'common'}

def start():
    test('test', 'normal')

def test(input_univ_name, input_notice_type):
    if input_univ_name == univ_name['test']:
        if input_notice_type == notice_type['일반']:
            halla = Halla(re_notice_type=notice_type['일반'])
        elif input_notice_type == notice_type['학사']:
            pass
        if halla == False:
            sys.exit(1)

def halla(input_univ_name, input_notice_type):
    if input_univ_name == univ_name['한라']:
        if input_notice_type == notice_type['일반']:
            pass
        elif input_notice_type == notice_type['학사']:
            pass

def dankook(input_univ_name, input_notice_type):
    pass
    # if input_univ_name == univ_name['한라']:
    #     if input_notice_type == notice_type['일반']:
    #         pass
    #     elif input_notice_type == notice_type['학사']:
    #         pass
    #     if halla == False:
    #         sys.exit(1)

if __name__ == "__main__":
    start()