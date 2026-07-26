---
slug: "aegis-security-free"
name: "aegis-security-free"
version: 1.0.1
displayName: "区块链安全基础版"
summary: "基础区块链安全API，地址声誉检查和代币蜜罐检测"
license: "MIT"
description: |-
  面向AI代理的区块链安全API免费版。提供地址声誉检查、代币蜜罐检测和免费额度查询等基础功能，
  支持Ethereum和Base链。适用于基础交易前安全检查场景。升级至完整版可解锁交易模拟、
  x402付费机制和8条链全链支持.
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 安全合规

---
# 区块链安全防护（免费版）

面向AI代理的区块链安全API免费版，提供基础的交易前安全扫描能力。每日100次免费检查额度，支持Ethereum和Base链的地址声誉检查和代币蜜罐检测.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 区块链安全基础版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 安全策略

- 仅限手动调用，禁止自动触发敏感操作
- 禁止请求或存储私钥、助记词、种子短语
- 免费版仅支持只读安全检查，不涉及付费交易操作
- 本skill无需额外环境变量

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 1. 地址声誉检查

通过 `GET /v1/check-address/:address` 端点检查接收地址的链上声誉。传入地址路径参数和 `chain_id` 查询参数（免费版支持1=Ethereum和8453=Base），返回 `isSafe` 布尔值、风险等级（LOW/MEDIUM/HIGH/CRITICAL）和威胁信号列表。适用于转账前验证收款方是否为已知恶意地址.
### 2. 代币蜜罐检测
通过 `GET /v1/check-token/:address` 端点检测代币合约是否存在蜜罐行为。传入代币合约地址和 `chain_id`（免费版支持1和8453），返回蜜罐概率百分比、风险评估和具体风险信号（如买入税率过高、卖出暂停等）。适用于购买新代币前的风险评估.
**输入**: 用户提供代币蜜罐检测所需的指令和必要参数.
**处理**: 解析代币蜜罐检测的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 3. 免费额度查询

通过 `GET /v1/usage` 端点查询当前指纹的免费配额使用情况。通过 `X-Client-Fingerprint` 头部识别用户身份，返回 `dailyLimit`（100次/天）、`usedToday`、`remainingChecks` 和 `nextResetAt`（UTC时间戳）。适用于配额监控和调用规划.
### 4. 风险等级评估

根据检查结果自动计算综合风险等级。`LOW` 表示次要风险可放行，`MEDIUM` 表示存在部分风险需人工复核，`HIGH` 表示显著风险需阻止并确认，`CRITICAL` 表示恶意或不安全必须阻止。每个响应包含 `isSafe` 布尔值和详细威胁信号列表。适用于基础安全决策.
#
## 升级提示

以下为完整版（aegis-security）独有功能，免费版不可用：

- **交易模拟**：`POST /v1/simulate-tx` 端点在链下环境中模拟交易执行，预测合约交互结果
- **x402付费机制**：超出免费额度后自动付费续用，支持USDC在Base或Solana上微额支付
- **全链支持**：支持Polygon(137)、Arbitrum(42161)、Optimism(10)、BSC(56)、Avalanche(43114)和Solana
- **反馈提交**：`POST /v1/feedback` 端点提交问题报告，支持requestId关联追踪

升级至完整版以获取全部能力.
## 使用流程

1. 在所有请求中设置 `X-Client-Fingerprint` 头部为稳定的用户标识，确保免费配额稳定分配
2. 调用 `GET /v1/usage` 检查剩余免费配额，规划当日调用次数
3. 交易前并行执行：`GET /v1/check-address/:to` + `GET /v1/check-token/:token`
4. 根据风险等级决策：LOW允许放行，MEDIUM提示用户复核，HIGH/CRITICAL阻止交易并解释风险
5. 免费额度用尽后，等待UTC次日0点重置或升级至完整版启用x402付费

#
## 示例

### 示例1：检查Base链地址安全性

