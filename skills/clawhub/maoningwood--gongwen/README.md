# gongwen — 党政机关公文 docx 生成 Skill

一个 [ZCode](https://zcode.dev) / 兼容 SKILL.md 约定的 agent skill：让 AI 助手按机关通行
公文版式生成规范的 docx 公文（通知、报告、请示、批复、函、会议纪要等），自带字体检查
和版式数字验收，生成结果可直接交 WPS / Office 使用。

## 版式规范（内置，非国标 GB/T 9704）

| 元素 | 字体 | 字号 | 其他 |
|---|---|---|---|
| 大标题 | 方正小标宋简体 | 二号 22pt | 居中，行距固定 33 磅，长标题手工分行 |
| 副标题 / 二级标题 | 楷体_GB2312 | 三号 | 副标题居中；二级标题不加粗 |
| 一级标题 | 黑体 | 三号 | |
| 三级标题 | 仿宋_GB2312 | 三号 | 加粗 |
| 正文 | 仿宋_GB2312 | 三号 16pt | 首行缩进 32 磅（2 汉字），行距固定值 29 磅，两端对齐 |
| 数字 / 西文 | Times New Roman | 随所在段落 | |
| 页边距 | 上下 2.54cm、左右 3.17cm | | A4，Word 默认边距体系 |

> 注意：本规范采用 Word 默认页边距体系，与 GB/T 9704 红头文件版式（3.7/3.5/2.8/2.6
> 边距等）不同，请勿混用。

## 安装

```bash
# 方式一：skills.sh 一键安装（自动识别 Claude Code / Codex / Cursor 等 75+ agent）
npx skills add maoningwood/gongwen

# 方式二：git clone（用户级，所有项目可用）
git clone https://github.com/maoningwood/gongwen.git ~/.agents/skills/gongwen
# 或项目级：克隆到 <项目>/.agents/skills/gongwen

pip3 install --user python-docx   # 唯一的运行时依赖
```

## 字体要求（重要，请先阅读）

公文对字体要求严格，**规定的字体不可用其他字体替代**。本仓库**不随附任何字体文件**：
以下字体均为商业版权（方正/中易/长城），随软件再分发字体文件属于侵权行为，
请使用者自行获取并安装。

| 字体 | 版权方 | 用途 | 获取渠道建议 |
|---|---|---|---|
| 方正小标宋简体 | 北大方正 | 大标题 | 方正字库官网 [foundertype.com](https://www.foundertype.com) 注册后可免费下载（个人非商业用途）；机关或装过 Office 的电脑通常已预装 |
| 黑体（SimHei） | 北京中易 | 一级标题、表头 | Windows / Office 中文版自带，可从自有授权的 Windows 电脑复制安装 |
| 楷体_GB2312 | 长城计算机 | 副标题、二级标题 | 随 Windows / Office 中文版附带 |
| 仿宋_GB2312 | 长城计算机 | 正文、三级标题、落款 | 随 Windows / Office 中文版附带 |

检查字体是否齐全（生成前必做，skill 会自动执行）：

```bash
python3 ~/.agents/skills/gongwen/scripts/check_fonts.py
```

缺字体时会明确列出名称、用途和获取渠道建议；装好后重跑直至全部 `[OK]`。
下载与安装来源的合规性由使用者自行把握，本项目不提供也不指向任何盗版字体资源。

## 使用

对 agent 说"写个通知：……"“按公文格式排一下这份报告"即可自动触发。生成代码示例：

```python
import sys
sys.path.insert(0, '~/.agents/skills/gongwen/scripts')  # 展开为实际路径
from gongwen_builder import GongwenDoc

g = GongwenDoc()
g.title(['关于召开年度重点工作', '推进会议的通知'])   # 长标题手工分行，防孤字行
g.recipient('各处室、各有关单位：')          # 主送机关顶格
g.para('为……，现将有关事项通知如下：')
g.h1('一、会议时间')
g.h2('（一）参会单位')
g.para('……')
g.table(['处室', '金额\n（万元）'], [['××处', '65.00']])
g.signoff('××市××局', '2026年9月2日')
g.save('会议通知.docx')
```

生成后用验收脚本核对版式（数字通道，不依赖目测）：

```bash
python3 ~/.agents/skills/gongwen/scripts/verify_gongwen.py 会议通知.docx
```

## 目录结构

```
gongwen/
├── SKILL.md                    # skill 入口：版式规范、易错点、流程、验收纪律
├── README.md
├── LICENSE
└── scripts/
    ├── gongwen_builder.py      # python-docx 构建库（版式全部封装）
    ├── check_fonts.py          # 字体检查（零依赖，macOS/Linux/Windows）
    └── verify_gongwen.py       # 版式数字验收
```

## 许可

代码以 [MIT License](LICENSE) 开源。**字体不在许可范围内**——本仓库不含任何字体文件，
也不授予任何字体的使用、复制或分发权利。
