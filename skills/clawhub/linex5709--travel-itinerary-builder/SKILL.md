---
name: travel-itinerary-builder
description: >
  旅行行程规划总入口。当用户提出多日旅行规划、制作旅行手册、定制亲子/家庭出游行程、
  或任何涉及 "旅行计划" "行程安排" "出游攻略" "旅游攻略" "day trip" "itinerary"
  等请求时触发。产出格式为自包含 HTML（零外部 CDN 依赖），包含每日时间线、
  景点卡片（图片/交通/流程/贴士）、能量趋势图、后勤工具箱。内容深度对标首尔 6 日
  亲子游手册——每个景点都有时间预估、交通指引、why/how/tips 三层信息结构。
  自动适配航班时刻、当地天气、儿童年龄。
agent_created: true
---

# 旅行行程规划 Skill

## 触发条件

当用户请求涉及以下任一场景时，加载此 skill：

- 多日旅行行程规划（不限天数）
- 亲子/家庭出游攻略
- "帮我做一份 XX 的旅行计划"
- "XX 几日游怎么安排"
- "定制一份旅行手册"
- 任何包含 "旅行" "旅游" "行程" "攻略" "itinerary" "travel plan" 的请求

## 产出格式

**始终生成自包含的 HTML 单文件**，零外部 CDN 依赖。使用 `assets/template.html` 作为 CSS 和 JS 架构模板。

### 零依赖原则（强制）

- 不使用 Tailwind CDN、Chart.js CDN、Google Fonts 等外部资源
- 纯原生 CSS 变量系统 + 纯 JS 渲染
- 系统字体栈：`'PingFang SC','Microsoft YaHei','Hiragino Sans GB',system-ui,-apple-system,sans-serif`
- 图表使用纯 CSS 条形图（参照模板 `renderChart()` 的实现）
- 图片使用本地路径或内嵌 SVG 降级占位（加载失败显示景点名称）

### HTML 整体结构

```
header (sticky, logo + 标题 + 日期 + 标签)
  ├── overview-card (能量趋势 CSS 条形图 + 关键统计)
  ├── day-nav (日期切换按钮)
  ├── #day-content (动态渲染区域)
  │   ├── day-intro (日期badge + 航班badge + 标题 + 描述 + 时间线)
  │   └── spots-list
  │       └── spot-card × N
  │           ├── spot-img-wrap (景点大图 + 浮层名称)
  │           └── spot-body
  │               ├── time-badge (建议游玩时长)
  │               ├── transport-box (交通指引)
  │               ├── spot-reason (Why It's an Adventure?)
  │               ├── spot-how (编号步骤)
  │               └── tips-box (Expert Tips)
  ├── logistics (住宿建议 / 地图App / 必备装备)
  └── footer
```

### 每日景点卡片必须包含

| 字段 | 说明 | 示例 |
|------|------|------|
| `name` | 景点全称（双语） | "HiKR Ground (好客空间)" |
| `img` | 图片路径（本地优先） | `seoul_images/compressed/hikr_ground.jpg` |
| `timeSlot` | 建议时间窗口 + 游玩时长 | "16:00 — 18:00（建议游玩 2 小时）" |
| `transport` | 交通方式、线路、耗时 | "从明洞步行约 10 分钟即达" |
| `reason` | 为什么值得去（3-5句） | 从体验独特性、孩子适配度、体力消耗角度说明 |
| `how` | 编号步骤 4-5 步 | 每步写明具体做什么、区域/楼层、时间分配 |
| `tips` | 实用贴士 | 价格、预约、穿着、最佳时段、备选方案 |

## 内容写作规范

### 每日结构

```javascript
{
  title: "简洁有力的日主题（8-15字）",
  date: "X月X日（周X）",
  flightNote: "✈️ 航班信息（仅首尾日）",
  timeline: "08:00 → 09:00 ... → 20:00 返回（全天时间节点）",
  description: "当日概述（3-5句）：主题定位 + 体力节奏 + 关键衔接逻辑",
  spots: [ /* 2-3 个景点卡片 */ ]
}
```

### 时间与交通合理性（强制校验清单）

在编写每段行程时，必须逐项确认：

