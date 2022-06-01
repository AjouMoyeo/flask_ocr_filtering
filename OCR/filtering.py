import string
import argparse
from curse_detector import CurseDetector

def filtering(opt):
    curse = CurseDetector()
    result = curse.predict(opt.text)
    if(result[0] > 0.5):
        print(result[1])
        with open('filtering_result.txt', 'w', encoding='utf-8') as f:
            f.write("0")
        #return '0'
    else:
        print(result[1])
        with open('filtering_result.txt', 'w', encoding='utf-8') as f:
            f.write("1")
        #return '1'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', required=True, help='text for filtering')
    opt = parser.parse_args()
    filtering(opt)
