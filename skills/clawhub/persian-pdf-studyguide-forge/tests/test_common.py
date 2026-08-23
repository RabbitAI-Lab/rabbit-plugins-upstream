import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from common import (normalize_persian,search_normalize,extract_json,
                    coerce_ref,coerce_answer,is_bare_answer,strip_option_prefix)

def test_persian_letters_digits_and_zwnj():
    out=normalize_persian('كتاب 123 ي\u200cك')
    assert out=='کتاب ۱۲۳ ی\u200cک'

def test_bidi_removed():
    assert '\u202b' not in normalize_persian('\u202bمتن\u202c')

def test_search_digit_equivalence():
    assert search_normalize('صفحه ۱۲۳')==search_normalize('صفحه 123')

def test_json_fence():
    assert extract_json('```json\n[{"page":1}]\n```')[0]['page']==1

def test_coerce_ref_persian_string():
    assert coerce_ref('صفحهٔ ۳',1,10)==3
    assert coerce_ref('5',1,10)==5

def test_coerce_ref_clamps_and_falls_back():
    assert coerce_ref(99,1,10)==10
    assert coerce_ref(0,1,10)==1
    assert coerce_ref('بدون عدد',1,10)==1

def test_coerce_answer_persian_labels():
    assert coerce_answer('الف')=='A'
    assert coerce_answer('ج')=='C'
    assert coerce_answer('۲')=='B'
    assert coerce_answer('b')=='B'
    assert coerce_answer('')==''

def test_is_bare_answer():
    assert is_bare_answer('A') is True
    assert is_bare_answer('') is True
    assert is_bare_answer('ورزش') is False

def test_strip_option_prefix():
    assert strip_option_prefix('الف) مرحله دیوار')=='مرحله دیوار'
    assert strip_option_prefix('A) hello')=='hello'
