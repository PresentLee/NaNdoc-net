"""
Copyright : Team  Murphy-s-rule (Team Nandoc)
Writer : 윤성국(Geoff Yoon)

This module contain functions or methods to process text for label in dataset or output of model.
To generate HTML documentation for this module issue the command:

    pydoc -w util/text_processing.py

"""

from enum import Enum
import re
from jamo import h2j, j2hcj

class HangulTokenType(Enum):
    """
    tokentype
        - onset:  ㄱ | ㄲ | ㄴ | ㄷ | ㄸ | ㄹ | ㅁ | ㅂ | ㅃ | ㅅ | ㅆ | ㅇ | ㅈ | ㅉ | ㅊ | ㅋ | ㅌ | ㅍ | ㅎ
        - nucleus: ㅏ | ㅐ | ㅑ | ㅒ | ㅓ | ㅔ | ㅕ | ㅖ | ㅗ | ㅘ | ㅙ | ㅚ | ㅛ | ㅜ | ㅝ | ㅞ | ㅟ | ㅠ | ㅡ | ㅢ | ㅣ
        - coda: ㄱ | ㄲ | ㄳ | ㄴ | ㄵ | ㄶ | ㄷ | ㄹ | ㄺ | ㄻ | ㄼ | ㄽ | ㄾ | ㄿ | ㅀ | ㅁ | ㅂ | ㅄ | ㅅ | ㅆ | ㅇ | ㅈ | ㅊ | ㅋ | ㅌ | ㅍ | ㅎ
    """
    ONSET = 0
    NUCLEUS = 1
    CODA = 2

map_token_to_num = {
    '<sos>': 0, '<pad>': 1,'<eos>': 2,
    HangulTokenType.ONSET: {
        'ㄱ':  3, 'ㄲ':  4, 'ㄴ':  5, 'ㄷ':  6, 'ㄸ':  7, 'ㄹ':  8, 'ㅁ':  9, 'ㅂ': 10, 'ㅃ': 11, 'ㅅ': 12, 'ㅆ': 13,
        'ㅇ': 14, 'ㅈ': 15, 'ㅉ': 16, 'ㅊ': 17, 'ㅋ': 18, 'ㅌ': 19, 'ㅍ': 20, 'ㅎ': 21,
        'ㅏ': 22, 'ㅐ': 23, 'ㅑ': 24, 'ㅒ': 25, 'ㅓ': 26, 'ㅔ': 27, 'ㅕ': 28, 'ㅖ': 29, 'ㅗ': 30, 'ㅘ': 31, 'ㅙ': 32,
        'ㅚ': 33, 'ㅛ': 34, 'ㅜ': 35, 'ㅝ': 36, 'ㅞ': 37, 'ㅟ': 38, 'ㅠ': 39, 'ㅡ': 40, 'ㅢ': 41, 'ㅣ': 42,
        'ㄳ': 45, 'ㄵ': 47, 'ㄶ': 48, 'ㄺ': 51, 'ㄻ': 52, 'ㄼ': 53, 'ㄽ': 54, 'ㄾ': 55, 'ㄿ': 56, 'ㅀ': 57, 'ㅄ': 60},
    HangulTokenType.NUCLEUS: {
        'ㅏ': 22, 'ㅐ': 23, 'ㅑ': 24, 'ㅒ': 25, 'ㅓ': 26, 'ㅔ': 27, 'ㅕ': 28, 'ㅖ': 29, 'ㅗ': 30, 'ㅘ': 31, 'ㅙ': 32,
        'ㅚ': 33, 'ㅛ': 34, 'ㅜ': 35, 'ㅝ': 36, 'ㅞ': 37, 'ㅟ': 38, 'ㅠ': 39, 'ㅡ': 40, 'ㅢ': 41, 'ㅣ': 42},
    HangulTokenType.CODA: {
        'ㄱ': 43, 'ㄲ': 44, 'ㄳ': 45, 'ㄴ': 46, 'ㄵ': 47, 'ㄶ': 48, 'ㄷ': 49, 'ㄹ': 50, 'ㄺ': 51, 'ㄻ': 52, 'ㄼ': 53,
        'ㄽ': 54, 'ㄾ': 55, 'ㄿ': 56, 'ㅀ': 57, 'ㅁ': 58, 'ㅂ': 59, 'ㅄ': 60, 'ㅅ': 61, 'ㅆ': 62, 'ㅇ': 63, 'ㅈ': 64,
        'ㅊ': 65, 'ㅋ': 66, 'ㅌ': 67, 'ㅍ': 68, 'ㅎ': 69},
    'a': 70, 'b': 71, 'c': 72, 'd': 73, 'e': 74, 'f': 75, 'g': 76, 'h': 77, 'i': 78, 'j': 79, 'k': 80, 'l': 81, 'm': 82,
    'n': 83, 'o': 84, 'p': 85, 'q': 86, 'r': 87, 's': 88, 't': 89,
    'u': 90, 'v': 91, 'w': 92, 'x': 93, 'y': 94, 'z': 95,
    'A':  96, 'B':  97, 'C':  98, 'D':  99, 'E': 100, 'F': 101, 'G': 102, 'H': 103, 'I': 104, 'J': 105,
    'K': 106, 'L': 107, 'M': 108, 'N': 109, 'O': 110, 'P': 111, 'Q': 112, 'R': 113, 'S': 114, 'T': 115,
    'U': 116, 'V': 117, 'W': 118, 'X': 119, 'Y': 120, 'Z': 121,
    '0': 122, '1': 123, '2': 124, '3': 125, '4': 126, '5': 127, '6': 128, '7': 129, '8': 130, '9': 131,
    '!': 132, '@': 133, '#': 134, '$': 135, '%': 136, '^': 137, '&': 138, '*': 139, '(': 140, ')': 141, '-': 142,
    '_': 143, '=': 144, '+': 145, '[': 146, ']': 147, '{': 148, '}': 149, '\\': 150, '|': 151, ':': 150, ';': 151,
    "'": 152, '"': 153, ',': 154, '.': 155, '<': 156, '>': 157, '/': 158, '?': 159, ' ': 160
}

map_num_to_token = [
    '<sos>', '<pad>','<eos>',
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ' 'ㅎ',
    'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ',
    'ㅣ',
    'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ',
    'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X', 'Y', 'Z',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|', ':', ';', "'",
    '"', ',', '.', '<', '>', '/', '?', ' '
]

def isHangul(token):
    hanCount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', token))
    return hanCount > 0


def token_to_num(token):
    """
    The token_to_num function returns the number mapped by input token

    Args:
        token (str): The token will be converted to number mapped

    Returns:
        list(int): The numbers converted from input token
    """
    return [map_token_to_num[HangulTokenType(i)][sub_token] for i, sub_token in enumerate(j2hcj(h2j(token)))] \
            if isHangul(token) else [map_token_to_num[token]]

def tokenize_text(text):
    """
        The tokenize_text function returns the tokens from text, always start token is <sos>, end token is <eos>

        Args:
            text (str): The text will be tokenized

        Returns:
            list(str): The tokens from input text
    """
    return ['<sos>'] + list(text) + ['<eos>']

def text_to_nums(text):
    """
        The text_to_nums function returns the number list converted from text.
        The input text is tokenized, and after that tokens is converted to number list.

        Args:
            text (str): The text will be converted to numbers

        Returns:
            list(int): The numbers converted from tokens of text
    """
    nums = []
    for token in tokenize_text(text):
        nums.extend(token_to_num(token))

    return nums

