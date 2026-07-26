[🇺🇸 English](#english) · [🇨🇳 中文](#chinese)

---

<a name="english"></a>

# Wallet Balance

Multi-chain wallet balance skill for AI agents. Supports EVM chains, supported non-EVM chains, and Bitcoin. Powered by Antalpha AI `wallet-balance-query` MCP integration with automatic EVM public-data fallback.

## Features

- 🔍 **Multi-chain: EVM + Non-EVM + BTC** — supports **80+ chains**:
  - **68+ EVM chains**: Ethereum, BNB Chain, Base, Arbitrum, Optimism, Polygon, Avalanche, zkSync Era, Linea, Scroll, Blast, Berachain, Mantle, Sonic, and more
  - **11 Non-EVM chains**: Solana (SOL), Tron (TRX + TRC-20), TON, XRP, Litecoin (LTC), NEAR, Sui (SUI), Aptos (APT), Polkadot (DOT), Cardano (ADA), Kaspa (KAS)
  - **Bitcoin (BTC)**: via Blockstream public API
- 🤖 **Deterministic MCP balance query** — uses `wallet-balance-query` via Antalpha AI MCP, with stable token ordering plus total USD and by-chain summary
- 🔄 **Auto fallback** — if an EVM MCP query is unreachable, falls back to public RPC (Ethereum, BSC) + Blockstream (BTC) + CoinGecko pricing
- 💾 **Address memory** — agents can remember addresses; say "check my balance" and all saved addresses are queried automatically
- 🌐 **Language-aware replies** — responds in the same language the user writes in

## Install

```bash
openclaw skill install https://github.com/AntalphaAI/wallet-balance
```

### Install via ClawHub

```bash
clawhub install wallet-balance
```

## Quick Start

```bash
cp .env.example .env
npm install
npm start
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `MCP_SKILLS_URL` | MCP Streamable HTTP endpoint (default: `https://mcp-skills.ai.antalpha.com/mcp`) |
| `MCP_TOOL_NAME` | Tool id (default: `wallet-balance-query`) |
| `MCP_API_KEY` | Optional `Authorization: Bearer` value |
| `ENABLE_MCP` | Default `true`; set `false` to use only public providers for EVM |
| `ENABLE_FALLBACK_PROVIDER` | Default `true`; when MCP fails for EVM, use public subset |
| `MAX_MCP_RESPONSE_CHARS` | Upper bound on MCP SSE body size (default `12000000`) |
| `MCP_MAX_TOKEN_ROWS` | Max rows read from MCP `tokens` array (default `50000`) |
| `ETH_RPC_URL` / `BNB_RPC_URL` | Public RPC defaults via PublicNode |
| `MEMORY_STORE_PATH` | Optional absolute path for the memory JSON file |

## API Endpoints

- `GET /agent-skills/v1/assets?input=<address>` — single address lookup
- `GET /agent-skills/v1/assets?from_memory=1` — query all remembered addresses + combined total
- `GET /agent-skills/v1/memory` — list remembered addresses
- `POST /agent-skills/v1/memory` — add `{"add":"0x..."}` or remove `{"remove":"0x..."}`
- `GET /healthz` — health check (includes `mcp_enabled`)

## Response `data_source` Values

- `mcp_wallet_balance_query` — balances from Antalpha AI MCP `wallet-balance-query`
- `public_only` — BTC queries, or EVM with `ENABLE_MCP=false`
- `public_fallback` — EVM MCP failed/timed out and fallback was used

## Usage Examples

```
"Check the balance of 0x81f9c401B0821B6E0a16BC7B1dF0F647F36211Dd"
"What's in my wallet?"
"查一下 0x... 的余额"
"查我的余额"
```

## Packaging Notes

Exclude `node_modules`, `.env`, and `remembered-addresses.json` from distributable archives. Run `npm install` and configure `.env` on the target host.

---

<a name="chinese"></a>

# Wallet Balance（钱包余额查询）

面向 AI Agent 的多链钱包余额查询技能，支持 EVM、受支持的非 EVM 链和比特币，通过 Antalpha AI 的 `wallet-balance-query` MCP 工具获取稳定余额汇总，并在 EVM 的 MCP 不可用时自动降级到公开数据。

## 功能特性

- 🔍 **多链支持（EVM + 非 EVM + BTC）** — 覆盖 *80+ 条链*：
  - **68+ EVM 链**：以太坊、BNB Chain、Base、Arbitrum、Optimism、Polygon、Avalanche、zkSync Era、Linea、Scroll、Blast、Berachain、Mantle、Sonic 等
  - **11 条非 EVM 链**：Solana (SOL)、Tron (TRX+TRC-20)、TON、XRP、Litecoin (LTC)、NEAR、Sui (SUI)、Aptos (APT)、Polkadot (DOT)、Cardano (ADA)、Kaspa (KAS)
  - **Bitcoin (BTC)**：通过 Blockstream 公开 API 查询
- 🤖 **确定性 MCP 余额查询** — 通过 Antalpha AI MCP 调用 `wallet-balance-query`，返回稳定排序的 token 列表、总资产和分链汇总
- 🔄 **自动降级** — EVM 的 MCP 不可达时自动切换到公开 RPC（ETH/BSC）+ Blockstream（BTC）+ CoinGecko 报价
- 💾 **地址记忆** — Agent 可记住钱包地址，用户说"查我的余额"即自动汇总所有已保存地址
- 🌐 **语言自适应** — 用中文问就用中文回，用英文问就用英文回

## 安装

```bash
openclaw skill install https://github.com/AntalphaAI/wallet-balance
```

### 通过 ClawHub 安装

```bash
clawhub install wallet-balance
```

## 快速启动

```bash
cp .env.example .env
npm install
npm start
```

## 环境变量

| 变量 | 说明 |
|------|------|
| `MCP_SKILLS_URL` | MCP 端点（默认：`https://mcp-skills.ai.antalpha.com/mcp`） |
| `MCP_TOOL_NAME` | 工具 ID（默认：`wallet-balance-query`） |
| `MCP_API_KEY` | 可选，`Authorization: Bearer` 鉴权值 |
| `ENABLE_MCP` | 默认 `true`；设为 `false` 则 EVM 仅使用公开数据 |
| `ENABLE_FALLBACK_PROVIDER` | 默认 `true`；MCP 失败时自动降级到公开数据 |
| `MAX_MCP_RESPONSE_CHARS` | MCP SSE 响应体大小上限（默认 `12000000`） |
| `MCP_MAX_TOKEN_ROWS` | 从 MCP `tokens` 数组最多读取的行数（默认 `50000`） |
| `ETH_RPC_URL` / `BNB_RPC_URL` | EVM 公开 RPC（通过 PublicNode） |
| `MEMORY_STORE_PATH` | 记忆文件自定义绝对路径 |

## API 接口

- `GET /agent-skills/v1/assets?input=<地址>` — 单地址查询
- `GET /agent-skills/v1/assets?from_memory=1` — 查询所有已保存地址 + 合并总资产
- `GET /agent-skills/v1/memory` — 列出已保存地址
- `POST /agent-skills/v1/memory` — 添加 `{"add":"0x..."}` 或删除 `{"remove":"0x..."}`
- `GET /healthz` — 健康检查（含 `mcp_enabled` 状态）

## data_source 字段说明

- `mcp_wallet_balance_query` — 来自 Antalpha AI MCP `wallet-balance-query`
- `public_only` — BTC 查询，或 `ENABLE_MCP=false` 时的 EVM 查询
- `public_fallback` — EVM 的 MCP 超时/不可达，已降级到公开数据

## 使用示例

```
"Check the balance of 0x81f9c401B0821B6E0a16BC7B1dF0F647F36211Dd"
"What's in my wallet?"
"查一下 0x... 的余额"
"查我的余额"
```

## 打包说明

分发时请排除 `node_modules`、`.env` 和 `remembered-addresses.json`；在目标主机上执行 `npm install` 并配置 `.env` 后启动。
