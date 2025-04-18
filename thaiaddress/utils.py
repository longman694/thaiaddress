import re
from itertools import groupby
from typing import List, Tuple, Union, Optional
import numpy as np
import deepcut
from pythainlp.util import isthai
from pythainlp.corpus import thai_stopwords


def remove_emoji(text: str) -> str:
    """
    Remove emojis from a given text
    """
    regrex_pattern = re.compile(
        pattern="["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "]+",
        flags=re.UNICODE,
    )
    return regrex_pattern.sub(r"", text)


def preprocess(text: str) -> str:
    """
    Generalized function to preprocess an input
    """
    text = text.strip()
    text = text.replace("ส่ง ", "")
    text = text.replace("จัดส่ง", "")
    text = text.replace("ชือ.", "")
    text = text.replace("ชื่อ ", "")
    text = text.replace("ผู้รับ", "")
    text = text.replace("ส่งที่ ", " ")
    text = text.replace("ที่อยู่ ", " ")
    text = text.replace("ที้อยุ่ ", " ")
    text = text.replace("ที่อยู่จ้า ", " ")
    text = text.replace("ส่งของที่ ", " ")
    text = text.replace("ส่งมาที่", " ")
    text = text.replace("\n-", " ")
    text = text.replace("\n", " ")
    text = text.replace(": ", " ")
    text = text.replace("(", "")
    text = text.replace(")", "")
    text = text.replace('"', "")
    text = remove_emoji(text)
    text = " ".join([t for t in text.strip().split(" ") if t.strip() != ""])
    return text


def clean_location_text(text: str) -> str:
    """
    Clean location before using fuzzy string match
    """
    text = text.replace("แขวง", " ")
    text = text.replace("เขต", " ")
    text = text.replace("อำเภอ", " ")
    text = text.replace("ตำบล", " ")
    text = text.replace("ต.", " ")
    text = text.replace("ตฺ", "ต.")
    text = text.replace("อ.", " ")
    text = text.replace("จ.", " ")
    text = text.replace("คอหงส์", "คอหงษ์")
    text = text.replace("กทม.", "กรุงเทพมหานคร")
    text = text.replace("กทม", "กรุงเทพมหานคร")
    return text


def get_digit(text: str) -> str:
    """
    Get digit output from a given text
    """
    return "".join([c for c in text if c.isdigit()])


def is_stopword(word: str) -> bool:  # เช็คว่าเป็นคำฟุ่มเฟือย
    """
    Check if a word is stop word or not using PyThaiNLP

    Reference
    ----------
    Pythainlp, https://github.com/PyThaiNLP/pythainlp
    """
    return word in thai_stopwords()


def range_intersect(r1: range, r2: range) -> Optional[range]:
    """
    Check if range is intersected

    References
    ----------
    Stack Overflow, https://stackoverflow.com/questions/6821156/how-to-find-range-overlap-in-python
    """
    return range(max(r1.start, r2.start), min(r1.stop, r2.stop)) or None


def merge_labels(preds: list) -> Tuple[List[Tuple[int, int]], List[str]]:
    """
    Get merged labels and merge tuple to merge tokens
    """
    preds = list(np.ravel(preds))
    merge, labels = [], []
    s = 0
    for label, g in groupby(preds):
        g = list(g)
        labels.append(label)
        if len(g) > 1:
            merge.append((s, s + len(g)))
        s += len(g)
    return merge, labels


def merge_tokens(tokens: List[str], merge: List[Tuple[int, int]]) -> List[str]:
    """
    Merge tokens with an input merge

    References
    ----------
    Stack Overflow, https://stackoverflow.com/questions/43550219/merge-elements-in-list-based-on-given-indices
    """
    for t in merge[::-1]:
        merged = "".join(tokens[t[0] : t[1]])  # merging values within a range
        tokens[t[0] : t[1]] = [merged]  # slice replacement
    return tokens
