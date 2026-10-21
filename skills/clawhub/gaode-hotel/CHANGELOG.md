# 飞猪联动 CHANGELOG

## v1.0 — 2026-10-21

### 做了什么
- 新建项目子目录 `飞猪联动/`，打通高德 POI × 飞猪酒店实时库存
- `travel_agent.py`：高德 `/search` 解析任意地名（商圈、地铁站、餐厅、小区）→ 拿规范名和坐标 → 喂给飞猪 `search-hotel` 拿真实房价和预订链接
- `SKILL.md`：OpenClaw Skill 声明，intents 覆盖 `hotel_search`/`travel_booking`/`poi_anchored_hotel_search`

### 关键决策
- **双锚定策略**：高德返回的类目非住宿时用 `--key-words`（通用，如 798艺术区）；类目是住宿时（说明输入是泛名词如"西湖"）回退用 `--poi-name`（飞猪对头部景区锚定更准）。这绕开了飞猪 `--poi-name` 只认头部景区、`--key-words` 对泛名词偏移的核心限制
- **API key 只走环境变量 `GAODE_POI_KEY`**，不写入任何文件（遵守全局安全规则）
- **高德富化可选**：`--enrich-nearby` 附上目的地 1km 内餐饮，复用现有 POI 数据库

### 验证
- 798艺术区（普通商圈）→ 3 家真实酒店，¥236–¥358，feizhu.com 预订链接，锚定"近798艺术区" ✓
- 西湖（头部景区）→ poi-name 回退后锚定"近杭州西湖风景名胜区" ✓
- 酒仙桥（非著名地名）+ `--enrich-nearby` → 周边餐饮 5 条带评分 ✓

### 下一步待做
- Hackathon 截止 2026-10-25，还有 4 天：打包成可 `clawhub install` 的 Skill 包
- 补一个自然语言解析层：现在要手动拆 `--city`/`--place`/日期，下一步让 agent 直接吃"我下周去成都宽窄巷子出差住两晚"这种整句
- 录一个 30 秒 demo 视频：三句话三座城（798/西湖/宽窄巷子）展示任意地点锚定能力，作为提交作品
