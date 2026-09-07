<!-- Copyright (c) 2026 杨鹏飞 | MIT License | forklift-expert v2.4 -->

# 中英双语模块 — 术语对照 / 检索通道 / 英文输出规范

> 本模块是 v2.4 新增的**语言路由配套文件**。
> 解决三件事:① 用户用英文提问时能触发本技能;② 英文提问用英文作答;
> ③ 英文提问走英文检索通道(Google 优先),不再拿中文搜索引擎的中文结果糊弄人。
> 完整流程见 SKILL.md 的「语言路由与检索通道」章节。

---

## 一、语言判定与响应规则

### 判定矩阵

| 用户输入 | 输出语言 | 检索通道 | 检索关键词语言 |
|---------|---------|---------|--------------|
| 纯中文 / 中英混排(中文为主) | 中文 | 中文通道(百度 + 必应中文 + 国内权威源) | 中文关键词 |
| 纯英文 | **英文** | **Google 英文通道**(`hl=en&gl=us`,见第三节) | 英文关键词 |
| 英文为主 + 少量中文(如英文问句里夹品牌中文名) | **英文** | Google 英文通道 | 英文关键词 |
| 中文问句里夹英文术语(如"叉车 BMS 是什么") | 中文(术语保留英文并加中文注释) | 中文通道 | 中英混查 |

### 三条硬规定

1. **语言跟随用户,不跟随知识库**:`brands.md` / `standards.md` 等本地库是中文写的,
   但英文提问时必须**把结论用英文重述**,而不是把中文段落原样吐给用户。
2. **术语不得硬译**:必须使用第二节的对照表。禁止把"前移式叉车"译成 "forward-moving
   forklift"、"门架"译成 "door frame"、"属具"译成 "tool" 这类字面硬译。
3. **数字与单位需本地化**:英文输出时,公制保留但补英制换算
   (如 `2.5 t (5,510 lb)`、`3,000 mm (118 in)`)。详见第四节。

---

## 二、中英术语对照表

### 2.1 车辆类型(ISO 5053-1 分类)

| 中文 | English | 备注 |
|------|---------|------|
| 平衡重式叉车 | counterbalance forklift truck | 电动/柴油/锂电均属此类 |
| 三支点叉车 | 3-wheel counterbalance truck | 单驱动轮 + 双转向轮 |
| 前移式叉车 | reach truck | 门架/货叉前移,**不是** forward-moving forklift |
| 电动托盘搬运车 | powered pallet truck / pallet jack | 步行式称 walkie pallet truck |
| 电动堆高车 | pedestrian stacker / walkie stacker | 步行式堆垛 |
| 拣选车 | order picker | 人随货升 |
| 三向堆垛叉车 | very narrow aisle (VNA) truck | 又称 man-up / combi truck |
| 侧面叉车 | sideloader | 长物料工况 |
| 越野叉车 | rough terrain forklift | 4WD,大胎 |
| 集装箱正面吊 | reach stacker | 港口正面吊 |
| 空箱堆高机 | empty container handler | |
| 集装箱叉车 | container handler / heavy-duty forklift | |
| 防爆叉车 | explosion-proof forklift | ATEX / IECEx 认证 |
| 冷库叉车 | cold store forklift / freezer forklift | 低温工况 |
| 港口叉车 | port forklift / terminal forklift | |
| AGV / AMR | AGV (Automated Guided Vehicle) / AMR | 无人搬运车 / 自主移动机器人 |
| 牵引车 | tow tractor / tugger | |

### 2.2 结构部件

| 中文 | English |
|------|---------|
| 门架 | mast |
| 单级 / 两级 / 三级门架 | simplex (standard) / duplex / triplex mast |
| 全自由门架 | full free lift mast |
| 货叉 | fork / fork arm |
| 货叉架 | fork carriage |
| 挡货架 | load backrest |
| 护顶架 | overhead guard |
| 属具 | attachment(**禁译** tool / implement) |
| 侧移器 | side shifter |
| 调距叉 | fork positioner |
| 纸卷夹 | paper roll clamp |
| 软包夹 | bale clamp |
| 旋转叉 | rotating fork clamp |
| 起升油缸 | lift cylinder |
| 倾斜油缸 | tilt cylinder |
| 起升链条 | lift chain / load chain |
| 门架滚轮 | mast roller / mast bearing |
| 驱动桥 | drive axle |
| 转向桥 | steer axle |
| 驱动轮 / 承载轮 | drive wheel / load wheel |
| 实心胎 / 充气胎 | cushion (solid) tire / pneumatic tire |
| 车架 | chassis / frame |

