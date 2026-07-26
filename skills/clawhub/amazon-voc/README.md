# Amazon-VOC —VOC洞察 亚马逊 Amazon

Official ARI (Amazon Review Intelligence) Skill for collecting and analyzing Amazon
reviews into actionable Voice-of-Customer insights: pain points, purchase drivers, user
personas, use cases, competitor gaps, and Listing optimization ideas.

> ARI 官方 Amazon 评论采集与消费者洞察 Skill。用中文直接描述需求即可，无需理解 API
> 或编写代码；所有付费操作都会先报价，只有你明确确认后才会扣除积点。

---

## What it does / 能做什么

- 订阅 ASIN、采集评论，查看星级 / 关键词 / 趋势等免费图表数据。
- 生成 **VOC**、**深度洞察**、**趋势**、**变体**、**竞品对比** 等 AI 分析报告。
- 输出痛点、购买动因、用户画像、使用场景、改进机会与 Listing 建议。

Works in any Skill-capable AI client (e.g. Claude). Just ask in natural language:

```text
使用 amazon-review-intelligence-extractor 分析 ASIN B0XXXXXXXX，站点 amz_us，
先告诉我需要多少积点，不要直接扣点。
```

## Requirements / 前置条件

- **Python 3** (standard library only — no third-party packages).
- An **ARI API key** starting with `ari_live_`.
  Get one at <https://ari.funewa.com/zh/account?ui=d47626f#api-keys> (verify your email
  first). Top up credits at <https://ari.funewa.com/zh/billing>.

## Install / 安装

1. Copy this folder into your client's skills directory (e.g. a `skills/` dir), keeping
   the folder name `amazon-review-intelligence-extractor`.
2. Configure your API key (stored only under your local user profile):

   ```powershell
   python scripts/ari.py configure
   ```

3. Verify account + credit balance:

   ```powershell
   python scripts/ari.py check
   ```

The key is read from `ARI_API_KEY` or `~/.ari/config.json` at runtime — it is **never**
committed to this repository. 请勿把 Key 发给他人或放进公开文档。

## CLI commands / 命令

| Command | API | Consumes credits? |
|---|---|---|
| `configure` | save key locally | No |
| `check` | user + balance | No |
| `products` | list subscribed ASINs | No |
| `collect` | submit a collection task | **Yes — requires `--confirm`** |
| `status` | collection task status | No |
| `reviews` | read collected reviews | No |
| `charts` | stars / trend / keywords / flow | No |
| `quote` | analysis price quote | No |
| `analyze` | voc / insight / trend / variant / compare | **Yes — requires `--confirm`** |
| `deepdive` | product + charts + reviews + reports + VOC quote | No by default; `--confirm` to analyze |
| `reports` / `report` | list / read archived reports | No |

Run `python scripts/ari.py <command> --help` for full arguments.
Default site is `amz_us`; also supports `amz_uk / amz_de / amz_jp / amz_ca / amz_fr /
amz_es / amz_it`.

### Typical flow / 标准流程

```powershell
python scripts/ari.py products
python scripts/ari.py collect --asin B0XXXXXXXX --site amz_us --pages 3            # quote only
python scripts/ari.py collect --asin B0XXXXXXXX --site amz_us --pages 3 --confirm --wait
python scripts/ari.py deepdive --asin B0XXXXXXXX --site amz_us                     # preview + quote
python scripts/ari.py deepdive --asin B0XXXXXXXX --site amz_us --confirm           # generate VOC
```

## Billing safety / 扣费保护

采集和 AI 分析都会消耗积点。付费命令（`collect`、`analyze`、付费 `deepdive`）**必须**
显式追加 `--confirm` 才会真正执行 —— 不带 `--confirm` 时只返回报价。请在明确告知并得到
用户确认后再扣点，禁止替用户默认确认。

## Repository layout / 目录结构

```
SKILL.md              # Skill manifest + operating instructions (skill 指令)
使用说明.md            # End-user guide in Chinese (中文使用指南)
scripts/ari.py        # Standard-library CLI (采集与分析命令行)
references/reference.md# CLI & API reference (命令 / 字段 / 错误码)
agents/openai.yaml    # Agent interface metadata
```

## Links / 常用入口

- API Key: <https://ari.funewa.com/zh/account?ui=d47626f#api-keys>
- Billing / 充值套餐: <https://ari.funewa.com/zh/billing>
- Products / 产品管理: <https://ari.funewa.com/zh/products>
- Reports / 报告中心: <https://ari.funewa.com/zh/reports>
