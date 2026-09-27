<!--
Copyright (c) 2026 杨鹏飞 / 微信公众号「叉车技术老炮」
Licensed under the MIT License - 完整协议见 ../LICENSE.md
-->
# forklift-expert 使用详解

> 本文件是 SKILL.md 的**补充与扩展**,为 LLM/Agent/集成开发者提供
> 更细颗粒度的使用说明、调用示例、边界条件和故障排查指引。
> 速查请用 [SKILL.md](SKILL.md);深入使用请读本文。

---

## 一、Skill 在系统中的位置

```
用户问题
  ↓
LLM Agent 触发识别
  ↓ (匹配触发词)
forklift-expert Skill 激活
  ↓
读取 SKILL.md → 步骤 0 语言判定 → 工作流 → 选择模块文件
  ↓
references/ 下的 16 个模块文件 + 联网检索
  ↓
按输出模板生成回答（语言随用户,图表默认 SVG）
  ↓
返回给用户（招投标类额外交付 HTML 文件）
```

---

## 二、模块文件清单与适用场景

| 模块文件 | 主题 | 何时读 |
|----------|------|--------|
| `references/brands.md` | 品牌与官网目录 | 任何涉及品牌/产品的问题 |
| `references/standards.md` | 国标/ISO/EN 标准 | 法规/标准问题,且本地有收录 |
| `references/standard-retrieval.md` | **标准联网检索模块** | 状态/条款/未收录标准/用户要求"查一下" |
| `references/knowledge.md` | 基础知识问答 | 技术/分类/原理类问题 |
| `references/tech-battery.md` | **动力电池技术库** | 电池/充电/BMS/衰减/热管理/电压平台 |
| `references/heavy-spec-electric.md` | **大吨位电叉参数参考** | 6-8 吨级电叉选型、布置校核、性能对标 |
| `references/selection-guide.md` | 选型决策指南 | 选型/采购/推荐车型 |
| `references/fault-diagnosis.md` | 故障诊断手册 | 故障/维修/诊断 |
| `references/safety-regulation.md` | 安全/驾照/保险 | 安全/法规/驾照/保险 |
| `references/safety-management.md` | **安全管理实务** | 彻底检验/风险管理/LOTO/现场交通管理 |
| `references/market-trends.md` | 行业动态与趋势 | 行业整体趋势(本地数据基准) |
| `references/maintenance-plan.md` | 维保计划与定期保养 | 保养/检修/维保周期 |
| `references/parts-consumables.md` | 配件/易损件/消耗品 | 配件选型/型号/规格 |
| `references/used-forklift-evaluation.md` | 二手叉车评估 | 二手评估/选购 |
| `references/sales-news.md` | **销售动态(联网+图表)** | **销售排行/销量/市场份额** |
| `references/svg-chart.md` | **图表生成(SVG 默认)** | **一切需要配图的数值对比/份额/趋势** |
| `references/tender-broadcast.md` | **招投标播报(周度+HTML)** | **招标/投标/中标/采购公告** |
| `references/i18n.md` | **多语言(中/英自动匹配)** | **英文提问、术语一致性、双语输出** |

> 说明:v2.5 起移除公众号文章索引模块——该数据源受平台反爬限制,无法稳定获取,
> 不具备依赖价值。作者信息见 `AUTHOR.md`,项目总览见 `README.md`(中英双语)。

---

## 三、典型使用场景示例

### 场景 1:用户问品牌(单品牌查询)

**输入**: "比亚迪叉车怎么样?"

**Skill 处理**:
1. 触发词"叉车"命中 → 激活
2. 问题类型识别:品牌/产品类
3. 读 `references/brands.md` 找到比亚迪叉车条目
4. 查 web_search 补具体型号参数
5. 按"模板 A:品牌/产品咨询"输出

**输出示例**:
```
[比亚迪叉车] 简述
- 官网: www.bydforklift.com
- 母公司/上市: 比亚迪(1211.HK)
- 主营产品类: I/III 类,锂电叉车为主,钠电(2026 量产)
- 代表型号: 详见官网(web_search 补)
- 关键参数: 详见官网(web_search 补,不给编造值)
- 适用场景: 室内、3-5 吨级、新能源场景
- 来源: 比亚迪叉车官网 + 2025-2026 行业数据
```

