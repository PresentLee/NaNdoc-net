import unittest
import functools
import text_processing

test_sheet_is_hangul = [
    {'args': '파', 'return': True}, {'args': '이', 'return': True}, {'args': '썬', 'return': True}, {'args': '에', 'return': True},
    {'args': '서', 'return': True}, {'args': '한', 'return': True}, {'args': '글', 'return': True}, {'args': '인', 'return': True},
    {'args': '지', 'return': True}, {'args': '영', 'return': True}, {'args': '어', 'return': True}, {'args': '인', 'return': True},
    {'args': '지', 'return': True}, {'args': '구', 'return': True}, {'args': '분', 'return': True}, {'args': '한', 'return': True},
    {'args': '다', 'return': True}, {'args': '여', 'return': True}, {'args': '러', 'return': True}, {'args': '가', 'return': True},
    {'args': '지', 'return': True}, {'args': '방', 'return': True}, {'args': '법', 'return': True}, {'args': '을', 'return': True},
    {'args': '테', 'return': True}, {'args': '스', 'return': True}, {'args': '트', 'return': True}, {'args': '함', 'return': True},
    {'args': 'a', 'return': False}, {'args': 'b', 'return': False}, {'args': 'c', 'return': False}, {'args': 'd', 'return': False},
    {'args': 'e', 'return': False}, {'args': 'f', 'return': False}, {'args': 'g', 'return': False}, {'args': 'h', 'return': False},
    {'args': 'i', 'return': False}, {'args': 'j', 'return': False}, {'args': 'k', 'return': False}, {'args': 'l', 'return': False},
    {'args': 'm', 'return': False}, {'args': 'n', 'return': False}, {'args': 'o', 'return': False}, {'args': 'p', 'return': False},
    {'args': 'q', 'return': False}, {'args': 'r', 'return': False}, {'args': 's', 'return': False}, {'args': 't', 'return': False},
    {'args': 'u', 'return': False}, {'args': 'v', 'return': False}, {'args': 'w', 'return': False}, {'args': 'x', 'return': False},
    {'args': 'y', 'return': False}, {'args': 'z', 'return': False}, {'args': 'A', 'return': False}, {'args': 'B', 'return': False},
    {'args': 'C', 'return': False}, {'args': 'D', 'return': False}, {'args': 'E', 'return': False}, {'args': 'F', 'return': False},
    {'args': 'G', 'return': False}, {'args': 'H', 'return': False}, {'args': 'I', 'return': False}, {'args': 'J', 'return': False},
    {'args': 'K', 'return': False}, {'args': 'L', 'return': False}, {'args': 'M', 'return': False}, {'args': 'N', 'return': False},
    {'args': 'O', 'return': False}, {'args': 'P', 'return': False}, {'args': 'Q', 'return': False}, {'args': 'R', 'return': False},
    {'args': 'S', 'return': False}, {'args': 'T', 'return': False}, {'args': 'U', 'return': False}, {'args': 'V', 'return': False},
    {'args': 'W', 'return': False}, {'args': 'X', 'return': False}, {'args': 'Y', 'return': False}, {'args': 'Z', 'return': False},
    {'args': '!', 'return': False}, {'args': '@', 'return': False}, {'args': '#', 'return': False}, {'args': '$', 'return': False},
    {'args': '%', 'return': False}, {'args': '^', 'return': False}, {'args': '&', 'return': False}, {'args': '*', 'return': False},
    {'args': '(', 'return': False}, {'args': ')', 'return': False}, {'args': '-', 'return': False}, {'args': '_', 'return': False},
    {'args': '=', 'return': False}, {'args': '+', 'return': False}, {'args': '[', 'return': False}, {'args': ']', 'return': False},
    {'args': '{', 'return': False}, {'args': '}', 'return': False}, {'args': '\\', 'return': False}, {'args': '|', 'return': False},
    {'args': ':', 'return': False}, {'args': ';', 'return': False}, {'args': "'", 'return': False}, {'args': '"', 'return': False},
    {'args': ',', 'return': False}, {'args': '.', 'return': False}, {'args': '<', 'return': False}, {'args': '>', 'return': False},
    {'args': '/', 'return': False}, {'args': '?', 'return': False}
]

