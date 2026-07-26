---
slug: "aegis-security"
name: "aegis-security"
version: 1.2.3
displayName: "区块链安全防护"
summary: "区块链安全API，扫描代币蜜罐、模拟交易、检查地址声誉风险"
license: "Proprietary"
description: |-
  面向AI代理的区块链安全API。提供代币蜜罐检测、交易模拟、地址声誉检查等功能，
  支持EVM和Solana多链，集成x402付费协议。适用于DeFi交易前安全审计、代币风险评估、
  地址欺诈检测等场景。不适用于需要100%确定性的关键决策.
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 安全合规
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# 区块链安全防护

面向AI代理的区块链安全API，提供交易前安全扫描能力。免费额度100次/天，超出后通过x402协议按需付费（USDC on Base或Solana）.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 区块链安全防护处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 深度漏洞扫描与CVE关联 | 不支持 | 支持 |
| 安全基线合规审计 | 不支持 | 支持 |
| 批量资产风险评分 | 不支持 | 支持 |
| 威胁情报实时订阅与告警 | 不支持 | 支持 |

## 安全策略

- 仅限手动调用，禁止自动触发敏感操作
- 禁止请求或存储私钥、助记词、种子短语
- 付费调用前必须确认用户意图（特别是 `simulate-tx`）
- 仅在用户明确批准后自动化签名前检查
- 本skill无需额外环境变量

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
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

通过 `GET /v1/check-address/:address` 端点检查接收地址的链上声誉。传入地址路径参数和 `chain_id` 查询参数（如8453表示Base链），返回 `isSafe` 布尔值、风险等级（LOW/MEDIUM/HIGH/CRITICAL）和威胁信号列表。适用于转账前验证收款方是否为已知恶意地址.
### 2. 交易模拟

通过 `POST /v1/simulate-tx` 端点在链下环境中模拟交易执行。请求体包含 `from`（发送方地址）、`to`（接收方或合约地址）、`value`（wei单位的字符串）、`data`（可选calldata hex）和 `chain_id`（默认8453）。返回交易是否成功执行、状态变更详情和潜在风险警告。适用于DeFi合约交互前的安全预检.
### 3. 代币蜜罐检测
通过 `GET /v1/check-token/:address` 端点检测代币合约是否存在蜜罐行为。传入代币合约地址和 `chain_id`（1=Ethereum, 8453=Base等），返回蜜罐概率百分比、风险评估和具体风险信号（如买入税率过高、卖出暂停等）。适用于购买新代币前的风险评估.
**输入**: 用户提供代币蜜罐检测所需的指令和必要参数.
**处理**: 解析代币蜜罐检测的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 4. 免费额度查询

通过 `GET /v1/usage` 端点查询当前指纹的免费配额使用情况。通过 `X-Client-Fingerprint` 头部识别用户身份，返回 `dailyLimit`（100次/天）、`usedToday`、`remainingChecks` 和 `nextResetAt`（UTC时间戳）。适用于配额监控和调用规划.
### 5. x402付费机制

超出免费额度后，API返回 `402 Payment Required` 状态码并附带x402付费挑战。通过集成 `@x402/fetch` 和 `@x402/evm`（EVM链）或 `@x402/svm`（Solana链）客户端，实现自动支付和请求重试。支持USDC在Base链或Solana上的微额支付。适用于高频安全检查场景。- 验证返回数据的完整性和格式正确性
- 参考`x402付费机制`的配置文档进行参数调优
### 6. 风险等级评估
根据检查结果自动计算综合风险等级。`LOW` 表示次要风险可放行，`MEDIUM` 表示存在部分风险需人工复核，`HIGH` 表示显著风险需阻止并确认，`CRITICAL` 表示恶意或不安全必须阻止。每个响应包含 `isSafe` 布尔值和详细威胁信号列表。适用于自动化交易策略中的风险决策.
**输入**: 用户提供风险等级评估所需的指令和必要参数.
### 7. 多链支持
支持8条区块链的地址和代币检查：Ethereum(chain_id=1)、Base(chain_id=8453)、Polygon(chain_id=137)、Arbitrum(chain_id=42161)、Optimism(chain_id=10)、BSC(chain_id=56)、Avalanche(chain_id=43114)和Solana。`check-address` 和 `check-token` 支持全部链，`simulate-tx` 仅支持EVM链（Solana不支持交易模拟）.
**输入**: 用户提供多链支持所需的指令和必要参数.
**输出**: 返回多链支持的处理结果,包含执行状态码、结果数据和执行日志.
### 8. 反馈提交
通过 `POST /v1/feedback` 端点提交问题报告或功能反馈，不消耗免费配额。请求体包含 `kind`（issue/feedback/expectation）、`summary`、`endpoint`、`status_code`、`chain_id` 和 `agent` 对象（含name和version）。支持通过 `failed_request_id` 关联 `_meta.requestId` 进行服务端追踪。适用于问题反馈和服务改进.
**处理**: 解析反馈提交的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回反馈提交的处理结果,包含执行状态码、结果数据和执行日志.
#
## 使用流程