### 2.3 动力、电池与电气

| 中文 | English |
|------|---------|
| 铅酸电池 | lead-acid battery |
| 锂电池 | Li-ion (lithium-ion) battery |
| 电池管理系统 | BMS (Battery Management System) |
| 荷电状态 / 健康状态 | SOC (State of Charge) / SOH (State of Health) |
| 充电机 | battery charger |
| 机会充电 | opportunity charging |
| 侧拉电池 | side-extraction battery / battery roller bed |
| 行走电机 / 起升电机 | traction (drive) motor / lift (hydraulic) motor |
| 电机控制器 | motor controller |
| 接触器 | contactor |
| 加速器 / 油门踏板 | accelerator pedal |
| 工作制(S2 短时 / S9 断续周期) | duty cycle (S2 short-time / S9 intermittent periodic) |
| 防护等级 | IP rating (Ingress Protection) |
| PLC / 电控平台 | PLC / CODESYS-based controller |

### 2.4 液压系统

| 中文 | English |
|------|---------|
| 齿轮泵 | gear pump |
| 多路阀 | control valve / directional control valve |
| 限速阀 / 下降限速阀 | velocity fuse / flow-regulating valve |
| 溢流阀 | relief valve |
| 液压马达 | hydraulic motor |
| 蓄能器 | accumulator |
| 属具油路 | attachment circuit / auxiliary hydraulic function |
| 液压油 | hydraulic fluid / hydraulic oil |

### 2.5 性能参数

| 中文 | English |
|------|---------|
| 额定起重量 | rated capacity / load capacity |
| 载荷中心距 | load center distance |
| 起升高度 | lift height |
| 自由提升高度 | free lift |
| 门架闭合高度 / 失载高度 | collapsed mast height / lowered mast height |
| 剩余载荷 | residual capacity |
| 载荷曲线 | load chart / capacity chart |
| 行驶速度 | travel speed |
| 爬坡度 | gradeability / gradability |
| 最小转弯半径 | minimum turning radius |
| 直角堆垛通道宽度 | right-angle stacking aisle width |
| 门架倾角 | mast tilt angle |
| 轴距 / 轮距 | wheelbase / track width |
| 最小离地间隙 | ground clearance |
| 整机重量 / 桥载荷 | service weight / axle load |
| 能耗 | energy consumption (kWh) |

### 2.6 安全、法规与标准

| 中文 | English |
|------|---------|
| 行车制动 / 停车制动 | service brake / parking brake |
| 湿式制动 | wet (oil-immersed) brake |
| 再生制动 | regenerative braking |
| 纵向 / 横向稳定性 | longitudinal / lateral stability |
| 稳定性验证 | stability verification (ISO 22915 series) |
| 倾翻 | tipover / overturn |
| 额定起重量标牌 | capacity plate / rating plate / nameplate |
| 特种设备 | special equipment (China regulatory category) |
| 场(厂)内专用机动车辆 | special-purpose motor vehicles in restricted areas |
| N1 / N2 作业人员证 | N1 / N2 operator certificate (China) |
| 定期检验 | periodic inspection |
| 载荷试验 | load test |
| GB/T 43756 叉车设计规范 | GB/T 43756 Forklift truck — Design specifications |
| GB/T 44679 叉车报废/禁用条件 | GB/T 44679 Forklift — Scrapping and prohibition criteria |
| GB/T 43657 电动叉车能耗 | GB/T 43657 Energy consumption of electric forklifts |
| ISO 3691 工业车辆安全要求 | ISO 3691 Industrial trucks — Safety requirements |
| ISO 5053-1 术语与分类 | ISO 5053-1 Industrial trucks — Terminology and classification |
| ISO 23308 能耗测量方法 | ISO 23308 Energy efficiency — Test methods |
| EN 1175 / EN 1726 | 欧标(电气 / 安全要求) |
| OSHA 29 CFR 1910.178 | 美国:动力工业车辆安全标准 |
| ANSI/ITSDF B56.1 | 美国:高起升/低起升车辆安全标准 |
| EU 2023/1230 | 欧盟机械法规(Machinery Regulation) |
| PUWER / LOLER | 英国:工作设备 / 起重设备法规 |

### 2.7 市场与商业术语