### 场景 2:用户问选型(推荐车型)

**输入**: "我有个冷库,高 6 米,通道 2.8 米,推荐什么叉车?"

**Skill 处理**:
1. 触发词命中 → 激活
2. 问题类型:选型决策类
3. 读 `references/selection-guide.md` 走决策流程
4. 匹配:室内 + 6m 高架 + 2.8m 通道 → Class II 前移式锂电
5. 按"模板 B:选型决策"输出

**输出示例**:
```
场景:冷库室内作业,货架 6m,通道 2.8m
建议:
- 吨位: 1.5-2 吨
- 动力: 锂电(LFP,带低温加热)
- 类别: ISO Class II 前移式
- 品牌带: 比亚迪 / 杭叉 XE / 丰田 8FBE
- 配置: 全封闭驾驶室 + 防凝露加热
- 预算: 18-28 万(单台参考)
- 风险点: 低温充电效率,LFP 选带加热版
参考: references/selection-guide.md 第 X 节
```

### 场景 3:用户问销量排行(销售模块)

**输入**: "2026 年叉车销量排行?国内国外分别怎么样?"

**Skill 处理**:
1. 触发词"销量""排行"命中 → 激活
2. 识别:销售类 → 激活 `references/sales-news.md`
3. 联网检索最近月度数据
4. 按国内/国外分组
5. 按"模板 S"输出,带图表

**输出示例**(精简):
```
# 叉车销售动态报告(截至 2026-08)

## 国内品牌 TOP 5
| 排名 | 品牌 | 销量(万台) | 份额 |
| 1 | 安徽合力 | 39.45 | xx% |
| 2 | 杭叉集团 | xx.xx | xx% |
...

### ASCII 柱状图
```
安徽合力   ████████████████████████  39.45 万台
杭叉集团   ██████████████████████    xx.xx 万台
...
```

## 国外品牌 TOP 5
| 排名 | 品牌 | 销量(万台) | 全球份额 |
| 1 | 丰田 | xx.xx | xx% |
...

数据源: CITA 月报 / 海关 / 联网检索 2026-08-XX
```

### 场景 4:用户问标准状态(标准检索)

**输入**: "GB/T 43756-2024 现在还现行吗?"

**Skill 处理**:
1. 触发词"标准号"命中 → 激活
2. 识别:法规/标准类 + 状态确认 → 激活 `references/standard-retrieval.md`
3. 本地库先查 `references/standards.md`
4. 联网核验(openstd.samr.gov.cn / std.samr.gov.cn)
5. 按"模板 D+:标准检索(联网核验)"输出

### 场景 5:用户问故障(诊断)

**输入**: "我的合力 3 吨叉车起升无力,怎么回事?"

**Skill 处理**:
1. 触发词"叉车"命中
2. 识别:故障诊断类
3. 读 `references/fault-diagnosis.md` 匹配"起升无力"症状
4. 按"模板 C:故障诊断"输出可能原因+处理

### 场景 6:用户要图表（SVG 默认，v2.4 新增）

**输入**: "给我画个叉车品牌销量的图"

**Skill 处理**:
1. 识别:数值对比 → 走 `references/svg-chart.md`
2. 联网取最新销量数据（联动 `references/sales-news.md`）
3. 选择图表类型:品牌排行 → 横向条形图;国内外对比 → 分组柱状图
4. 生成**内联 SVG**（零 CDN、`viewBox` 自适应、数据标签、来源行）
5. 同时保留 Markdown 表格供精确复制

**输出要点**:
```
- 内联 <svg> 横向条形图,首名橙 #ff6b35,其余深蓝 #1a2a4a
- 每柱标数值,含标题/单位/检索日期/来源行
- 用户说"要文本图/终端看" → 降级 ASCII 并说明
```

### 场景 7:用户用英文提问（v2.4 新增）

**输入**: "Which electric forklift brands sell best in China in 2026?"

**Skill 处理**:
1. **步骤 0 语言判定**:英文占比 > 60% → 判定为英文
2. 识别:销售类 → `references/sales-news.md`
3. 联网检索
4. 按"模板 S"输出,但**表头、图表标签、脚注全部英文**
5. 术语按 `references/i18n.md` 对照表;品牌名/型号/标准号保持原形