- [ ] **航班窗口**：首日以落地+出关+交通后 2-3 小时为游览起点；末日以航班起飞前 3 小时到达机场为终点
- [ ] **交通耗时**：每个景点间标注实际地铁/步行耗时（参考 Naver Map 级别精度）
- [ ] **用餐时间**：每天预留 1-1.5 小时午餐 + 1 小时晚餐，标注推荐餐厅类型
- [ ] **午间避暑**：夏季（6-9月）12:00-15:00 尽量安排室内活动
- [ ] **儿童节奏**：每 2-3 小时安排一次休息点（咖啡馆、草坪、书店）
- [ ] **总时长**：每日游览时间不超过 10 小时（含交通）

### 推荐开场描述模板

```
今日是[主题定位]。上午[活动A]，下午[活动B]。[衔接逻辑描述]。
[体力消耗预估]。[特别提醒——天气/人流/时间]。
```

### 景点描述三层结构

1. **Why（推荐理由）**：体验独特性 + 孩子适配度 + 体力消耗 + 教育/情感价值
2. **How（操作步骤）**：4-5 步，每步标注【区域/楼层】+ 具体动作 + 预估耗时
3. **Tips（实用贴士）**：价格、预约要求、穿着建议、最佳时间段、雨天备选、排队策略

### 工具箱 (Logistics) 必须包含

1. **住宿建议**：推荐区域 + 理由 + 机场交通方式 + 参考价格
2. **地图与App**：当地必备 App 及其用途（导航/打车/翻译）
3. **必备装备**：季节适配的装备清单（夏季强调防晒+薄外套+折叠伞）

## 图片获取策略

1. **首选**：从 Wikipedia Commons / Wikipedia REST API 搜索景点相关图片，下载到本地
2. **批量请求**：每次请求间隔 ≥3 秒，避免 429 限流
3. **压缩处理**：下载后使用 Pillow 压缩至 1600px 宽、JPEG 80% 质量
4. **降级方案**：HTML 中 `onerror` 回调渲染 SVG 占位图（灰底+景点名称）
5. **备选**：如果图片获取困难，建议用户生成 PDF 版本（嵌入图片，完全自包含）

## 能量趋势图

使用纯 CSS 条形图（参照模板 `renderChart()`），显示每日：
- 体能消耗指数（蓝色条，1-100）
- 趣味冒险指数（琥珀色条，1-100）

数值判断参考：

| 情景 | 体能 | 趣味 |
|------|------|------|
| 全室内轻松日（如 KidZania） | 40-50 | 90-100 |
| 水上运动日 | 85-95 | 85-90 |
| 半天室内+半天室外 | 65-75 | 80-90 |
| 半日到达首日 | 35-45 | 60-70 |
| 半日离开末日 | 45-50 | 75-85 |

## 语言

- 使用简体中文
- 景点名称附带原文/英文名
- 价格标注当地货币 + ₩/¥/$ 符号
- 日期格式：X月X日（周X）
- 语气：专业但亲切，像资深旅行策划师

## 参考资料

`assets/template.html` — 完整的首尔 6 日游 HTML 模板，包含所有 CSS 变量、JS 渲染逻辑和响应式布局。每次生成新行程时：
1. 复制此模板
2. 替换标题、日期、航班信息
3. 修改 `itinerary` 对象中的每日数据
4. 更新 `chartData` 中的能量值
5. 调整 logistics 内容为目的地适配版本
6. 替换所有图片路径

## 图片处理 Python 脚本参考

当需要从 Wikipedia 获取景点图片时，使用以下模式（每次请求间隔 ≥3 秒）：

```python
import requests, time
from PIL import Image

HEADERS = {'User-Agent': 'TravelItineraryBot/1.0'}
BASE = 'https://en.wikipedia.org/api/rest_v1/page/summary/'

def get_image(title):
    resp = requests.get(BASE + title, headers=HEADERS, timeout=15)
    if resp.status_code == 200:
        data = resp.json()
        return data.get('originalimage', {}).get('source')
    return None

def compress(input_path, output_path, max_width=1600, quality=80):
    img = Image.open(input_path)
    if img.width > max_width:
        ratio = max_width / img.width
        img = img.resize((max_width, int(img.height * ratio)), Image.LANCZOS)
    img.save(output_path, quality=quality, optimize=True)
```

按上述模式下载后立即压缩，再用于 HTML/PDF 生成。
