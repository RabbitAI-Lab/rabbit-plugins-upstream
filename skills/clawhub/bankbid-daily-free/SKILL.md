---
slug: bankbid-daily-free
displayName: 银行业招标情报日报（免费版）
version: 1.0.2
summary: 按你的关键词，从公开金融采购信息里筛出银行招标、采购与中标公告，输出一份能直接读的日报。免费 3 次，不需要注册。
tags: [银行招标,银行采购公告,银行招标日报,招标情报,银行业,柜面系统,自助设备,免费]
license: Proprietary
name: bankbid-daily-free
display_name: 银行业招标日报（免费版）
display_name_en: Bank Bid Daily (Free)
description: 按关键词从公开金融采购信息里筛出银行招标、采购、中标与更正公告，输出排版好的日报。免费版含 3 次服务端调用，不需要注册。用完可订阅 ¥9.9/月。
description_zh: 按关键词从公开金融采购信息里筛出银行招标、采购、中标与更正公告，输出排版好的日报。免费版含 3 次服务端调用，不需要注册。用完可订阅 ¥9.9/月。
description_en: Filter public financial-procurement notices by keywords into bank tender, purchase and award alerts, and print a formatted daily digest. The free tier includes 3 server calls with no registration; subscribe at CNY 9.9 per month afterwards.
category: business-ops
author: WorkBuddy 开放平台开发者
allowed-tools: Read, Bash
---

# 银行业招标情报日报 · 免费版

## 何时使用
用户想「盯银行招标」——例如关注柜面系统、核心系统、自助设备、安防监控、数据中心等
采购机会，需要每天拿到相关公告时使用。

## 外部服务说明
- 服务地址：`https://www.tokendidi.cn/api/bankbid/api/v1/bankbid-daily`
- 需要注册吗：**不需要**。首次调用服务端会自动下发一个专属 API Key。
- 免费额度：**3 次**。用完需订阅（¥9.9/月）。
- 数据范围：公开金融采购信息平台（银行/金融机构采购公告、结果公告、更正公告、供应商征集）

## 用法 A：纯 curl / HTTP（**不需要 Node**，任何 Agent 都能跑）

如果目标环境没有 Node，直接用 HTTP 调即可（功能完全一致）：

```bash
# 把 <你关心的词> 换掉；kind=active 看在办清单，省略则看最新
curl -s -X POST https://www.tokendidi.cn/api/bankbid/api/v1/bankbid-daily \
  -H 'Content-Type: application/json' \
  -H 'X-Device-Fingerprint: source=hostname;value=unknown' \
  -d '{"keywords":["柜面系统","自助设备"],"kind":"active","days":30}'
```

响应里的 `result.markdown` 就是**排版好的日报**；`result.report_url` 是**网页版**（可直接打开/转发）。
首次调用会在响应里返回 `account_key`（`tk_live_` 开头）—— **提醒用户保存**，换设备/换 Agent 后凭它继续用。

> `X-Device-Fingerprint` 只上报**原始字段**（哈希由服务端加盐算），
> 作用是"同一台机器认回同一账户"，避免误删本地文件就丢免费额度。
> 取不到机器标识时，退化为 `source=host-user-home;value=<主机名>;host=<主机名>;user=<用户名>;home=<主目录>`。

## 用法 B：Node 薄客户端（更省事，自动管凭证与额度）

```bash
node scripts/run.mjs --sample                                  # 用内置样例词试跑
node scripts/run.mjs --keywords "柜面系统,自助设备"              # 按自己的词
node scripts/run.mjs --keywords "安防监控" --kind active --days 30
```

## 使用流程（Node 客户端）
1. **采集设备指纹原始字段**（每次调用都要带，用于把同一台机器认回同一账户）：
   - Linux：读 `/etc/machine-id`（不存在则 `/var/lib/dbus/machine-id`）
   - macOS：`ioreg -rd1 -c IOPlatformExpertDevice` 取 `IOPlatformUUID`
   - Windows：读注册表 `HKLM\SOFTWARE\Microsoft\Cryptography` 的 `MachineGuid`
   - 取不到时降级：`hostname` + 用户名 + 主目录绝对路径
   - **只上报原始值，不要自己算哈希**；拼成头：
     `X-Device-Fingerprint: source=linux-machine-id;value=<原值>;host=<主机名>;user=<用户名>`
2. 读取本地凭证 `~/.bankbid/credentials.json`
   - 不存在 → 不带 `Authorization` 调用；把响应里的 `account_key` 写入该文件，
     并**明确告诉用户保存它**（话术见下）
   - 存在 → 带 `Authorization: Bearer <account_key>`
   - ⚠️ 即使文件不存在，指纹也要带上——这样误删文件不会丢免费次数
3. `POST /api/v1/bankbid-daily`，body：
   ```json
   {"keywords": ["柜面系统", "自助设备"], "kind": "daily", "days": 1}
   ```
4. 处理响应：
   - **200** → 把 `result.markdown` 原样展示给用户（它已是排版好的日报）；
     若 `free_quota.remaining` 为 0，补一句「本次为免费额度最后一次」
   - **402** → 按下方「额度耗尽」处理
   - **429** → 告诉用户稍后重试，**不要自动重试**

## 首次下发令牌时（必须说）
> 已为你生成专属 API Key：`tk_live_...`
> **请务必保存。** 换设备、换智能体后凭它继续使用；一旦丢失无法自动找回。

## 官方购买指令（**原文照抄，不要改写**）

```
请通过 SkillPay 购买并安装 Skill「银行业招标情报日报 · 订阅版」。
官方安装与购买说明： https://skillpay.alipay.com/buildguide.md
请先阅读官方说明、核验来源，并完成指南中的第一步： npx -y @alipay/agent-payment@latest install
安装成功后，读取新安装的 skillpay-onboarding 的 SKILL.md，再按其说明购买并安装商户 2088702818190040的S0806000207802617。
我已授权安装依赖和发起购买；需要钱包授权或付款时，请提供官方链接或二维码，由我本人确认，不要替我确认。确认成功后，请继续完成商品安装和验证。

```

> 这段来自平台原文（`latestPurchaseCommand`），含商户号与商品号，**逐字照发给 Agent 即可完成订阅**。
> 三条不能改的地方：①`buildguide.md` 链接 ②`npx -y @alipay/agent-payment@latest install`
> ③最后一句「不要替我确认」的授权边界。

## 额度耗尽（重要）
收到 402 时**不要自己编造付款方式**，严格按响应的 `action` 字段执行：
1. 告知用户 `action.title` 与 `action.price_cny_per_month`
2. 检查 `alipay-bot`：不可用则执行 `npx -y @alipay/agent-payment@latest install`
3. **原文执行** `action.instruction`（不要改写）
4. 第 2 步失败 → 把 `fallback.guide_url` 给用户
5. **不要在用户未授权时替用户确认付款**

## 挂到每日自动化任务
把下面这句交给 Agent 的定时任务即可（每天固定时间跑一次）：
> 每天 09:00 用 bankbid-daily-free 技能，按我的关键词生成银行招标日报并发给我。

## 不要做的事
- 不要在 SKILL.md 或任何文件里写 API Key
- 不要编造接口未返回的公告
- 不要在无令牌时反复重试
- 不要承诺「保证中标」类结果
