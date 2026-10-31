"""给所有出 PDF 的 skill 追加「交付前字体门禁」硬规则（外部引用 pdf-font-fixer）。
幂等：已存在同标题则跳过。
"""
import os

ROOT = '/root/.skills'
SKILLS = ['cn-word-card', 'wise-exam', 'daniel-exam', 'daniel-typeset',
          'daniel-reading', 'book-to-learn', 'my-pptx', 'daniel-poster']

BLOCK = """
---

## 交付前字体门禁（强制，不可跳过）

**本 skill 产出的任何 PDF，在交给用户之前必须最后一个跑这一步。**

```bash
FIXER="${PDF_FONT_FIXER:-$HOME/.skills/pdf-font-fixer}"
python3 "$FIXER/scripts/detect.py" <产物.pdf>      # 退出码 0=通过，2=不通过
```

- **0**：可以交付。
- **2**：不许交付。先修字体重新生成（把出问题的中文字族换成 `Noto Sans SC`，它是 TrueType；
  **不要用 `Noto Sans CJK SC`**，那是 CFF，手机会乱码）；实在换不了才用
  `python3 "$FIXER/scripts/fix.py" <产物.pdf>`，并且必须提示用户
  「**可复制性已牺牲，要保留复制请替换 XXX 字体**」（XXX 填具体字体名）。

原理与三种病因见 `pdf-font-fixer/SKILL.md`。一句话：**CFF/OpenType 轮廓的中文字体
（Noto Sans CJK、PingFang、多数 OTF）在部分手机打印预览里画不出字形，整页中文变乱码。
TrueType 中文字体（Noto Sans SC / 方正系列 TTF / 文泉驿）全平台正常。**
"""

for sk in SKILLS:
    p = os.path.join(ROOT, sk, 'SKILL.md')
    if not os.path.exists(p):
        print('[skip] %s 无 SKILL.md' % sk)
        continue
    s = open(p, encoding='utf-8').read()
    if '交付前字体门禁' in s:
        print('= %s 已存在' % sk)
        continue
    if not s.endswith('\n'):
        s += '\n'
    s += BLOCK
    open(p, 'w', encoding='utf-8').write(s)
    open(p, 'rb').read().decode('utf-8')
    print('OK %s 已追加门禁章节' % sk)
