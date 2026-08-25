# Local hardening patch

Based on ClawHub release `frontier-ai-vl/stock-screener-pro` version `3.1.1`.

Local version: `3.5.0`.

Changes:

- Fixed sell accounting in `backtest_strategy`: net sale proceeds are added to cash.
- Restricted DSA requests to loopback addresses only; the distributed skill never sends DSA credentials to a remote host.
- Added Tonghuashun iFinD HTTP QuantAPI support for realtime quotes and daily history.
- Fixed the QuantAPI host to `https://quantapi.51ifind.com` so credentials cannot be redirected by configuration.
- Moved Tencent public quote and K-line fallbacks to HTTPS.
- Integrated AI4Trade read APIs and explicitly-confirmed signal, follow, and one-shot heartbeat actions using a fixed API host and environment-only token handling.
- Added `auto`, `ths`, and `tencent` provider modes plus a credential-safe status tool.
- Added regression tests for backtest accounting, DSA URL policy, and Tonghuashun response parsing.
- Compacted the public MCP surface, removed the QLib backend, and retained TradingAgents as the optional multi-agent research backend.
- Updated TradingAgents for its 0.7 configuration API and added a short-lived loopback bridge to the current OpenClaw default model. The bridge passes no Gateway token or upstream provider key to TradingAgents.

Do not overwrite this folder with `openclaw skills update stock-screener-pro` unless the upstream release contains equivalent fixes.
