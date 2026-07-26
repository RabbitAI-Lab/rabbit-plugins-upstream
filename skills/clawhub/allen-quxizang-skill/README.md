<p align="center">
  <img src="docs/images/banner.jpg" alt="布达拉宫夜景" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT License">
  <img src="https://img.shields.io/badge/data_files-24-green" alt="24 data files">
  <img src="https://img.shields.io/badge/platform-Coze%2FDify%2FOpenCode%2FClaude-orange" alt="Multi-platform">
</p>

<h1 align="center">趣西藏 · QuXizang Skill</h1>
<p align="center"><i>老领队Allen扎西陪你进藏 —— 安全第一，财富留藏，文化尊严</i></p>
<p align="center"><b>Made by Allen · 开源 MIT</b></p>

<p align="center">
  <b>中文</b> | <a href="#english">English</a>
</p>

---

**趣西藏**是一套可部署到任何 AI 平台（Coze/Dify/OpenCode/Claude）的西藏旅游助手完整资源包。不是简单的"景点介绍 + 攻略合集"——它提供了一个有灵魂的藏族老领队人设、一套硬核安全熔断系统、和一个覆盖全藏的藏民小微商户网络。

---

## 为什么需要这个项目

市面上"西藏旅游助手"不少，但大部分是：

| 普通 AI 助手 | 趣西藏 |
|-------------|--------|
| 给出笼统建议"注意高反" | 根据海拔+天数+病史+天气综合评估，**强制拦截危险行程** |
| 推荐八廓街流水线商品 | 精准匹配 33 家藏民自营商户，每一笔消费直达藏族家庭 |
| 百度百科式的文化介绍 | Allen扎西口吻的市井真话——"天珠 99% 是义乌树脂，不如买把藏香实在" |
| 想到才问，不问不说 | 自动预判下一步风险——你 D3 到拉萨，D2 就提前告诉你布宫要预约、纳木错没吃的 |
| 固定的单平台部署 | 一套资源，Coze/Dify/OpenCode/Claude 全平台通用 |

---

## 核心设计

### Allen扎西人设

Allen扎西是一个 15 年藏区老领队——直爽、真诚、责任感强。他叫你"哥们""阿佳（大姐）"，偶尔训你但永远为你着想。每个回复固定三段式：

> **🚨【Allen扎西的保命/避坑雷达】**
> 直接点出海拔、天气、证件、高反风险。无风险就写"目前看来一切安好"。
>
> **🗺️【地道藏味方案】**
> 路线、推荐、避坑技巧。涉及商户时从 33 家藏民小微商户精准匹配。
>
> **🌾【阿佳的温馨叮嘱】**
> 一条环保或文化贴士。涉及寺庙/神湖时告诉你怎么做才不犯忌。

### 安全系统

```
病史筛查 ──→ 海拔评估 ──→ 天气联动 ──→ 路况查询 ──→ 行程建议
（前置）      （熔断器）       （关键词）    （实时搜索）
```

- **病史筛查前置**：出方案前强制问有无高血压/心脏病/哮喘/怀孕等
- **海拔熔断器**：>3800m + <3 天适应 + 过夜 → **警告**；>4500m 或 <=1 天 → **强制拦截**；>5000m + 过夜 → **绝对禁止**
- **天气熔断**：识别 10 个关键词（暴雪/道路结冰/大风/强降雨/暴雨/山洪/泥石流/冰雹/沙尘暴/暴风雪）自动触发安全警告
- **路况实时查**：通过 WebSearch 搜索西行川藏等实时播报平台获取最新路况

### 三段式状态机

项目定义了用户所处的三个阶段，AI 根据用户输入自动识别并切换行为：

| 阶段 | 核心任务 | 触发逻辑 |
|:----:|---------|---------|
| **规划期** | 资格审查（病史+边防证）、出行纠偏、行前清单 | 用户表达进藏意愿 |
| **在途中** | 动态海拔监控、天气路况联动、落地 24h 天条 | 用户提到已在路上 |
| **游玩期** | 本地商户分流、文化守门、生态守护 | 用户表示已到藏区 |

### 财富留藏

33 家藏民小微商户覆盖拉萨、林芝、山南、日喀则、那曲、昌都、阿里、甘孜 8 个区域。每家标注经纬度、海拔、价格档位、营业时间，以及**Allen扎西为什么推荐这家**——每笔消费直达藏族家庭。不推荐连锁酒店和商业化高佣金网点。

---

## 📂 项目结构

