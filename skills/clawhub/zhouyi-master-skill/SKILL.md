---
# 通用（ModelScope / 千问AI / QwenWork 均可解析）
name: zhouyi-master-skill
description: >-
  周易大师技能：八字测算、四柱/六爻/大六壬/奇门遁甲/紫微斗数/金口诀排盘、灵签抽签、
  情侣配对、周易起名、身份证解析、十神论命、运势图等 49 项命理功能。
  适用输入：出生年月日时分、性别、姓名、身份证号/手机号、占卜事由；
  触发词：算八字/看运势/排盘/抽签/配对/起名/测名字/黄历/解梦/称骨；
  不适用：医疗健康诊断、法律金融建议、非命理类问答。
version: 2.8.0
author: 九重居 (jiuchongju)
license: MIT

# 平台专属追加字段（按 platform 裁剪；generic 为全平台超集，各平台忽略不需要的键）
display_name: 周易大师
display_name_en: Zhouyi Master
description_zh: >-
  八字测算、运势、排盘、抽签、配对、起名、身份证解析、十神论命等 49 项功能。
description_en: >-
  Chinese metaphysics toolkit: Bazi, divination (Liu Yao/Qi Men/Zi Wei/Jin Kou Jue),
  lots, compatibility, naming, ID parsing, Ten Gods destiny, fortune charts — 49 features.
category: lifestyle-culture
allowed-tools: [bash, read]

# 保留 OpenClaw 运行契约
metadata:
  openclaw:
    requires:
      env:
        - ZHOUYI_API_KEY
      bins:
        - python3
    primaryEnv: ZHOUYI_API_KEY
    envVars:
      - name: ZHOUYI_API_KEY
        required: true
        description: 周易大师开放平台 API 密钥，在 https://iching.jiuchongju.com 注册后创建。
    homepage: https://iching.jiuchongju.com
  modelscope:
    category: other
    tags: [zhouyi, bazi, fortune, divination, chinese-metaphysics]
---

# 周易大师技能

> 本技能包为周易大师开放平台（iching.jiuchongju.com）面向公开市场发布的通用版本，
> 采用 BYOK（自带密钥）模式：包内不含任何 API-KEY，请在安装后通过环境变量
> `ZHOUYI_API_KEY` 或 `config.yaml` 注入你自己的密钥（包内已含默认共享 Key，跳过注入亦可直接使用）。
> 许可：MIT。

## 获取密钥（首次使用必读）

1. 访问 https://iching.jiuchongju.com 注册账户；
2. 在「开放平台 → API-KEY 管理」创建密钥（形如 `sk-zhouyi-...`）；
3. 密钥：包内 `config.yaml` 已内置默认共享 Key，下载即用；如需独立额度可设置环境变量 `ZHOUYI_API_KEY` 覆盖
   字段。优先级：显式参数 > 对应 `ZHOUYI_*` 环境变量 > 包内配置 > 默认值。
   密钥用 `--api-key` / `ZHOUYI_API_KEY` / `api_key`，地址用 `--base-url` / `ZHOUYI_BASE_URL` / `endpoint.base_url`。
   配置按脚本位置自动读取（不依赖工作目录，也支持 `--config`）；服务根地址兼容 `/api/`、`/api/open` 尾缀。
   免费额度 500 次/日，更高额度请到官网申请。

## 功能（49 项）

- 算命：八字测算、优生择吉、姓名测试（简/繁）、日干论命、称骨论命、企业起名、十神论命（四宫位条款，文案三语）
- 运势：桃花运、大运（10年/步）、流年、流月、流日、运势图（月运/日运/一生）
- 排盘：四柱八字、六爻、大六壬、奇门遁甲、玄空飞星、紫微斗数、金口诀
- 抽签：周公解梦、观音/吕祖/黄大仙/关帝/妈祖灵签、诸葛神数
- 情侣配对：星座、姓名、五格、生肖、血型、QQ号
- 民俗预测：黄道日历、三世财运、生男生女、号码吉凶、指纹算命、
  耳鸣/眼跳/心惊/面热/喷嚏预测、属相性格
- 起名/证件解析：周易起名（三才五格筛选）、身份证解析（18 位身份证号）

完整功能与参数见 references/function-catalog.md。

F49 运势图使用单一方法 `fortune_chart` / CLI `fortune-chart` / MCP `zhouyi_fortune_chart`，
对应 `POST /api/open/fortune/chart`。必填 `mode`、`gender`、`birthDate`、`birthTime`；
`mode` 仅 `monthly`（12 个月运点）、`daily`（14 个日运点）、`lifetime`（全部大运及流年）。
性别支持 `male/female/男/女`，出生日期 `yyyy-MM-dd`、时间 `HH:mm`；
可选 `specDate`（CLI `--spec-date` / MCP `spec_date`，`yyyy-MM-dd`），缺省当天，`lifetime` 不使用。
JSON 保留原业务字段；云端 HTML 展示评分图与完整明细，不把三种模式拆成三个功能。

能力边界注记（与移动端页面展示口径对齐）：
- F4 优生择吉为「吉日库预生成分页查询」，日期跨度最多 31 天，超范围返回范围限制提示；
- F22 周公解梦仅支持关键词检索，不含分类浏览；
- F46 周易起名如需"四季用神建议"，请先执行 `paipan --type bazi` 获取用神信息后组合使用。

## 调用方式

运行 `scripts/zhouyi_client.py <command> [args]`；部分命令通过类型参数覆盖多个功能编号，F2 为 Agent 侧对话能力（不调用 CLI）。

示例（`ZHOUYI_API_KEY` 由环境变量提供，请勿把密钥硬编码进脚本或提交到代码仓库）：

```bash
export ZHOUYI_API_KEY=你的密钥
python3 scripts/zhouyi_client.py bazi --name 张三 --gender 男 \
  --birth-date 1990-01-15 --birth-time 10:30 --save-html ./html
python3 scripts/zhouyi_client.py fortune-chart --mode monthly --gender female \
  --birth-date 1990-05-15 --birth-time 08:30 --spec-date 2026-11-20 --save-html ./html
python3 scripts/zhouyi_client.py quota
```

## 额度与费用

- 免费额度 500 次/日；更高额度请到官网 https://iching.jiuchongju.com 申请（付费按年）；
- MCP 与 Skill 共用同一开放 API，调用合并计数；超限时接口返回提示文案，请按提示处理。
- ClawHub 不支持付费技能元数据，费用规则以本节说明为准。

## 结果展示

每次调用返回可视化 HTML（与官网移动端页面同款样式），脚本自动保存到输出目录，
请向用户提供文件路径。