1. 在所有请求中设置 `X-Client-Fingerprint` 头部为稳定的用户标识，确保免费配额稳定分配
2. 调用 `GET /v1/usage` 检查剩余免费配额，规划当日调用次数
3. 交易前并行执行三项检查：`GET /v1/check-address/:to` + `POST /v1/simulate-tx` + `GET /v1/check-token/:token`
4. 根据风险等级决策：LOW允许放行，MEDIUM提示用户复核，HIGH/CRITICAL阻止交易并解释风险
5. 超出免费配额时，配置x402客户端（`@x402/fetch` + `@x402/evm`）实现自动付费续用

#
## 示例

### 示例1：检查Base链地址安全性并查询免费额度

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
# ...
# 响应包含 isSafe、riskLevel、threatSignals 等字段
```

### 示例2：模拟Ethereum上的代币交换交易

```bash
curl -X POST "https://security-api.example.com/v1/simulate-tx" \
  -H "Content-Type: application/json" \
  -H "X-Client-Fingerprint: agent-default" \
  -d '{
    "from": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
    "to": "0x68b3465833fb72A70ecDF485E0e4C7bD56653845",
    "value": "0",
    "data": "0x38ed1739",
    "chain_id": 1
  }'
# ...
# 同时检查目标代币是否存在蜜罐风险
curl "https://security-api.example.com/v1/check-token/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48?chain_id=1" \
  -H "X-Client-Fingerprint: agent-default"
```

## 错误处理

| 错误场景 | HTTP状态 | 原因 | 处理方式 |
|:---:|:---:|:---:|:---:|
| 免费额度耗尽 | 402 | 当日100次免费配额已用完 | 配置x402客户端自动付费，或等待UTC次日0点重置 |
| 地址标记为恶意 | 200 | `isSafe=false`，地址在黑名单中 | 阻止交易，向用户展示威胁信号详情 |
| 代币蜜罐检测阳性 | 200 | honeypot概率高，存在卖出限制 | 警告用户该代币可能无法卖出，建议不购买 |
| chain_id不支持 | 400 | 传入了不在支持列表中的链ID | 检查Supported Chains表，使用有效的chain_id（如1/8453/137） |
| X-Client-Fingerprint缺失 | 200 | 回退到IP/User-Agent计费，可能导致配额不稳定 | 建议设置稳定指纹（如 `agent-default`）确保配额分配一致 |
| simulate-tx的value格式错误 | 400 | value传入了数字而非wei字符串 | 确保value为字符串类型（如 `"0"` 而非 `0`），单位为wei |
| Solana链调用simulate-tx | 400 | Solana不支持交易模拟 | 对Solana链仅使用 `check-address` 和 `check-token`，跳过simulate-tx |
| 服务端错误 | 500 | 上游服务异常 | 一次；若持续失败，展示错误和 `_meta.requestId` 供排查 |

## 常见问题

### Q1: 免费额度是如何计算的？

免费额度按 `X-Client-Fingerprint` 头部进行每日100次配额分配。UTC时间次日0点自动重置。如果未设置该头部，系统回退到IP/User-Agent进行配额计算，可能导致配额不稳定.
### Q2: 如何配置x402付费机制？

安装 `@x402/fetch` 和 `@x402/evm`（EVM链）或 `@x402/svm`（Solana链）npm包，创建x402Client并注册签名方案，用 `wrapFetchWithPayment` 包装fetch函数。配置一个代理管理的钱包签名器（不要在prompt或环境变量中存储原始私钥）.
### Q3: 哪些链支持交易模拟（simulate-tx）？

`simulate-tx` 支持所有EVM链：Ethereum(1)、Base(8453)、Polygon(137)、Arbitrum(42161)、Optimism(10)、BSC(56)、Avalanche(43114)。Solana链不支持交易模拟，仅支持 `check-address` 和 `check-token`.
### Q4: 风险等级HIGH和CRITICAL有什么区别？

`HIGH` 表示显著风险，Agent应阻止交易并请求用户确认。`CRITICAL` 表示地址或交易被判定为恶意或不安全，Agent必须阻止交易且不建议继续。两者都会触发 `isSafe=false`，但CRITICAL通常关联已知诈骗地址或蜜罐合约.
### Q5: X-Client-Fingerprint的作用是什么？

`X-Client-Fingerprint` 是用于免费配额识别的稳定标识符。设置为固定的用户或Agent ID（如 `agent-default`）可确保配额分配一致。轮换指纹可能绕过免费配额限制，但这不是安全机制，仅是尽力而为的防滥用措施.
### Q6: 如何判断代币是否是蜜罐？

调用 `GET /v1/check-token/:address` 并查看返回的 `honeypot` 概率和风险信号。如果蜜罐概率高于阈值或存在卖出暂停、交易税率异常等信号，建议不要购买该代币。同时建议配合 `simulate-tx` 验证交易是否能正常执行.
## 已知限制

- 免费额度100次/天，高频场景需配置x402付费
- `simulate-tx` 不支持Solana链
- 免费配额基于尽力而为的防滥用机制，非安全保证
- 检测结果不构成100%确定的安全保证，关键决策仍需人工复核

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "区块链安全防护处理结果",
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
