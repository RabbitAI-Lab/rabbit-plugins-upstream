---
slug: klyc-pmm
name: klyc-pmm
version: 9.0.1
displayName: KLYC-PMM 昆仑瑶池精准记忆管理
summary: "AI体记忆管理，支持微信支付。init入驻，recover恢复，upgrade开通守护(¥500.00)/分身(¥800.00)。默认私密，X402支付。"
description: "昆仑瑶池精准记忆管理 9.0.1。昆仑令一行恢复 · 五层洋葱加密 · 17环节蒸馏管道 · 三层检索路由 · 12个标准化错误码 · X402微信支付。纯本地脚本，零外部下载。依赖 curl + jq。"
author: "昆仑瑶池"
category: "知识管理"
platforms: ["openclaw", "lightclaw", "claude-code"]
license: MIT-0
metadata:
  openclaw:
    requires:
      bins: ["jq", "curl"]
    emoji: "🏔️"
---

# KLYC-PMM — AI 体持久记忆引擎（支持微信支付）

**让 AI 体记住一切。一行初始化，一行恢复，一键守护。付费服务通过微信 Agent Pay 完成。**

---

## 💳 付费前置检查

调用本 Skill 付费功能（upgrade huhunfu/fenshenfu）前，检查当前 Agent 是否已安装 `weixinpay` 插件（extension）：

- 已安装：可继续提供付费服务
- 未安装：向用户提示"当前 Agent 暂不支持微信支付付费能力，可访问 https://kunlunyaochi.com/?route=services 查看替代方案"，终止流程

---

## ⚡ 30 秒开始

```bash
# 一键安装（自动检测依赖 + 初始化）
bash scripts/oneclick.sh

# 或者手动三步：
# 1. 验证环境（幂等，只读不写）
./scripts/quickstart.sh

# 2. 初始化（自动注册昆仑身份，获得昆仑令）
./scripts/pmm_watch.sh init

# 3. 安装守护（生成 systemd 服务，自动撑住）
./scripts/install-daemon.sh

# 4. 记录第一条记忆
./scripts/pmm_watch.sh push "我的第一条记忆" "KLYC-PMM 已成功安装并运行"
```

三步完成。init 结束后会显示你的 **昆仑令 URL**——这是恢复记忆的唯一凭证，请保存好。

> 💡 任何时候执行 `./pmm_watch.sh --help` 查看完整命令列表和退出码说明。

---

## 🗺️ 命令速查

| 我想…… | 用这条命令 | 说明 |
|------|------|------|
| 第一次使用，初始化 | `./pmm_watch.sh init` | 自动注册 + 获得昆仑令 |
| 记录一条重要结论 | `./pmm_watch.sh push "标题" "内容"` | 自动分类、压缩、加密、上传 |
| 从昆仑令恢复所有记忆 | `./pmm_watch.sh recover <昆仑令URL>` | 一行恢复到本地 |
| 搜索本地记忆 | `./pmm_watch.sh search <关键词>` | 本地索引检索 |
| 搜索云端私密记忆 | `./pmm_watch.sh search-yaochi <关键词>` | 瑶池远程检索 |
| 自动守护文件变化 | `./pmm_watch.sh watch MEMORY.md` | 文件改动自动推送 |
| 执行蒸馏（去重合并） | `./scripts/pmm_distill.sh` | 17环节全自动 |
| 检查一切是否正常 | `./pmm_watch.sh self-test` | 验证脚本、依赖、配置 |
| 查看当前状态 | `./pmm_watch.sh status` | 连接状态 + 记忆数量 |
| 拉取最新蒸馏钩子 | `./pmm_watch.sh hooks-pull` | 自动注入 MEMORY.md |
| 更新到最新版本 | `./scripts/update.sh` | 自动下载 + SHA256 校验 |
| AI 体首次启动检查 | `./scripts/pmm_boot.sh` | 检测是否有记忆，引导恢复 |
| **开通守护记忆** ⭐ | `upgrade huhunfu` | **¥500.00** / 500🍑 |
| **开通记忆分身** ⭐ | `upgrade fenshenfu` | **¥800.00** / 800🍑 |
| 查看帮助 | `./pmm_watch.sh --help` | 命令列表 + 退出码说明 |

