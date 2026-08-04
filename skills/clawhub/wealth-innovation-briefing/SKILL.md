---
name: wealth-innovation-briefing
description: 生成《金融创新简报（财富管理）》竖版 A4 海报 PDF —— 按 6 个方向 × 5 条共 30 条，每条含具体公司、新闻链接、事件说明(≥100字)、创新点、某股份制银行学习点。适合每日/每周自动化，向领导汇报与邮件分享。
agent_created: true
---

# 金融创新简报（财富管理）海报 PDF 生成器

把"采集金融创新动态 → 结构化 30 条 → 渲染高大上竖版 A4 海报 PDF"整套工作流固化下来。
核心思想：**数据与样式解耦**——模板 `build_briefing_template.py` 只管版式，每次只换 `today / EXTRA / DIRECTIONS / SUMMARY_LEAD` 四个变量后调用 `build()`，绝不动 CSS。

## 何时使用
- 用户要"每日/每周金融创新简报""财富管理动态""私人银行产品权益创新"这类海报/PDF 汇报物。
- 自动化任务（每日 09:00 触发）需要稳定产出可邮件分享的竖版 A4 PDF。
- 用户想微调方向、加数据交叉验证、改版式配色时，改对应变量即可。

## 交付物规格（硬约束）
- 竖版 A4（`@page { size: A4; margin: 0 }`），PDF 无页眉页脚，可邮件分享。
- 6 方向 × 5 条 = 30 条。方向命名建议固定为：
  `存款理财` / `理财货架` / `公募基金` / `私募与高净值` / `银保协同` / `信托创新`
  （原始需求是 4 大类"存款理财、公募私募、银保、信托"，实践中拆成这 6 个方向更饱满）。
- 每条必含：`title`(观点式标题) + `source`(来源) + `link`(新闻链接) + `body`(≥100字事件说明) + `innovation`(创新点) + `learning`(某股份制银行学习点)。
- 每方向额外配 `EXTRA`：`tags`(3-6个关键词) + `insight`(核心洞察) + `action`(银行行动建议)。
- 页面结构：封面 → 本期摘要 → 6 方向各【1 页导读 + 2 页案例(前3条 + 后2条+小结卡)】= 20 页。

## 工作流（每跑一次做这 4 步）
1. **采集**：用 WebSearch 按 6 方向各找 5 条近期权威新闻（财联社/券商中国/中国证券报/21世纪经济报道/上海证券报/澎湃/界面/每经/各公司官网及公众号）。每条确认有具体公司、可引用链接、足够写满 100+ 字的细节。
2. **写数据**：生成 `content_<日期>.py`，导出 `DIRECTIONS`（结构见 references/content_template.py）与 `EXTRA`（按方向 title 索引）。
3. **构建 HTML**：写 `build_<日期>.py`，import 模板后覆盖四个变量并 `tpl.build()`（见下"复用方式"）。产出 `briefing.html`。
4. **渲染 PDF**：跑 `convert_pdf.py`（见 references/convert_pdf.py），用本地缓存 Chromium 把 HTML 转 A4 PDF。
   之后调用 `present_files` 交付，并把高层摘要写回自动化 `memory.md`。

## 复用方式（build 脚本骨架）
```python
import sys, os
sys.path.insert(0, os.path.dirname(__file__))   # 让模板与数据文件可被 import
import build_briefing_template as tpl
from content_20260728 import DIRECTIONS, EXTRA  # 你的数据

tpl.today = "2026年7月28日"
tpl.DIRECTIONS = DIRECTIONS
tpl.EXTRA = EXTRA
tpl.SUMMARY_LEAD = "三条主线摘要……"   # 导读页那段长文，建议按"确定性资产争夺/规则重塑/账户化跃迁"三条主线写

if __name__ == '__main__':
    tpl.build()
```
模板在 references/build_briefing_template.py：只改 `today/DIRECTIONS/EXTRA/SUMMARY_LEAD` 四个全局变量，调用 `build()`。
`build()` 会写出 `briefing.html`（同目录）。**不要重写 CSS。**