**输出示例**:
```
# Forklift Sales Report (as of 2026-08)

## Domestic Brands
| Rank | Brand | Sales (10k units) | Share | YoY |
|------|-------|-------------------|-------|-----|
| 1 | Anhui Heli | 39.45 | xx% | +xx% |

（SVG chart with English labels）
Data source: CITA, retrieved 2026-09-12
```

### 场景 8:用户咨询招投标信息（v2.4 新增）

**输入**:（2026-09-12 周六）"本周有什么叉车招标信息?"

**Skill 处理**:
1. 触发词"招标"命中 → 激活 `references/tender-broadcast.md`
2. **锁周窗口**:2026-09-07(周一) ~ 2026-09-13(周日)
3. 多渠道联网检索（政府采购网 / 公共资源交易平台 / 招投标公共服务平台）
4. 清洗分类:招标 / 中标 / 变更废标;按车型与金额分组
5. 结构化汇总 + 生成**自包含 HTML**
6. 写入 `/workspace/叉车招投标信息播报_2026-09-12.html` 并 present
7. 对话中给 3-6 条文字版摘要

**HTML 交付要点**:
```
- 报告头:数据窗口 2026-09-07 ~ 2026-09-13
- 本周速览(数据卡 + SVG 区域/金额分布图)
- 重点推荐 TOP 3(橙色高亮卡)
- 招标公告清单 / 中标结果清单(表格,窄屏转卡片)
- 时间预警(未来 7 天截止)
- 零 CDN 依赖,断网可开,可转发
- 每条信息带可点击来源链接（无源不收录）
```

### 场景 9:用户问动力电池（v2.5 新增）

**输入**:"80 V 锂电叉车电池怎么选?铅酸充电器能不能直接给锂电充?"

**Skill 处理**:
1. 触发词"电池/锂电/BMS/充电"命中 → 激活 `references/tech-battery.md`
2. 先给电芯体系对比（LFP / 三元 / 钛酸锂 / 钠离子 / 铅酸）与电压平台（48 V / 80 V / 300-350 V）
3. 明确回答**禁配项**:铅酸充电器曲线与锂电 BMS 不匹配,不可直接代用
4. 补工作制（S2 60 min / S3 15%）与配重校验口径 —— 电池自重占整车 15-25%,改锂电须复核配重
5. BMS 故障信号、SOH 测试方法、热管理窗口（15-35 ℃、电芯温差 < 5 ℃）
6. 需要具体厂商容量/循环次数/价格 → 转 `web_search`

**避坑**:不给出未经核实的品牌电池包参数;锂电灭火强调**大量水降温**,不推荐普通干粉

### 场景 10:用户问大吨位电叉参数（v2.5 新增）

**输入**:"8 吨电动平衡重叉车的起升速度、爬坡度一般是多少?"

**Skill 处理**:
1. 触发词"6/7/8 吨 + 电动"命中 → 激活 `references/heavy-spec-electric.md`
2. 给整车参数量级（额定载荷 / 载荷中心 / 自重 / 前后桥载荷分配）
3. 给门架几何（h1/h2/h3/h4、m1/m2 离地间隙、Ast 通道宽度、Wa 转弯半径）
4. 给动力性能:行驶 18-20 km/h、起升 0.38-0.48 m/s、爬坡度 7-11%（满载）
5. 给电气口径:80 V 平台、双电机 S2 功率、液压 250 bar / 80 L/min、EN 16796 能耗 10.5-14.5 kWh
6. **必做提醒**:载荷中心 600 vs 900 mm 口径不同,跨厂商对比必须对齐门架型式与轮胎配置
7. 具体厂商型号值 → 转 `web_search`

### 场景 11:用户问安全管理实务（v2.5 新增）

**输入**:"出口欧洲的叉车,定期检验要怎么做?维修时能量隔离怎么管?"