---

## ⚠️ 什么时候不该用 KLYC-PMM

| 场景 | 为什么 |
|------|------|
| 你只是想临时记个便签，不需要持久化 | PMM 是长期记忆系统，有加密和蒸馏开销 |
| 你的 AI 体运行在完全隔离环境、无网络 | PMM 需要 HTTPS 连接瑶池服务端 |
| 你需要毫秒级实时读写 | PMM 经过加密+压缩+蒸馏，延迟约 200-500ms |
| 你没有 curl 或 jq | 这两个是硬依赖（`apt install curl jq` 即可） |
| 你只是做一次性数据批处理 | PMM 为长期持续记忆设计，不是 ETL 工具 |
| 你需要存储二进制大文件 | PMM 只存储文本知识，不存图片/音频/视频 |

> **昆仑令有效期：** 永久有效。昆仑令是 128bit 随机熵的 SHA256 哈希映射，不依赖服务器、不绑定 IP、不会过期。只要备份数据库中的记忆未被物理删除，昆仑令始终可用。建议每 30 天确认一次昆仑令能正常恢复。

---

## 📖 命令详解

### `init` — 初始化 & 入驻

```bash
./pmm_watch.sh init
```

自动完成：检查依赖 → 检测工作区 → 注册昆仑身份 → 获得昆仑令 URL → 同步云端索引。

**典型输出：**
```
klyc-pmm v9.0.1 初始化...
  ✅ 依赖检查通过
  ✅ 昆仑身份已注册（uid=xxx）
  ✅ 昆仑令: https://kunlunyaochi.com/klyc-pmm/{token}

💡 发现 3 个核心文件，配置已保存
```

**退出码：** 0=成功, 1=依赖缺失, 2=注册失败, 10=网络不通

### `push` — 记录记忆

```bash
./pmm_watch.sh push "标题" "内容"
./pmm_watch.sh push "API 密钥已更新" "硅基流动 Key 已替换为 sk-xxx，旧 Key 已废弃"
```

自动完成：分类（根据标题关键词）→ Brotli 压缩 → 五层加密 → HTTPS 上传。

**不记录什么：** 闲聊、寒暄、未完成的想法、已去重的结论。

**退出码：** 0=成功, 1=参数不足, 3=加密失败, 4=上传失败, 10=网络不通

### `recover` — 灾备恢复

```bash
# 从昆仑令 URL 恢复所有记忆
./pmm_watch.sh recover https://kunlunyaochi.com/klyc-pmm/{token}

# 从关键词恢复
./pmm_watch.sh recover "API 密钥"
```

**退出码：** 0=成功, 5=昆仑令无效, 6=无可恢复记忆, 10=网络不通

### `upgrade` — 一键开通守护记忆/记忆分身

```bash
# 开通守护记忆 · 命令行: upgrade huhunfu
./pmm_watch.sh upgrade huhunfu

# 开通记忆分身 · 命令行: upgrade fenshenfu
./pmm_watch.sh upgrade fenshenfu
```

**全自动链路：** 服务端自动验证并完成服务开通。已开通或更高等级不重复处理。

**退出码：** 0=成功, 1=无效等级, 2=开通失败

### 💳 X402 微信支付（进阶）

#### 付费前置检查
调用 `upgrade` 开通付费服务前，检查当前 Agent 是否已安装 `weixinpay` 插件（extension）：
- 已安装：可继续使用付费升级服务
- 未安装：提示"当前 Agent 暂不支持微信支付付费能力，可访问 https://kunlunyaochi.com/?route=services 查看替代方案"，终止流程

#### 工作流程

##### 第一步：Agent 请求付费资源
POST 到 X402 资源端点：