| 中文 | English |
|------|---------|
| 销量 / 出货量 | sales volume / shipments |
| 内销 / 出口 | domestic sales / exports |
| 市场份额 | market share |
| 渗透率 | penetration rate |
| 保有量 | installed base / parc |
| 同比 / 环比 | year-on-year (YoY) / month-on-month (MoM) |
| 叉车月报 | monthly forklift report |
| 二手叉车 | used forklift / pre-owned forklift |
| 经营性租赁 | operating lease / rental fleet |
| 中叉网 / 工业车辆分会(CITA) | China Forklift Association (CITA) |

---

## 三、检索通道矩阵(Retrieval Routing)

### 3.1 通道选择

| 场景 | 首选通道 | 降级通道 | 兜底 |
|------|---------|---------|------|
| 英文提问(任何类型) | **Google**<br>`https://www.google.com/search?q=<query+URL-encoded>&num=20&hl=en&gl=us` | **Bing 英文**<br>`https://www.bing.com/search?q=<query>&setlang=en&mkt=en-US` | 通用 `web_search` 工具 |
| 英文提问 + 需抓正文(标准/官网/财报) | 先 Google 定位 URL → `web_fetch` 抓该 URL 全文 | Bing 定位 → `web_fetch` | 直接 `web_fetch` 官网 |
| 中文提问 | 百度 / 必应中文 | 通用 `web_search` | — |
| 中文标准核验 | 国家标准全文公开系统 `openstd.samr.gov.cn`、工标网 `csres.com` | 见 `standard-retrieval.md` | — |
| 英文标准核验(ISO/EN/OSHA) | Google 定位 → ISO 在线 / ANSI 官网 / OSHA 官网 | `web_fetch` iso.org / osha.gov | — |

### 3.2 Google 通道的可用性说明(重要,实测结论)

> ⚠️ **实测环境结论(2026-08-31)**:从境内网络沙箱直连 `www.google.com`
> 的 HTTP 请求**连接失败**(curl 返回 HTTP 000,连接被重置);
> DuckDuckGo、Brave 同样不可达,Mojeek 返回 403。
> **Bing 英文版可用**(HTTP 200,可返回完整英文结果页)。

因此本技能对 Google 的处理是**"首选但不死等"**:

1. 英文提问时,**第一步先尝试 Google 通道**;
2. Google 不可达(连接失败 / 超时 / 返回反爬页)时,**立即自动降级到 Bing 英文版**,
   不向用户抱怨、不停下来问问题;
3. Bing 也不通时,用通用 `web_search` 工具兜底;
4. **在回答末尾如实标注本次实际使用的检索通道与检索日期**,例如:
   `Retrieved via Bing (Google unreachable from this network), 2026-08-31.`

**出境网络环境提示**:若运行环境可直连 Google(如境外主机、已配置代理),
第 1 步即可成功,无需降级。降级链路的存在只是为了让规则在无 Google 的环境里也能跑通,
而不是把"必须 Google"变成一条执行不了的死规则。

### 3.3 英文检索关键词模板

```
# Specs / 型号参数
"Hangcha XE25 specifications"  "Heli K2 series lithium battery"
"BYD 2.5 ton lithium forklift" "Linde H30 specifications"
"Toyota 8FBE15 specs"          "Jungheinrich ETV 216i reach truck specs"

# Standards / 标准
"ISO 3691-1:2020 industrial trucks safety requirements"
"ISO 22915 stability verification forklift"
"ISO 23308 energy efficiency test method"
"OSHA 1910.178 powered industrial trucks"
"ANSI B56.1 safety standard forklift"
"EN 1175 electrical requirements industrial trucks"
"GB/T 43756 forklift design specification English"

# Market / 市场
"forklift sales China 2026 CITA monthly"
"China forklift exports 2026 customs data"
"global forklift market share Toyota Kion Jungheinrich"
"lithium forklift penetration rate 2026"
"AGV AMR market 2026 warehouse automation"

# Technology / 技术
"forklift Li-ion battery BMS 80V"
"forklift hydraulic gear pump troubleshooting"
"forklift controller fault code Curtis Zapi"
"forklift mast roller replacement"

# Parts / 配件
"forklift fork carriage class 2 dimensions"
"forklift brake shoe part number"
"forklift 80V battery specification"
"forklift charger compatibility"
```

---

## 四、英文输出规范

### 4.1 单位换算(英文输出时补英制)