test_sheet_token_to_num = [
    {'args': '<sos>', 'return': [0]}, {'args': '<pad>', 'return': [1]}, {'args': '<eos>', 'return': [2]},
    {'args': 'ㄱ', 'return':  [3]}, {'args': 'ㄲ', 'return':  [4]}, {'args': 'ㄴ', 'return':  [5]}, {'args': 'ㄷ', 'return':  [6]},
    {'args': 'ㄸ', 'return':  [7]}, {'args': 'ㄹ', 'return':  [8]}, {'args': 'ㅁ', 'return':  [9]}, {'args': 'ㅂ', 'return': [10]},
    {'args': 'ㅃ', 'return': [11]}, {'args': 'ㅅ', 'return': [12]}, {'args': 'ㅆ', 'return': [13]}, {'args': 'ㅇ', 'return': [14]},
    {'args': 'ㅈ', 'return': [15]}, {'args': 'ㅉ', 'return': [16]}, {'args': 'ㅊ', 'return': [17]}, {'args': 'ㅋ', 'return': [18]},
    {'args': 'ㅌ', 'return': [19]}, {'args': 'ㅍ', 'return': [20]}, {'args': 'ㅎ', 'return': [21]},
    {'args': 'ㅏ', 'return': [22]}, {'args': 'ㅐ', 'return': [23]}, {'args': 'ㅑ', 'return': [24]}, {'args': 'ㅒ', 'return': [25]},
    {'args': 'ㅓ', 'return': [26]}, {'args': 'ㅔ', 'return': [27]}, {'args': 'ㅕ', 'return': [28]}, {'args': 'ㅖ', 'return': [29]},
    {'args': 'ㅗ', 'return': [30]}, {'args': 'ㅘ', 'return': [31]}, {'args': 'ㅙ', 'return': [32]}, {'args': 'ㅚ', 'return': [33]},
    {'args': 'ㅛ', 'return': [34]}, {'args': 'ㅜ', 'return': [35]}, {'args': 'ㅝ', 'return': [36]}, {'args': 'ㅞ', 'return': [37]},
    {'args': 'ㅟ', 'return': [38]}, {'args': 'ㅠ', 'return': [39]}, {'args': 'ㅡ', 'return': [40]}, {'args': 'ㅢ', 'return': [41]},
    {'args': 'ㅣ', 'return': [42]},
    {'args': 'ㄳ', 'return': [45]}, {'args': 'ㄵ', 'return': [47]}, {'args': 'ㄶ', 'return': [48]}, {'args': 'ㄺ', 'return': [51]},
    {'args': 'ㄻ', 'return': [52]}, {'args': 'ㄼ', 'return': [53]}, {'args': 'ㄽ', 'return': [54]}, {'args': 'ㄾ', 'return': [55]},
    {'args': 'ㄿ', 'return': [56]}, {'args': 'ㅀ', 'return': [57]}, {'args': 'ㅄ', 'return': [60]},
    {'args': 'a', 'return': [70]}, {'args': 'b', 'return': [71]}, {'args': 'c', 'return': [72]}, {'args': 'd', 'return': [73]},
    {'args': 'e', 'return': [74]}, {'args': 'f', 'return': [75]}, {'args': 'g', 'return': [76]}, {'args': 'h', 'return': [77]},
    {'args': 'i', 'return': [78]}, {'args': 'j', 'return': [79]}, {'args': 'k', 'return': [80]}, {'args': 'l', 'return': [81]},
    {'args': 'm', 'return': [82]}, {'args': 'n', 'return': [83]}, {'args': 'o', 'return': [84]}, {'args': 'p', 'return': [85]},
    {'args': 'q', 'return': [86]}, {'args': 'r', 'return': [87]}, {'args': 's', 'return': [88]}, {'args': 't', 'return': [89]},
    {'args': 'u', 'return': [90]}, {'args': 'v', 'return': [91]}, {'args': 'w', 'return': [92]}, {'args': 'x', 'return': [93]},
    {'args': 'y', 'return': [94]}, {'args': 'z', 'return': [95]},
    {'args': 'A', 'return':  [96]}, {'args': 'B', 'return':  [97]}, {'args': 'C', 'return':  [98]}, {'args': 'D', 'return':  [99]},
    {'args': 'E', 'return': [100]}, {'args': 'F', 'return': [101]}, {'args': 'G', 'return': [102]}, {'args': 'H', 'return': [103]},
    {'args': 'I', 'return': [104]}, {'args': 'J', 'return': [105]}, {'args': 'K', 'return': [106]}, {'args': 'L', 'return': [107]},
    {'args': 'M', 'return': [108]}, {'args': 'N', 'return': [109]}, {'args': 'O', 'return': [110]}, {'args': 'P', 'return': [111]},
    {'args': 'Q', 'return': [112]}, {'args': 'R', 'return': [113]}, {'args': 'S', 'return': [114]}, {'args': 'T', 'return': [115]},
    {'args': 'U', 'return': [116]}, {'args': 'V', 'return': [117]}, {'args': 'W', 'return': [118]}, {'args': 'X', 'return': [119]},
    {'args': 'Y', 'return': [120]}, {'args': 'Z', 'return': [121]},
    {'args': '0', 'return': [122]}, {'args': '1', 'return': [123]}, {'args': '2', 'return': [124]}, {'args': '3', 'return': [125]},
    {'args': '4', 'return': [126]}, {'args': '5', 'return': [127]}, {'args': '6', 'return': [128]}, {'args': '7', 'return': [129]},
    {'args': '8', 'return': [130]}, {'args': '9', 'return': [131]},
    {'args': '!', 'return': [132]}, {'args': '@', 'return': [133]}, {'args': '#', 'return': [134]}, {'args': '$', 'return': [135]},
    {'args': '%', 'return': [136]}, {'args': '^', 'return': [137]}, {'args': '&', 'return': [138]}, {'args': '*', 'return': [139]},
    {'args': '(', 'return': [140]}, {'args': ')', 'return': [141]}, {'args': '-', 'return': [142]}, {'args': '_', 'return': [143]},
    {'args': '=', 'return': [144]}, {'args': '+', 'return': [145]}, {'args': '[', 'return': [146]}, {'args': ']', 'return': [147]},
    {'args': '{', 'return': [148]}, {'args': '}', 'return': [149]}, {'args': '\\', 'return': [150]}, {'args': '|', 'return': [151]},
    {'args': ':', 'return': [150]}, {'args': ';', 'return': [151]}, {'args': "'", 'return': [152]}, {'args': '"', 'return': [153]},
    {'args': ',', 'return': [154]}, {'args': '.', 'return': [155]}, {'args': '<', 'return': [156]}, {'args': '>', 'return': [157]},
    {'args': '/', 'return': [158]}, {'args': '?', 'return': [159]}, {'args': ' ', 'return': [160]},
    {'args': '파', 'return': [20, 22]}, {'args': '이', 'return': [14, 42]}, {'args': '썬', 'return': [13, 26, 46]}, {'args': '에', 'return': [14, 27]},
    {'args': '서', 'return': [12, 26]}, {'args': '한', 'return': [21, 22, 46]}, {'args': '글', 'return': [3, 40, 50]}, {'args': '인', 'return': [14, 42, 46]},
    {'args': '지', 'return': [15, 42]}, {'args': '영', 'return': [14, 28, 63]}, {'args': '어', 'return': [14, 26]}, {'args': '잘', 'return': [15, 22, 50]},
    {'args': '엣', 'return': [14, 27, 61]}, {'args': '구', 'return': [3, 35]}, {'args': '분', 'return': [10, 35, 46]}, {'args': '명', 'return': [9, 28, 63]},
    {'args': '다', 'return': [6, 22]}, {'args': '여', 'return': [14, 28]}, {'args': '러', 'return': [8, 26]}, {'args': '가', 'return': [3, 22]},
    {'args': '왈', 'return': [14, 31, 50]}, {'args': '방', 'return': [10, 22, 63]}, {'args': '법', 'return': [10, 26, 59]}, {'args': '을', 'return': [14, 40, 50]},
    {'args': '테', 'return': [19, 27]}, {'args': '스', 'return': [12, 40]}, {'args': '트', 'return': [19, 40]}, {'args': '함', 'return': [21, 22, 58]},
]