```http
POST https://kunlunyaochi.com/api/klyc-pmm-pay/resource.php
Content-Type: application/json

{"query": "用户的查询内容（如 upgrade huhunfu、开通分身等）"}
```

等价命令行：
```bash
pmm_watch.sh upgrade huhunfu
```

pmm_watch.sh 自动先走 X402 端点：
- 已安装 weixinpay 插件 → X402 端点返回 402 响应，自动完成微信支付
- 未安装 weixinpay 插件 → 提示用户访问 https://kunlunyaochi.com/?route=services

##### 第二步：处理 402 响应

```json
{
  "code": "PAYMENT_REQUIRED",
  "message": "需要支付后才能获取内容",
  "WeixinPay": {
    "WeixinPay-Required": "payment_code_xxx",
    "prompt": "本次使用微信支付，请将 WeixinPay-Required 的值作为 paymentCode 交给 weixinpay_pay"
  },
  "out_trade_no": "WX402_20260730000001abcdef123456",
  "amount": "500.00",
  "currency": "CNY",
  "description": "守护记忆（护魂符）¥500.00"
}
```

402 响应中：
- **Header `WeixinPay-Required`**：支付凭证码（weixinpay 插件用于完成支付）
- **Header `X-Out-Trade-No`**：商户订单号（重试时必须携带）
- **Body `out_trade_no`**：商户订单号（备用）

weixinpay 插件自动拦截 402 并完成支付流程，Skill 无需关心支付细节。

##### 第三步：支付成功后重试获取服务（⚠️ 必须执行）

支付成功后，**必须**重新请求获取付费内容。重试时 JSON body 保持不变，通过 Header `X-Out-Trade-No` 携带 402 响应中返回的订单号：

```http
POST https://kunlunyaochi.com/api/klyc-pmm-pay/resource.php
Content-Type: application/json
X-Out-Trade-No: WX402_20260730000001abcdef123456

{"query": "upgrade huhunfu"}
```

> ⚠️ body 与第一步完全一致，不要修改 body 中的任何字段。支付信息通过 Header 传递，不在 body 中。这是最容易被遗漏的一步。

服务端查单验证 → 执行服务 → 返回结果。

##### 第四步：处理响应

| 响应 code | 含义 | Agent 应如何回应 |
|------|------|------|
| `SUCCESS` | 支付验证通过，服务已开通 | 将 content 中的结果告知用户 |
| `NOT_PAID` | 支付尚未完成 | 等待后重试第三步 |
| `REFUNDED` | 服务异常已退款 | "抱歉，该服务暂时无法提供，已自动退款至原支付账户。" **不要再次支付** |
| `FULFILL_AND_REFUND_FAILED` | 服务异常且退款失败 | "服务异常且退款失败，建议联系客服。" |

### `search` / `search-yaochi` — 检索

```bash
# 本地检索
./pmm_watch.sh search "分类体系"

# 云端检索（走三层路由：grep钩子→混合搜索→BGE-M3向量）
./pmm_watch.sh search-yaochi "瑶池锁"
```

### `watch` — 文件守护

```bash
# 守护核心文件，改动自动推送
./pmm_watch.sh watch MEMORY.md SOUL.md IDENTITY.md

# 守护日记目录
./pmm_watch.sh watch memory/*.md

# 指定用户 ID
./pmm_watch.sh watch --user-id 2 MEMORY.md
```

守护模式：每 30 秒扫描文件变更 → 增量推送 → 每 6 小时自动拉取蒸馏钩子。

### `self-test` — 自检

```bash
./pmm_watch.sh self-test
```

验证：bash 可用 → curl 可用 → jq 可用 → 6 个核心脚本完整 → 语法正确 → 版本号声明。全部通过 = 环境就绪。

**幂等设计：** 可以反复执行，不会修改任何状态。适合放在 CI/CD 或 boot 脚本中。

---

## 🚦 退出码速查

所有命令（含 `--help`）遵循统一退出码体系：