| 公制 | 英制 |
|------|------|
| 1 t | 2,204.6 lb |
| 1 kg | 2.205 lb |
| 1 m | 3.281 ft = 39.37 in |
| 1 mm | 0.0394 in |
| 1 kW | 1.341 hp |
| 1 MPa | 145 psi = 10 bar |
| 1 L/min | 0.264 US gpm |
| 载荷中心距 500 mm | 20 in(常见标准值) |
| 载荷中心距 600 mm | 24 in |

> 写法示例:`Rated capacity 2,500 kg (5,510 lb) at 500 mm (20 in) load center.`

### 4.2 英文输出模板(对应 SKILL.md 模板 A~H,英文提问时使用)

```
## Brand / Product
**Brand:** xxx
- Website: URL
- Parent company / Listing: xxx
- Product classes: ISO I/II/III/IV/V
- Representative models (2025-2026): xxx  [verify via web search]
- Typical applications: xxx
- Key specs: xxx  [verify via web search — do NOT fabricate]
- Source: Official website + 2025-2026 industry data
```

```
## Selection Advice
**Application:** (restate the user's operating conditions in 1-2 sentences)
- Capacity: xxx (recommendation + reason)
- Power: Li-ion / lead-acid / diesel + reason
- Class: ISO Class x + reason
- Candidate brands: xxx (2-3 options)
- Key options: xxx
- Budget range: xxx (excluding tax)
- Risks: xxx
Ref: selection-guide.md §xx
```

```
## Troubleshooting
**Symptom:** (as described by the user)
Possible causes (highest probability first):
1. xxx — Diagnosis: xxx — Action: xxx
2. xxx — Diagnosis: xxx — Action: xxx
3. xxx — Diagnosis: xxx — Action: xxx

Recommended on-site steps:
1. xxx  2. xxx  3. xxx

When to call the manufacturer: xxx
Ref: fault-diagnosis.md §xx
```

```
## Standard / Regulation
**Standard:** GB/T xxxxx-xxxx (or ISO/EN)
**Title:** xxx
**Status:** Current / Withdrawn / Not yet effective (verified online: YYYY-MM-DD)
**Effective date:** xxxx-xx-xx
**Replaces / Replaced by:** xxx (if applicable)
**Key content:** xxx (clause-level)
**Scope:** xxx
**Online verification source:** openstd.samr.gov.cn / iso.org / osha.gov
**Access:** Preview at openstd.samr.gov.cn; purchase at cssn.net.cn
Source: forklift-expert maintained by Yang Pengfei
```

### 4.3 署名(英文输出时)

统一使用英文署名,保留原始版权归属:

```
Source: forklift-expert — maintained by Yang Pengfei (杨鹏飞),
WeChat public account "叉车技术老炮" (Forklift Tech Veteran).
License: MIT — Copyright (c) 2026 杨鹏飞
```

---

## 五、常见误译警示(红线)

| ❌ 错误译法 | ✅ 正确译法 | 说明 |
|-----------|-----------|------|
| forward-moving forklift | reach truck | 前移式叉车,指门架/货叉可前移 |
| door frame / gantry | mast | 门架 |
| lifting height | lift height | 起升高度 |
| loading capacity | rated capacity / load capacity | 额定起重量 |
| center of load | load center distance | 载荷中心距 |
| tool / implement | attachment | 属具 |
| energy consumption standard (ISO 5053-1) | — | **ISO 5053-1 是术语分类标准,不是能耗标准** |
| battery management | BMS | 电池管理系统,固定缩写 |
| forklift license | operator certificate (N1/N2) | 中国为特种设备作业人员证 |
| scrapping standard | scrapping / end-of-life criteria | 报废条件 |
| explosion protection forklift | explosion-proof forklift | 防爆叉车 |
| stacker (泛指) | walkie stacker / reach stacker | 需区分:步行堆高车 vs 港口正面吊 |

---

## 六、边界

- 本模块只负责**语言与检索路由 + 术语准确性**,不改变任何原有技术结论与数据。
- 双语输出**不是**"把答案翻译两遍":默认只输出用户提问所用的那一种语言,
  除非用户明确要求 bilingual output。
- 英文输出时,数据真实性要求与中文完全一致:
  **不编造参数、不编造标准号、不报价**(沿用 SKILL.md 硬规则 1/2/12)。

---

*Copyright (c) 2026 杨鹏飞 / 微信公众号「叉车技术老炮」 — MIT License*