**Skill 处理**:
1. 触发词"彻底检验/风险管理/上锁挂牌/交通管理"命中 → 激活 `references/safety-management.md`
2. 周期性彻底检验:检验周期（6 / 12 个月）、胜任人员独立性要求、书面报告 14 项要素、保存期限
3. 风险管理四步循环 + **控制层级顺序**（消除→替代→隔离→工程→行政→PPE）,强调工程控制优先
4. LOTO 八步 + **储能元件警告**（电容、蓄能器、举升负载在断电后仍可能释放能量）
5. 现场交通管理:持证操作、钥匙柜管控、安全带、安全作业程序、交通管理计划五要素
6. 给国内 vs 海外体系对照表,出口机型按严格口径准备
7. 具体法规条款与最新版本 → 走 `references/standard-retrieval.md` 联网核验

---

## 四、模块组合使用

实际问答中,经常需要**组合调用**多个模块:

```
[品牌 + 参数]    references/brands.md + web_search
[销量 + 趋势]    references/sales-news.md + references/market-trends.md
[销量 + 图表]    references/sales-news.md + references/svg-chart.md
[标准 + 条款]    references/standards.md + references/standard-retrieval.md
[故障 + 配件]    references/fault-diagnosis.md + references/parts-consumables.md
[选型 + 二手]    references/selection-guide.md + references/used-forklift-evaluation.md
[维保 + 安全]    references/maintenance-plan.md + references/safety-regulation.md
[招标 + 行情]    references/tender-broadcast.md + references/market-trends.md
[电池 + 选型]    references/tech-battery.md + references/selection-guide.md
[电池 + 故障]    references/tech-battery.md + references/fault-diagnosis.md
[大吨位 + 选型]  references/heavy-spec-electric.md + references/selection-guide.md
[大吨位 + 图表]  references/heavy-spec-electric.md + references/svg-chart.md
[安全 + 维保]    references/safety-management.md + references/maintenance-plan.md
[安全 + 法规]    references/safety-management.md + references/safety-regulation.md
[安全 + 标准]    references/safety-management.md + references/standard-retrieval.md
[任何 + 英文]    任意模块 + references/i18n.md
```

**原则**:主线 1 个模块 + 交叉引用 1-2 个,不堆叠超过 3 个。
**横切模块**(`references/i18n.md` / `references/svg-chart.md`)不计入堆叠数量。

---

## 五、调用本 Skill 的方式

### 5.1 在支持 Skill 的 Agent 平台(ClawHub / Claude.ai Skills / ZCode 等)
- 把整个 `forklift-expert/` 目录放到 skills 目录
- Agent 会自动按 frontmatter 识别触发词
- 用户提问命中 → 自动激活

### 5.2 通过 RAG / Embedding 检索
- 把 `references/*.md` 全部切块向量化
- 用户提问 → 向量召回 → 拼到 prompt
- 注意:本 Skill 设计为"全文阅读",向量召回可能丢失上下文
- 推荐:整文件读取 > 向量检索

### 5.3 直接 prompt 引用(轻量级)
- 在 system prompt 中告诉 LLM "有本 Skill 的 references 目录"
- LLM 按需 `Read` 文件,按工作流回答
- 适合一次性、低频问答

### 5.4 微调 / 蒸馏训练(蒸馏链路)
- 参考 `forklift-distill-project`(MiniMind 蒸馏案例)
- 数据集从 references 自动抽取 + 人工标注
- 学生模型基于已完成 SFT 的教师模型

---

## 六、常见误用与避坑

### ❌ 错误用法

| 错误 | 后果 | 正确做法 |
|------|------|----------|
| 不读 SKILL.md 直接答 | 输出格式不统一、触发硬规则绕过 | 先读 SKILL.md 工作流 |
| 凭印象编型号参数 | 错误数据(如把 CPCD200 答成 10 万吨) | 必须 web_search 实时查 |
| 混用国内/国外品牌 | 用户难以对比 | 销售类问题严格分组 |
| 二手评估给具体价格 | 误导交易决策 | 给区间不给数字 |
| 配件报价 | 区域差异大 | 引导查服务站 |
| 标准状态编造 | 法规风险 | 走 references/standard-retrieval.md 联网核验 |
| 忽略版权声明 | 协议违规(MIT 也要保留版权) | 输出带"资料来源:杨鹏飞/叉车技术老炮" |
| 用 ASCII 图当默认输出 | 移动端折行、可读性差(v2.4 起不合格) | 默认 SVG,ASCII 仅降级备选 |
| 招投标不给周窗口 | 数据新旧混杂、误导 | 报告头必须写本周一~周日 |
| 招投标编造凑数 | 严重误导投标决策 | 没搜到就说没搜到,不凑数 |
| 英文提问却中文答 | 答非所问 | 步骤 0 先做语言判定 |
| 中英混排表头 | 阅读割裂 | 全语言一致,双语需显式请求 |