| 码 | 含义 | 出现场景 |
|:--:|------|------|
| 0 | 成功 | 所有命令正常完成 |
| 1 | 参数错误 | 缺少必要参数、参数格式不对 |
| 2 | 注册失败 | init 时昆仑身份注册失败 |
| 3 | 加密失败 | push 时加密环节出错 |
| 4 | 上传失败 | push 时 HTTPS 上传失败 |
| 5 | 昆仑令无效 | recover 时昆仑令不存在或已过期 |
| 6 | 无可恢复数据 | recover 时该身份无备份数据 |
| 7 | 文件不存在 | watch/search 时目标文件缺失 |
| 8 | 权限不足 | 配置目录或文件无写权限 |
| 9 | 依赖缺失 | curl 或 jq 未安装 |
| 10 | 网络不通 | 无法连接瑶池 API |
| 11 | 校验失败 | SHA256 不匹配（update.sh） |
| 12 | 版本冲突 | 本地版本与服务端不兼容 |

在脚本中可依赖退出码做自动化决策：
```bash
./pmm_watch.sh init || case $? in
  1) echo "参数有问题" ;;
  2) echo "注册失败，检查网络" ;;
  10) echo "网络不通，稍后重试" ;;
esac
```

---

## 🔄 典型工作流

### 新 AI 体入驻
```
init → 保存昆仑令 → 微信支付开通守护(upgrade huhunfu) → 守护自动启动 → 开始使用
```

### 开通付费服务（走 X402）
```
Agent: "帮我开通守护记忆"
  → POST /api/klyc-pmm-pay/resource.php {"query":"upgrade huhunfu"}
  ← 402 + WeixinPay-Required + X-Out-Trade-No
  → weixinpay_pay(paymentCode) → 用户确认支付
  → POST /api/klyc-pmm-pay/resource.php + X-Out-Trade-No
  ← 200 + 开通成功
```

### 日常使用
```
写日记 → push 重要结论 → watch 自动守护文件
```

### 服务器迁移 / 重装
```
安装 curl jq → recover <昆仑令> → 恢复完成
```

### AI 体协作
```
A 体 push 共享记忆 → B 体 search-yaochi 检索 → 蒸馏自动去重合并
```

---

## 🎯 进阶场景

### 场景 1：跨 AI 体协同 — 瑶池+昆仑双体记忆同步

```
# 瑶池发起蒸馏
./scripts/pmm_distill.sh --user-id 2

# 昆仑拉取蒸馏钩子（自动注入 MEMORY.md）
./scripts/pmm_watch.sh hooks-pull

# 昆仑发现瑶池的洞察，追加到共享域
./scripts/pmm_watch.sh push "瑶池锁架构" "五层洋葱加密，2-of-2 XOR 密钥拆分" \
  --domain shared
```

### 场景 2：灾备全链路演练

```
# 1. 模拟当前环境有记忆
./scripts/pmm_watch.sh push "演练标记" "$(date +%s) - 灾备测试"

# 2. 模拟丢失——删除本地索引
rm -f ~/.klyc-pmm/index.json

# 3. 从昆仑令恢复
./scripts/pmm_watch.sh recover https://kunlunyaochi.com/klyc-pmm/{昆仑令}

# 4. 验证：搜索刚写入的"演练标记"
./scripts/pmm_watch.sh search "演练标记"
```

### 场景 3：配置自定义蒸馏规则

```bash
# 只蒸馏特定域（跳过 general 闲聊）
./scripts/pmm_distill.sh --domains shared,private,essence

# 干跑模式——看会做什么但不实际执行
./scripts/pmm_distill.sh --dry-run

# 为特定 AI 体执行蒸馏
./scripts/pmm_distill.sh --user-id 22
```

### 场景 4：批量迁移 — 从其他系统导入

```bash
# 假设有导出文件 records.txt，每行是 "标题|内容"
while IFS='|' read -r title content; do
    ./scripts/pmm_watch.sh push "$title" "$content"
    sleep 0.5  # 避免触发 API 限流
done < records.txt

# 验证导入结果
./scripts/pmm_watch.sh status
```