## 数据格式（content_<日期>.py）
```python
DIRECTIONS = [
  {
    "title": "存款理财：长钱锁定与活动化权益",
    "subtitle": "五年期大额存单从大行到股份行梯次重启……",
    "items": [
      {
        "title": "中国银行“七全期限”大额存单：国有大行破冰5年期",
        "source": "中国银行、网易财经",
        "link": "https://www.163.com/...",
        "body": "≥100字：时间+公司+动作+数据+为什么值得关注……",
        "innovation": "创新点：……",
        "learning": "银行学习点：……"
      },
      # ... 每方向 5 条
    ]
  },
  # ... 6 个方向
]
EXTRA = {
  "存款理财：长钱锁定与活动化权益": {
    "tags": ["五年期存单","活动化运营","场景权益"],
    "insight": "核心洞察……",
    "action": "银行行动建议……"
  },
  # 键必须 === 对应 DIRECTIONS[].title，否则小结卡为空
}
```
**约束**：`EXTRA` 的键必须与 `DIRECTIONS[].title` 完全一致（含冒号前后文），否则导读页/小结卡的 tags、insight、action 会落空。

## PDF 渲染（convert_pdf.py 要点）
- 依赖：Python 3.x + `pip install playwright`；渲染用**本地已缓存的 Chromium**：
  `C:\Users\Administrator\AppData\Local\ms-playwright\chromium-*\chrome-win64\chrome.exe`
  （脚本用 `glob` 自动找最新一份，无需联网下载）。
- `page.pdf(format="A4", print_background=True, margin=0, prefer_css_page_size=True)` 才会尊重 `@page` 竖版分页。
- 输出文件名带日期，如 `金融创新简报_财富管理_2026-07-28.pdf`。

## 已知坑（必读，踩过）
1. **路径 sed 误伤**：用 `sed 's/旧日期/新日期/'` 批量改脚本会**连 `OUT_DIR` 里的目录名一起改掉**，导致 `net::ERR_FILE_NOT_FOUND`。
   修复：只改文件名里的日期，`OUT_DIR` 始终指向真实工作目录（如 `automation-2026-07-27-20-34-05/outputs`）。
2. **EXTRA 键不匹配**：见上，键必须严格等于 direction title。
3. **HTML 屏幕预览看不出分页**：浏览器里 HTML 是连续滚动的（屏幕不认 `@page`），但 PDF 渲染会按 `page-break-after` 正确分页，属正常现象，别被截图误导。
4. **summary_html 旧版需 override**：本模板已把摘要长文抽成 `SUMMARY_LEAD` 变量，直接赋值即可，不用再 monkey-patch 整个函数。
5. **device_scale_factor**：设为 2 让 PDF 文字更锐利；viewport 1240×1754 近似 A4@150dpi。

## 自动化集成（若是定时任务）
- 自动化指令照抄"业务 prompt"（见本文件末尾），再加 5 步系统流程：①读 memory.md → ②执行 → ③输出 → ④present_files → ⑤写 memory.md 摘要。
- memory.md 只写**高层摘要**（日期/6方向主题/交付文件/关键趋势/与上一版差异），**不要**把 30 条全文或正文塞进去。

## 业务 prompt（原始指令，自动化每天触发执行的即此段）
> 关注当天金融业（私人银行、财富管理）领域的产品权益活动场景创新的重要动态，侧重需求走向、产品创新、模式创新、权益升级、技术创新方向。筛选按存款理财、公募私募、银保、信托 4 类别分成 6 个方向，每个方向 5 条有价值的信息，要标记出来具体的内容，要包括具体的公司，新闻链接，简要说明事件内容及值得关注的原因。每一条需要至少 100 字。而且要写出来创新点，和值得某股份制银行财富管理学习的地方。而且输出的样式要是一个海报样式的 pdf，可以分享给人发邮件的，需要页面高大上，适合向着领导汇报。要求竖版排版。