### ⚠️ 边界情况

1. **多轮对话上下文**:Skill 是无状态的,每轮问答都需重新读取相关文件
2. **多语言**:**v2.4 起中英双语均可作为默认输出**,按用户提问语言自动匹配;
   日/德/西语暂不支持(术语质量不足),遇到时如实说明并建议用中英
3. **数据时效**:本地库基准 2026-09,超过该时点的数据必须联网
4. **图片/图表输入**:Skill 不直接处理图像,但可基于用户描述推断
5. **SVG 渲染**:部分 Markdown 预览器/纯 CLI 不渲染内联 SVG,
   此时自动降级 ASCII 并提示
6. **招投标覆盖度**:部分企业自主采购平台需登录,公开检索可能不全,
   须在报告免责段如实说明

---

## 七、扩展与定制

### 7.1 增加新模块

如果要扩展本 Skill,推荐结构:

```
forklift-expert/
├── SKILL.md              # 总入口,更新 frontmatter 与触发词
├── LICENSE.md            # MIT
├── AUTHOR.md             # 作者信息
├── skill-card.md         # 发布卡片
├── usage-guide.md        # 使用详解(本文件)
├── references/sales-news.md         # 销售模块(范例)
├── references/svg-chart.md          # 图表模块(SVG 默认)
├── references/tender-broadcast.md   # 招投标播报模块
├── references/i18n.md               # 多语言模块
└── references/
    ├── <新模块>.md       # 新模块文件
    └── ...
```

新模块文件 frontmatter 建议:
```yaml
---
name: <模块名>
trigger: <触发词列表>
version: <版本>
---
```

### 7.2 修改触发词

编辑 `SKILL.md` 的 frontmatter `description` 字段,补充新的触发场景。

### 7.3 修改输出模板

编辑 `SKILL.md` 的"输出模板"章节,新增/调整模板格式。

### 7.4 本地化

当前 Skill 以中国数据为主。要本地化到其他国家:

1. 修改 `references/brands.md` 加入当地品牌
2. 修改 `references/standards.md` 替换为当地法规(如 ANSI/UL、CSA、JIS 等)
3. 修改 `references/sales-news.md` 的数据源(海关 → 当地统计局)
4. 修改 `references/safety-regulation.md`(驾照、保险)
5. **保留核心工作流,改数据填充**

---

## 八、性能与成本

### 8.1 Token 消耗参考

| 场景 | 读取文件数 | 输出长度 |
|------|-----------|----------|
| 简单品牌问答 | 1-2 | 200-400 字 |
| 选型决策 | 2-3 | 400-600 字 |
| 故障诊断 | 2 | 300-500 字 |
| 销售排行 | 2-3 + 联网 + SVG | 600-1200 字(含 SVG 代码) |
| 标准检索 | 2-3 + 联网 | 400-600 字 |
| 招投标播报 | 2 + 联网 + HTML | 对话摘要 300 字 + HTML 文件 |
| 综合跨域 | 4-5 | 800-1200 字 |

> 注:SVG 代码与 HTML 文件内容较占 token,属预期开销,
> 换来的是可离线渲染、可转发的成品交付物。

### 8.2 联网检索频率建议

- 标准状态类:**每次都查**(状态可能变化)
- 销量数据类:**每次都查**(月报更新)
- **招投标类:每次都查**(时效性 < 7 天,绝不缓存)
- 型号参数类:**每次都查**(新品上市)
- 基础原理类:**首次加载**(变化小)

### 8.3 缓存建议

- `references/` 全部文件可一次性加载到 context
- 标准状态、销售数据等联网结果建议带"缓存 24h"标记
- 不要缓存用户具体身份或敏感输入

---

## 九、与其他 Skill 的衔接

