"""改 wise-exam / daniel-exam：扫描版从「默认三件套」改为「字体门禁不通过才出的回退产物」。
幂等可重放。
"""
import os

ROOT = '/root/.skills'
WISE = os.path.join(ROOT, 'wise-exam', 'SKILL.md')
DAN = os.path.join(ROOT, 'daniel-exam', 'SKILL.md')

WISE_OLD4 = """4. **要答案就默认出三份**（与 daniel-exam 同步，用户 2026-10-31 定）：①带答案原卷
   （`build_answer_paper.py` 或 `build_exam_pdf.py --answers`）②纯答案卷（`answers_only.py`）
   ③**扫描版参考答案**（`build_answer_paper.py` 自动调 `scripts/make_scanned.py`，**默认 300dpi**、
   **文件名以「扫描版」开头**：`扫描版_<卷名>_参考答案版_300dpi.pdf`；`--no-scan` 关闭、`--scan-dpi` 改精度）。
   三份都给，不额外出空白题卷；用户明确只要其中某几份时才裁剪。"""

WISE_NEW4 = """4. **要答案就默认出两份**（用户 2026-10-31 修订）：①带答案原卷
   （`build_answer_paper.py` 或 `build_exam_pdf.py --answers`）②纯答案卷（`answers_only.py`）。
   ⚠️ **扫描版是回退产物，不是默认项**：只有交付前字体门禁
   （`pdf-font-fixer/scripts/detect.py`）不通过、且换字体/转轮廓都救不回来时才出
   （`make_scanned.py`，300dpi，文件名以「扫描版」开头）。
   **字体没问题就不出扫描版** —— 多一份位图纯属浪费；用户点名要时才出。"""

DAN_OLD4 = """4. **要答案就默认出三份**（用户 2026-10-31 定）：①带答案原卷（`build_answer_paper.py` 或
   `build_exam_pdf.py --answers`）②纯答案卷（`answers_only.py`）③**扫描版参考答案**
   （`build_answer_paper.py` 会自动调 `scripts/make_scanned.py` 产出，**默认 300dpi**、
   **文件名以「扫描版」开头**：`扫描版_<卷名>_参考答案版_300dpi.pdf`；`--no-scan` 可关闭、
   `--scan-dpi` 可改精度）。三份都给，不额外出空白题卷；用户明确只要其中某几份时才裁剪。"""

DAN_NEW4 = """4. **要答案就默认出两份**（用户 2026-10-31 修订）：①带答案原卷（`build_answer_paper.py` 或
   `build_exam_pdf.py --answers`）②纯答案卷（`answers_only.py`）。
   ⚠️ **扫描版是回退产物，不是默认项**：只有交付前字体门禁
   （`pdf-font-fixer/scripts/detect.py`）不通过、且换字体/转轮廓都救不回来时才出
   （`make_scanned.py`，300dpi，文件名以「扫描版」开头）。
   **字体没问题就不出扫描版**；用户点名要时才出。"""

WISE_OLD_PRIN = "1. **三件套一起给**：参考答案版（矢量、红字标在题上）+ 纯答案版 + **扫描版参考答案**（300dpi、文件名以「扫描版」开头）。"
WISE_NEW_PRIN = "1. **两份一起给**：参考答案版（矢量、红字标在题上）+ 纯答案版。扫描版只在字体门禁不通过时补（见规则 4）。"

WISE_OLD_TAB = """| 1 | 三件套 | 参考答案版 / 纯答案 / `扫描版_*`（名字含 dpi）都在 |
| 2 | 扫描版 | 无文本层；内嵌图 dpi ≥ 设定值×0.95 |"""
WISE_NEW_TAB = """| 1 | 两份齐全 | 参考答案版 / 纯答案 都在 |
| 2 | 字体门禁 | `pdf-font-fixer/scripts/detect.py` 退出码 0（字体全是 TrueType） |
| 2b | 扫描版（若存在才查） | 无文本层；内嵌图 dpi ≥ 设定值×0.95 |"""


def apply(path, pairs, tag):
    if not os.path.exists(path):
        print('[skip] 不存在', path)
        return
    s = open(path, encoding='utf-8').read()
    orig = s
    for old, new in pairs:
        if old in s:
            s = s.replace(old, new, 1)
        elif new.split('\n')[0] in s:
            pass
        else:
            print('  [!!] %s 锚点未命中：%s' % (tag, old.splitlines()[0][:50]))
    if s != orig:
        open(path, 'w', encoding='utf-8').write(s)
        open(path, 'rb').read().decode('utf-8')
        print('  ✓ %s 已更新' % tag)
    else:
        print('  = %s 无变化' % tag)


print('== wise-exam ==')
apply(WISE, [(WISE_OLD4, WISE_NEW4), (WISE_OLD_PRIN, WISE_NEW_PRIN), (WISE_OLD_TAB, WISE_NEW_TAB)], 'wise-exam')
print('== daniel-exam ==')
apply(DAN, [(DAN_OLD4, DAN_NEW4)], 'daniel-exam')