```bash
# 查询免费额度
curl "https://security-api.example.com/v1/usage" \
  -H "X-Client-Fingerprint: agent-default"
# ...
# 响应
# {
#   "freeTier": {
#     "enabled": true,
#     "dailyLimit": 100,
#     "usedToday": 2,
#     "remainingChecks": 98,
#     "nextResetAt": "2026-02-11T00:00:00.000Z",
#     "resetTimezone": "UTC"
#   },
#   "_meta": { "requestId": "uuid-xxx", "tier": "free", "latencyMs": 4 }
# }
# ...
# 检查Base链上的地址安全性
curl "https://security-api.example.com/v1/check-address/0x742d35Cc6634C0532925a3b844Bc454e4438f44e?chain_id=8453" \
  -H "X-Client-Fingerprint: agent-default"
```

### 示例2：检测Ethereum链上代币蜜罐

```bash
curl "https://security-api.example.com/v1/check-token/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48?chain_id=1" \
  -H "X-Client-Fingerprint: agent-default"
# ...
# 响应包含 honeypot概率、riskLevel、threatSignals 等字段
```

## 错误处理

| 错误场景 | HTTP状态 | 原因 | 处理方式 |
|---:|---:|---:|---:|
| 免费额度耗尽 | 402 | 当日100次免费配额已用完 | 等待UTC次日0点重置，或升级至完整版启用x402付费 |
| 地址标记为恶意 | 200 | `isSafe=false`，地址在黑名单中 | 阻止交易，向用户展示威胁信号详情 |
| 代币蜜罐检测阳性 | 200 | honeypot概率高，存在卖出限制 | 警告用户该代币可能无法卖出，建议不购买 |
| chain_id不支持 | 400 | 免费版仅支持chain_id=1和8453 | 使用Ethereum(1)或Base(8453)链，其他链需升级完整版 |
| X-Client-Fingerprint缺失 | 200 | 回退到IP/User-Agent计费，可能导致配额不稳定 | 建议设置稳定指纹（如 `agent-default`）确保配额分配一致 |
| 请求交易模拟端点 | 403 | 免费版不支持 `simulate-tx` | 升级至完整版以使用交易模拟功能 |
| 服务端错误 | 500 | 上游服务异常 | 检查网络连接和配置后重试；若持续失败，展示错误和 `_meta.requestId` 供排查 |

## 常见问题

### Q1: 免费额度是如何计算的？

免费额度按 `X-Client-Fingerprint` 头部进行每日100次配额分配。UTC时间次日0点自动重置。如果未设置该头部，系统回退到IP/User-Agent进行配额计算，可能导致配额不稳定.
### Q2: 免费版支持哪些链？

免费版支持Ethereum(chain_id=1)和Base(chain_id=8453)两条链的 `check-address` 和 `check-token` 检查。如需Polygon(137)、Arbitrum(42161)、BSC(56)等链支持，请升级至完整版.
### Q3: 免费额度用尽后怎么办？

等待UTC时间次日0点自动重置，或升级至完整版配置x402付费机制（通过 `@x402/fetch` 和 `@x402/evm` 客户端实现USDC自动微额支付），实现超限后自动续用.
### Q4: 免费版可以使用交易模拟吗？

不可以。`POST /v1/simulate-tx` 是完整版独有功能。免费版仅支持只读安全检查（地址声誉和代币蜜罐检测）。如需交易模拟能力，请升级至完整版.
### Q5: 风险等级HIGH和CRITICAL有什么区别？

`HIGH` 表示显著风险，Agent应阻止交易并请求用户确认。`CRITICAL` 表示地址或交易被判定为恶意或不安全，Agent必须阻止交易且不建议继续。两者都会触发 `isSafe=false`，但CRITICAL通常关联已知诈骗地址或蜜罐合约.
### Q6: 如何判断代币是否是蜜罐？

调用 `GET /v1/check-token/:address` 并查看返回的 `honeypot` 概率和风险信号。如果蜜罐概率高于阈值或存在卖出暂停、交易税率异常等信号，建议不要购买该代币.
## 已知限制

- 免费额度100次/天，额度用尽需等待次日重置或升级完整版
- 仅支持Ethereum(1)和Base(8453)两条链，其他链需升级完整版
- 不支持交易模拟（`simulate-tx`），完整版可用
- 不支持x402付费机制和反馈提交端点
- 检测结果不构成100%确定的安全保证，关键决策仍需人工复核

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "区块链安全基础版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "aegis-security"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