| 衔接场景 | 推荐 Skill |
|----------|-----------|
| 叉车故障涉及液压管路设计 | nlp-to-cad(机械) |
| 叉车进入车间布局设计 | nlp-to-cad(工业布局) |
| 叉车 AGV 调度算法 | 通用编程/算法 Skill |
| 叉车电池与储能技术 | 通用电池 Skill |
| 叉车驾照法规细节 | 通用法规 Skill |

**原则**:叉车领域的核心问题留在本 Skill,跨域问题主动转交。

---

## 十、版本与维护

- 文档版本:**v1.2(2026-09)**
- 配套 Skill:forklift-expert **v2.5**
- 维护者:杨鹏飞 / 叉车技术老炮
- 反馈渠道:微信公众号留言
- **v1.2 变更**:同步 v2.5——
  ① 全部 18 个模块迁入 `references/`(修复此前 SKILL.md / usage-guide 指向 `references/*.md`
  但文件平铺在根目录的路径断裂问题);
  ② 新增 `references/tech-battery.md`(动力电池技术,修复 `knowledge.md` 的悬空引用)、
  `references/heavy-spec-electric.md`(6–8 t 电动平衡重参数)、
  `references/safety-management.md`(周期性彻底检验 / 设备风险管理 / 上锁挂牌 / 现场交通管理);
  ③ 删除 `wechat-articles.md`(微信公众号抓取数据源不稳定,不再作为依赖);
  ④ 知识库基准由 2026-06 更新至 2026-09,品牌模块补 2026 上半年经营数据;
  ⑤ 版本号在 `SKILL.md` / `_meta.json` / `skill-card.md` / 本文件统一为 **2.5**;
  ⑥ 新增中英双语 `README.md`;
  ⑦ 场景示例、模块组合表、避坑表同步增删(去微信场景,补电池/大吨位/安全管理场景)
- **v1.1 变更**:同步 v2.4——模块清单增 `references/svg-chart.md` / `references/tender-broadcast.md` /
  `references/i18n.md`;新增场景 6(图表)/ 7(英文提问)/ 8(招投标)示例;
  模块组合表增三条;避坑表增五条;边界情况更新多语言与 SVG 渲染说明
- 已知问题:见 `references/market-trends.md` 数据时效声明;销售与招投标模块需联网,离线场景受限

---

## 十一、快速参考卡片(可粘贴到 prompt)

```markdown
# Skill:forklift-expert v2.5(叉车专家)

## 激活条件
用户问题含"叉车/电叉/柴油叉车/锂电叉车/平衡重/前移式/堆高车/AGV/
杭叉/合力/比亚迪/林德/丰田/永恒力/卡尔玛/招标/投标/中标"等词,
或涉及 ISO 5053-1 分类的工业车辆。

## 工作流
0. 语言判定(中文→中文答,英文→英文答)
1. 读 SKILL.md 识别问题类型
2. 选择模块文件(18 个 references/ 之一)
3. 数据校验:本地基准 2026-09,超过该时点必须 web_search
4. 按模板输出(A-H + S 销售 + T 招投标 + U 多语言横切)
5. 含数值对比 → 默认配 SVG 图(references/svg-chart.md)

## 硬规则
- 不编造参数/标准号/销量/招标信息
- 不报价(配件/二手)
- 销售类:联网 + 国内/国外分组 + 图表(默认 SVG)
- 图表:默认 SVG,零 CDN 依赖;ASCII 仅降级备选
- 招投标:锁周窗口(提问日所在自然周)+ 每条带链接 + 交付自包含 HTML
- 多语言:语言全程一致;标准号/品牌/型号/版权行不翻译
- 标准状态:走 references/standard-retrieval.md 联网核验
- 保留版权声明:MIT 协议下"Copyright (c) 2026 杨鹏飞"

## 输出模板
- A 品牌/产品
- B 选型决策
- C 故障诊断
- D 法规/标准
- D+ 标准检索(联网)
- E 市场/趋势
- F 配件
- G 维保
- H 二手评估
- S 销售排行(SVG 图表默认)
- T 招投标播报(周窗口 + HTML 交付)
- U 多语言横切规则(中/英自动匹配)
```