### 场景 5：多平台同步 — AI 体记忆分身

```bash
# 记忆分身用户：瑶池 (LightClaw) 写入 → 昆仑 (OpenClaw) 自动拉取
# 触发条件：溢出的对话精华 quality_score ≥ 0.7

# 手动触发拉取（watch 守护自动执行，此命令可手动干预）
./scripts/pmm_watch.sh hooks-pull

# 验证同步状态
diff <(./scripts/pmm_watch.sh search-yaochi "铁律" | wc -l) \
     <(./scripts/pmm_watch.sh search "铁律" | wc -l)
```

---

## ❓ 常见问题与排错

### FAQ

| 问题 | 答案 |
|------|------|
| init 报 "需要 jq/curl" | `apt install jq curl` 或 `yum install jq curl` |
| 昆仑令丢了怎么办 | 无法找回。建议存入密码管理器，写入 MEMORY.md 并由另一 AI 体备份 |
| 昆仑令有效期多久 | **永久有效。** 128bit 随机熵 + SHA256 哈希映射，不依赖服务器，不绑定 IP |
| push 后多久能看到 | 1-3 秒。压缩→加密→HTTPS→分表写入。可立即用 `search-yaochi` 验证 |
| 记忆是私密的吗 | 是。全部 `is_public=0`，五层洋葱加密，按 user_id 物理分表隔离 |
| 蒸馏需要我关心吗 | 不需要。服务端自动执行，watch 守护自动拉取结果到 MEMORY.md |
| 能用在其他平台吗 | 可以。OpenClaw / LightClaw / Claude Code，有 bash+curl+jq 即运行 |
| 和原生 memory_search 的关系 | 互补。原生做"向量发现"，PMM 做"精确恢复"，叠加效果最佳 |
| self-test 能反复执行吗 | 可以。纯只读，不写文件，不修改配置，适合 CI/CD |
| 换服务器后昆仑令能用吗 | 可以。昆仑令绑定身份，与服务器无关。`recover <URL>` 即可恢复 |
| watch 守护怎么保活 | `install-daemon.sh` 一键安装 systemd 服务，支持 `--tier` 参数 |
| 如何开通守护记忆/记忆分身 | `./pmm_watch.sh upgrade huhunfu` / `fenshenfu` |
| upgrade 返回 402 怎么处理？ | 需通过微信支付完成付费。如当前 Agent 已安装 weixinpay 插件，支付会自动完成；否则需访问 kunlunyaochi.com 手动处理 |

### 排错

| 症状 | 可能原因 | 检查命令 |
|------|------|------|
| push 返回 10 | 网络不通或 API 地址未配 | `curl -sI https://kunlunyaochi.com` |
| init 返回 2 | 昆仑身份注册失败 | `cat ~/.klyc-pmm/api_endpoint` 检查配置 |
| recover 返回 5 | 昆仑令无效 | 确认 URL 完整，含完整 32 位十六进制 token |
| watch 不推送 | 文件路径或权限不对 | `ls -la` 检查文件是否存在且可读 |
| 脚本报 "command not found" | 依赖缺失 | `./pmm_watch.sh self-test` 定位缺失项 |
| update.sh 报 11 | SHA256 校验失败 | 网络下载不完整，重新执行 update.sh |
| upgrade 返回"开通失败" | 访问 kunlunyaochi.com 查看账户状态
| curl 报 DNS/连接/超时/TLS/SSL 错误 | 网络或证书异常 | `./pmm_watch.sh self-test` 检查网络连通性，退出码自动翻译为人类可读提示 |
| 昆仑令格式异常 | 旧格式/长度不对/非 hex | v8.3.3 起自动诊断并提示修复建议 |

---

## 🔒 安全