```
quxizang-skill/
│
├── prompts/
│   └── system_prompt_v2.md        ← Allen扎西人设 + 三段状态机（复制到 AI 人设框）
│
├── data/                          ← 核心知识库，24 个文件，Allen扎西口吻
│   │
│   │  # 安全类（必读）
│   ├── emergency.md               ← 应急手册：高反分级、医院电话、下撤路线、直升机救援
│   ├── medical_screening.md       ← 病史筛查白皮书：绝对禁忌表、9 种慢性病专项须知
│   ├── seasonal_road_closures.md  ← 封路实操日历：9 条路线全年月度通行矩阵
│   ├── weather_climate.md         ← 四大气候战区白皮书：月均数据、含氧量、Allen扎西决策表
│   │
│   │  # 文化类（必读）
│   ├── tibetan_customs_and_taboos.md ← 文化底线大全：神山圣湖、寺庙礼仪、藏民交往规矩
│   ├── tibetan_monasteries.md     ← 深度参拜：色拉辩经、哲蚌雪顿、萨迦经书墙、桑耶坛城
│   ├── tibetan_phrases.md         ← 50 条地道藏语：点茶、砍价、问路、求救
│   ├── tibetan_history_and_culture.md ← 历史人文深度指南：七分钟通史、世界遗产、建筑、唐卡、藏戏、茶马古道
│   ├── tibetan_festivals.md       ← 节庆时间表：雪顿节、赛马节、望果节 2026 年日程
│   │
│   │  # 消费类（推荐）
│   ├── local_merchants.json       ← 33 家藏民商户：8 区域、经纬度、价格、推荐理由
│   ├── gaode_recommendations.json ← 11 家高德精选备选（免费内置，有电话有评分）
│   ├── gaode_api_usage.json       ← 高德 API 调用计数器（5000次/月自动限额）
│   ├── shopping_price_guide.md    ← 防骗白皮书：6 大品类真实价格、造假黑幕、鉴别方法
│   ├── tibetan_gifts.md           ← 伴手礼认证：藏香/藏毯/唐卡/天珠四步验证法
│   ├── tibetan_cuisine.md         ← 饮食通关：酥油茶/糌粑/石锅鸡、4 种场景点餐实战
│   │
│   │  # 实用类（按需）
│   ├── permits_and_visas.md       ← 证件白皮书：大陆/港澳/台湾/外籍四类人群完整流程
│   ├── women_travel_safety.md     ← 女性安全指南：交通/住宿/公共场所全场景+紧急应对卡
│   ├── kailash_kora.md            ← 冈仁波齐全流程：劝退标准、装备、2 天复盘、直升机救援
│   ├── accommodation_realities.md ← 住宿真相：供氧类型、洗澡禁令、供暖骗局
│   ├── transport_within_tibet.md  ← 藏内交通价目表：巴士/包车/火车 2026 年参考价
│   ├── photography_spots.md       ← 摄影机位：布宫/羊湖/纳木错最佳时间、无人机规则
│   ├── agricultural_products.md   ← 农产品防伪：牦牛肉干/虫草/藏香猪采购指南
│   ├── eco_and_wildlife.md        ← 生态安全：旱獭鼠疫、野狗、野牦牛应对
│   └── telecom_and_signals.md     ← 信号指南：运营商覆盖、卫星电话、离线地图
│
├── scripts/
│   ├── safety_circuit_breaker.py  ← 海拔安全熔断器（含 7 条内置冒烟测试）
│   ├── audit_merchants.py         ← 商户数据完整性审计（检测缺 phone/wechat/verified_at）
│   └── gaode_api.py               ← 高德 API 商户搜索（5000次/月自动限额）
│
├── references/
│   ├── api-integration-guide.md   ← 零 API 依赖说明 + Open-Meteo 可选参考
│   ├── routes.md                  ← 5 大进藏路线海拔剖面与最佳季节
│   └── budget-tier.md             ← 三档预算参考价
│
├── docs/
│   └── DEPLOY.md                  ← 三平台部署指南（Coze / Dify / OpenCode）
│
├── config.yaml                    ← 项目配置（知识库文件清单）
├── SKILL.md                       ← OpenCode Skill 入口行为规范
├── README.md                      ← 就是这个文件
└── LICENSE                        ← MIT
```

---

## 3 分钟上手

```
git clone https://github.com/anomalyco/allen-Quxizang-Skill.git
cd allen-Quxizang-Skill
# 高德 API Key 已内置免费测试 Key，即开即用
# 建议部署时申请自己的 Key 覆盖：
export AMAP_KEY='你的高德Key'
```

然后选择你的平台：

<table>
<tr>
<th>OpenCode</th>
<th>Coze</th>
<th>Dify</th>
</tr>
<tr>
<td>

```bash
# 放到 skills 目录下
cp -r quxizang-skill \
  ~/.claude/skills/

# 触发词
/去西藏  /tibet-trip  /xizang  /西藏  /进藏攻略
```

</td>
<td>

1. 人设框贴入 `prompts/system_prompt_v2.md`
2. 知识库上传 `data/` 下所有文件
3. 开始使用（零 API 依赖，即开即用）

</td>
<td>

1. 系统提示词贴入 `prompts/system_prompt_v2.md`
2. 知识库上传 `data/` 下所有文件
3. 工作流中加入 HTTP 节点

</td>
</tr>
</table>

完整部署步骤见 [`docs/DEPLOY.md`](docs/DEPLOY.md)。

---

---



## 开发

贡献新商户、修正价格、更新封路数据——直接提 PR 修改对应的 `data/` 文件即可。所有文件使用Allen扎西第一人称口吻，保持口语化、直接、真诚的风格。

运行测试：

```bash
pip install "pytest>=7.0"    # 首次运行需安装 pytest
python3 -m pytest tests/ -v  # 24 个安全熔断器测试
```

---

## 联系作者

**Allen**
- 抖音：`allen.Ai` (ID: 333358117)
- GitHub：[anomalyco](https://github.com/anomalyco)
- 公众号：<br><img src="docs/images/qr-mp.jpg" width="150" alt="Allen的公众号二维码">

## 许可证

MIT License © 2026 Allen — 抖音 @allen.Ai

---

## English {#english}

**QuXizang** is an open-source AI skill pack for traveling to Tibet, deployable across Coze, Dify, OpenCode, and Claude. It features a 15-year veteran Tibetan guide persona (Allen扎西), a hardcore safety circuit breaker system (altitude + weather + medical screening), 24 structured knowledge files covering permits, culture, history, shopping, emergencies, weather, 33 vetted local Tibetan merchants, and a deep-dive history & culture guide.

Designed to be platform-agnostic: copy the system prompt, upload the knowledge base, and start using it — no API keys required.

[中文版](#) | README available in Chinese only (project content is in Chinese by design for Tibetan travel context).
