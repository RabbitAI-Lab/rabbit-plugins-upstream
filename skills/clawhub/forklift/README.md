# forklift-expert — 叉车专家技能包（中英双语 v2.4）

> 作者:杨鹏飞 / 微信公众号「叉车技术老炮」 · 协议:**MIT License**
> 一句话:**问叉车,用它。中英文都行,英文提问自动走 Google 英文检索。**

---

## 一、这是什么

forklift-expert 是一个**叉车(工业车辆)领域专家技能包**,覆盖:

- 品牌/产品/型号参数(杭叉、合力、柳工、比亚迪、林德、丰田、永恒力……)
- 选型决策(吨位/动力/ISO 类别/预算)
- 技术原理(液压、门架、电池、电机、控制器)
- 故障诊断(症状 → 原因 → 处理)
- 配件/维保/二手评估
- 法规与标准(GB/T、ISO、EN、OSHA,含联网核验)
- 市场行情与销量排行(带表格和图表)

**v2.4 新增中英双语**:用户用什么语言提问,就用什么语言作答;
英文提问时检索走 **Google 英文通道**(Google 不可达自动降级 Bing 英文版)。

---

## 二、安装(三步)

### 方式 A:手动安装(推荐,适用于 CodeBuddy / WorkBuddy)

1. 解压本 zip,得到 `forklift/` 文件夹
2. 把 `forklift/` 整个文件夹放到技能目录:
   - **CodeBuddy**:`~/.codebuddy/skills/` 下(与已有技能文件夹同级)
   - **OpenClaw**:`~/.openclaw/skills/` 下
   - 其他支持 Claude Skills 规范的工具:放入配置的 skills 目录即可
3. **新开一个会话**(技能列表在会话启动时加载,当前会话不生效)

### 方式 B:ClawHub CLI 安装(OpenClaw 用户)

```bash
npm i -g clawhub
clawhub --workdir ~/.openclaw --dir skills install @yangpf6698/forklift
```

> 注意:ClawHub registry 的版本标签目前仍显示 2.0.4,但下载内容实际是 **v2.4**
> (作者发布时未同步版本号元数据)。以包内 `SKILL.md` 的 `version: 2.4.0` 为准。

---

## 三、验证装好了没有

1. 确认技能目录下有 `forklift/SKILL.md`
2. 打开新会话,提问下面任意一句,看是否触发技能:
   - `叉车怎么选型?`
   - `杭叉 XE25 参数是多少?`
   - `What's the difference between a reach truck and a counterbalance forklift?`(英文)

---

## 四、怎么用

### 触发方式

| 场景 | 示例提问 |
|------|---------|
| 中文提问 | "3吨锂电叉车选型,室内搬运,给个方案" |
| 英文提问 | "Troubleshooting: forklift mast won't lift, hydraulic pump noisy" |
| 查标准 | "GB/T 43756-2024 现在什么状态?" |
| 查销量 | "2026 年上半年国内叉车销量排行" |
| 二手评估 | "帮我看一台 2019 年的二手前移式叉车" |

技能**自动触发**,不需要手动开关。问叉车相关问题就会激活。

### 中英双语行为(v2.4)

- **中文提问** → 中文回答,走中文检索通道(百度/必应中文 + 国内权威源)
- **英文提问** → **英文回答**,走 **Google 英文通道**
- **英文术语规范**:前移式叉车 = reach truck、门架 = mast、属具 = attachment
  (不会出现"forward-moving forklift"这种字面硬译)
- 英文回答自动补英制单位,如 `2.5 t (5,510 lb)`
- 回答末尾会标注实际检索通道和检索日期

### 搜索通道与降级(实测结论,2026-08)

| 通道 | 可用性 | 说明 |
|------|--------|------|
| Google | 境内网络 ❌ | 直连失败(HTTP 000),境外/有代理 ✅ |
| Bing 英文版 | ✅ | 降级首选,实测可返回完整英文结果页 |
| 通用 web_search | ✅ | 兜底 |

英文提问时:**先试 Google → 不通自动转 Bing 英文版 → 再不行用通用搜索**。
降级是静默的,不会中断提问,但会在答案末尾如实标注。

---

## 五、更新

技能有更新时,重新解压覆盖 `forklift/` 目录即可(注意保留版权声明)。
ClawHub CLI 用户:

```bash
clawhub --workdir ~/.codebuddy --dir skills install @yangpf6698/forklift --force
```

---

## 六、常见问题

**Q:新会话里技能没生效?**
技能在会话启动时加载。装完后必须**新开一个会话**。

**Q:为什么显示版本 2.0.4?**
那是 ClawHub registry 的标签没同步,包内实际是 v2.4.0(SKILL.md 里有版本记录)。

**Q:英文提问回答却是中文?**
检查是否 v2.4 版本(看 SKILL.md 头部 version)。旧版本没有语言路由。

**Q:英文提问但查不到英文数据?**
看回答末尾标注的检索通道。境内网络 Google 不通会自动用 Bing 英文版,
结果依然是英文。若标注的是"通用 web_search",说明两个英文通道都不可用。

**Q:技能会乱报价吗?**
不会。硬规则:不报配件价格、不编造参数、不编造标准号。

---

## 七、包内容一览

| 文件 | 用途 |
|------|------|
| `SKILL.md` | 技能主文件(触发词、工作流、硬规则、输出模板) |
| `bilingual-glossary.md` | **中英术语对照 + 语言/检索路由**(v2.4 新增) |
| `brands.md` | 品牌与官网目录 |
| `standards.md` | 国标/ISO/EN/法规 |
| `standard-retrieval.md` | 标准联网检索模块 |
| `knowledge.md` | 基础知识问答 |
| `selection-guide.md` | 选型决策指南 |
| `fault-diagnosis.md` | 故障诊断手册 |
| `safety-regulation.md` | 安全/驾照/保险 |
| `market-trends.md` | 行业动态与趋势 |
| `maintenance-plan.md` | 维保计划与保养 |
| `parts-consumables.md` | 配件/易损件 |
| `used-forklift-evaluation.md` | 二手评估 |
| `sales-news.md` | 销售排行(联网+图表) |
| `wechat-articles.md` | 公众号索引(仅参考) |
| `usage-guide.md` | 给 AI/开发者看的模块技术详解 |
| `AUTHOR.md` / `LICENSE.md` | 作者信息 / MIT 协议 |
| `skill-card.md` | ClawHub 展示卡片 |

---

*Copyright (c) 2026 杨鹏飞 · MIT License · 使用时建议标注"资料来源:杨鹏飞/叉车技术老炮维护的 forklift-expert"*