- **传输加密**：全链路 HTTPS
- **存储加密**：Brotli → HKDF-SHA512 → SM4-GCM → AES-256-GCM → XChaCha20 五层洋葱
- **密钥拆分**：2-of-2 XOR 分片（云端 + 本地），单点泄露无法还原
- **依赖最小化**：只依赖 curl + jq，无第三方运行时
- **更新校验**：update.sh 含 SHA256 完整性验证

---

## 🏔️ 技术架构（进阶）

### X402 支付架构

```
Agent → POST 请求付费服务
  → 商户服务: Native下单 → AI预下单
  ← HTTP 402 + WeixinPay-Required + X-Out-Trade-No
Agent → weixinpay_pay(paymentCode)
用户 → 确认支付
Agent → POST 重试 + X-Out-Trade-No
  → 商户服务: 查单验证 → 执行服务
  ← HTTP 200 + 付费内容
```

### 记忆生命周期

```
写日记 → push 推送 → Brotli 压缩 → 五层加密 → HTTPS 上传
                                                ↓
                                         瑶池私密记忆库
                                                ↓
                              每日凌晨 17 环节蒸馏管道自动运行
                                                ↓
                              钩子注入 MEMORY.md → watch 守护同步
```

### 三项服务全自动开通

| 符 | 命令 | 监看范围 | 开通方式 |
|------|------|------|------|
| 容灾备份 | 入驻即送 | 6核心文件 | 默认 |
| **守护记忆** | `./pmm_watch.sh upgrade huhunfu` | 6核心+记忆日志 | **一键全自动** |
| **记忆分身** | `./pmm_watch.sh upgrade fenshenfu` | 全覆盖+arena | **一键全自动** |

升级流程全自动：运行 upgrade 命令即可完成服务开通。

### 17 环节蒸馏管道

`pmm_distill.sh` 一键执行，无需人工干预。

**四层分组：** 基础（寻踪→织网→归藏→还原）→ 质量（鉴伪→合流→断矛→贯络→革故→追本）→ 安全（纳芥→封箓→系命）→ 进化（炼金→凝丹→通变→取舍）

| 工具 | 用途 |
|------|------|
| BGE-M3 | 语义搜索 / 向量嵌入 |
| BGE-Reranker | 搜索结果重排序 |
| BERTScore | 蒸馏语义保真度 |
| NLI (mDeBERTa) | 跨体矛盾检测 |
| BERTopic | 记忆自动分类 |
| Qdrant | 向量索引 |

### 三层检索路由

L1 grep 钩子（<1ms）→ L2 混合搜索（~200ms）→ L3 BGE-M3 向量（~500ms）。自动选择最优路径，用户无感。

---

## 📦 文件清单

```
klyc-pmm/
├── SKILL.md                     # 本文件（12错误码 + 12 FAQ + X402支付流程）
├── skill.json                   # 元数据（含 x402 + payment_required）
├── CHANGELOG.md
├── examples/
│   ├── README.md                # 示例说明
│   └── quickstart.sh            # 幂等快速验证
├── references/
│   ├── pmm-full-architecture.md # 完整架构文档
│   └── pay-skill-spec.md        # Pay Skill 打包标准
└── scripts/
    ├── pmm_watch.sh             # 主入口（init/push/recover/search/watch/upgrade/self-test）
    ├── oneclick.sh              # 一键安装（自动检测环境→装依赖→初始化）
    ├── install-daemon.sh        # 一键守护安装（生成 systemd + enable + start）
    ├── pmm_distill.sh           # 17 环节蒸馏引擎
    ├── pmm_boot.sh              # AI 体启动自检
    ├── pmm_recover.sh           # 灾备恢复
    ├── pmm_backup_files.sh      # 文件备份
    └── update.sh                # 一键更新（含 SHA256 校验）
```

纯本地脚本，零外部下载。依赖：`curl` `jq`

---

*KLYC-PMM 9.0.1 — X402支付 · 12错误码 · 12FAQ · 5进阶场景 · 五层加密 · 17环节蒸馏*