test_sheet_tokenize_text = [
    {
        'args': '이제 seq2seq를 이용해서 기계 번역기를 만들어보도록 하겠습니다.',
        'return': ['<sos>','이','제',' ','s','e','q','2','s','e','q','를',' ','이','용','해','서',' ','기','계',' ','번','역','기',
                   '를',' ','만','들','어','보','도','록',' ','하','겠','습','니','다','.','<eos>']
    },
    {
        'args': '병렬 데이터라고 하면 앞서 수행한 태깅 작업의 데이터를 생각할 수 있지만,',
        'return': ['<sos>','병','렬',' ','데','이','터','라','고',' ','하','면',' ','앞','서',' ','수','행','한',' ','태',
                   '깅',' ','작','업','의',' ','데','이','터','를',' ','생','각','할',' ','수',' ','있','지','만',',','<eos>']
    },
    {
        'args': 'tar는 target의 줄임말로 번역하고자 하는 문장을 나타냅니다.',
        'return': ['<sos>','t','a','r','는',' ','t','a','r','g','e','t','의',' ','줄','임','말','로',' ','번','역',
                   '하','고','자',' ','하','는',' ','문','장','을',' ','나','타','냅','니','다','.','<eos>']
    },
]
test_sheet_text_to_nums = [
    {
        'args': '이제 seq2seq를 이용해서 기계 번역기를 만들어보도록 하겠습니다.',
        'return': [0, 14,42, 15,27, 160, 88, 74, 86, 124, 88, 74, 86, 8,40,50, 160, 14,42, 14,34,63, 21,23, 12,26, 160, 3,42, 3,29, 160,
                   10,26,46, 14,28,43, 3,42, 8,40,50, 160, 9,22,46, 6,40,50, 14,26, 10,30, 6,30, 8,30,43, 160, 21,22, 3,27,62, 12,40,59,
                   5,42, 6,22, 155, 2]
    },
    {
        'args': '병렬 데이터라고 하면 앞서 수행한 태깅 작업의 데이터를 생각할 수 있지만,',
        'return': [0, 10,28,63, 8,28,50, 160, 6,27, 14,42, 19,26, 8,22, 3,30, 160, 21,22, 9,28,46, 160, 14,22,68, 12,26, 160, 12,35,
                   21,23,63, 21,22,46, 160, 19,23, 3,42,63, 160, 15,22,43, 14,26,59, 14,41, 160, 6,27, 14,42, 19,26, 8,40,50, 160,
                   12,23,63, 3,22,43, 21,22,50, 160, 12,35, 160, 14,42,62, 15,42, 9,22,46, 154, 2]
    },
    {
        'args': 'tar는 target의 줄임말로 번역하고자 하는 문장을 나타냅니다.',
        'return': [0, 89, 70, 87, 5,40,46, 160, 89, 70, 87, 76, 74, 89, 14,41, 160, 15,35,50, 14,42,58, 9,22,50, 8,30, 160, 10,26,46, 14,28,
                   43, 21,22, 3,30, 15,22, 160, 21,22, 5,40,46, 160, 9,35,46, 15,22,63, 14,40,50, 160, 5,22, 19,22, 5,23,59, 5,42, 6,22,
                   155, 2]
    },
]

class TextProcessing(unittest.TestCase):

    def test_token_to_num(self):
        for test_item in test_sheet_token_to_num:
            args = test_item['args']
            truth = test_item['return']
            ret = text_processing.token_to_num(args)
            self.assertTrue(functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, truth, ret), True), f'test_sheet: {args}:{truth}, function return: {ret}')

    def test_isHangul(self):
        for test_item in test_sheet_is_hangul:
            args = test_item['args']
            truth = test_item['return']
            ret = text_processing.isHangul(args)
            self.assertEqual(truth,ret)

    def test_tokenize_text(self):
        for test_item in test_sheet_tokenize_text:
            args = test_item['args']
            truth = test_item['return']
            ret = text_processing.tokenize_text(args)
            self.assertTrue(functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, truth, ret), True), f'test_sheet: {args}:{truth}, function return: {ret}')

    def test_text_to_nums(self):
        for test_item in test_sheet_text_to_nums:
            args = test_item['args']
            truth = test_item['return']
            ret = text_processing.text_to_nums(args)
            self.assertTrue(functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, truth, ret), True), f'test_sheet: {args}:{truth}, function return: {ret}')

if __name__ == '__main__':
    unittest.main()