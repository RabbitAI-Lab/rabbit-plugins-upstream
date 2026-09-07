#!/usr/bin/env python3
"""test_ocr_core.py — pure-logic tests for the v1.4.0 OCR engine (no tesseract
needed; runs anywhere). Use: python3 scripts/test_ocr_core.py  -> prints PASS/FAIL."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_dual_ocr import (merge_word_sets, rejoin_fragments, words_to_text,
                              repair_word, token_set, coverage, _iou)

fails = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: fails.append(name)

# repair_word: Arabic->Persian chars + digits, ZWNJ preserved
check("repair ي->ی ك->ک", repair_word("يك") == "یک")
check("repair arabic digits", repair_word("١٢٣") == "۱۲۳")
check("ZWNJ preserved", repair_word("می\u200cشود") == "می\u200cشود")

# merge: union keeps words found by any pass; votes counted; no word lost
p1 = [{"t": "خواب", "conf": 91.0, "box": (10, 10, 50, 20), "psm": 3},
      {"t": "طبیعی", "conf": 55.0, "box": (70, 10, 40, 20), "psm": 3}]
p2 = [{"t": "خواب", "conf": 94.0, "box": (11, 10, 49, 20), "psm": 6},
      {"t": "انسان", "conf": 88.0, "box": (120, 10, 45, 20), "psm": 6}]
m = merge_word_sets([p1, p2])
texts = {w["t"] for w in m}
check("merge keeps all 3 words", texts == {"خواب", "طبیعی", "انسان"})
check("merge votes/best-conf", next(w for w in m if w["t"] == "خواب")["votes"] == 2
      and next(w for w in m if w["t"] == "خواب")["conf"] == 94.0)

# RTL gap math: fragment to the LEFT of previous must rejoin (direction-agnostic)
frags = [{"t": "می\u200c", "conf": 90.0, "box": (100, 10, 20, 18), "votes": 2, "psms": {3}, "agree": True},
         {"t": "دهد", "conf": 90.0, "box": (60, 10, 36, 18), "votes": 2, "psms": {3}, "agree": True}]
rj = rejoin_fragments([dict(f) for f in frags], None)
check("RTL fragment rejoin", len(rj) == 1 and rj[0]["t"] == "می\u200cدهد")
# but distinct words with a real gap must NOT merge
words2 = [{"t": "خواب", "conf": 90.0, "box": (100, 10, 45, 18), "votes": 2, "psms": {3}, "agree": True},
          {"t": "طبیعی", "conf": 90.0, "box": (20, 10, 45, 18), "votes": 2, "psms": {3}, "agree": True}]
rj2 = rejoin_fragments([dict(f) for f in words2], None)
check("real word gap not merged", len(rj2) == 2)

# words_to_text: RTL line must come out right-to-left
line = [{"t": "دوم", "box": (10, 10, 40, 18)}, {"t": "کلمه", "box": (60, 10, 50, 18)},
        {"t": "اول", "box": (120, 10, 35, 18)}]
check("RTL line order", words_to_text(line).strip() == "اول کلمه دوم")
# LTR line stays LTR
line_l = [{"t": "first", "box": (10, 10, 40, 18)}, {"t": "second", "box": (60, 10, 50, 18)}]
check("LTR line order", words_to_text(line_l).strip() == "first second")

# coverage: missing-risk detection
_L = " ".join(f"کلمه{i}" for i in range(20))
_O = " ".join(f"کلمه{i}" for i in range(19))  # 1/20 = 5% unseen -> low
cov = coverage(1, _L, _O)
check("coverage low risk", cov["missing_risk"] == "low" and cov["logical_words"] == 20)
cov2 = coverage(2, "", "چیزی")
check("coverage image-only page", cov2["missing_risk"] == "none")

# tiny-box IoU guard
check("iou tiny identical", _iou((5, 5, 1, 1), (5, 5, 1, 1)) == 1.0)
check("iou tiny distant", _iou((5, 5, 1, 1), (99, 99, 1, 1)) == 0.0)

print(f"\n{'ALL PASS' if not fails else f'{len(fails)} FAILURES: ' + ', '.join(fails)}")
sys.exit(0 if not fails else 1)
