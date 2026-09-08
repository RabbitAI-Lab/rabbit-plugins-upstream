# GLM-5.3 on Theta EdgeCloud (validated 2026-08-31)

## Route
- Base URL: `https://ondemand.thetaedgecloud.com/infer_request`
- OpenAI-compatible chat completions: `POST /infer_request/chat/completions`
- Model id: `glm_5_3` (response `model` field reports `glm-5.3`)
- Auth: `Authorization: Bearer <on-demand API token>`

## Tool calling (the key change vs GLM-5.2 docs)
- Use the **OpenAI-compatible `/chat/completions`** endpoint with top-level `tools` + `tool_choice`.
- Verified modes: `none`, `auto`, `required`, forced function selection; plus schema-valid arguments, parallel tool calls, streaming, and tool-result continuation (`role:"tool"` + `tool_call_id` round-trip).
- The job-style `/infer_request/glm_5_3` endpoint returns stored job results and does **not** expose structured `tool_calls`. (Confirmed by Theta Support, 2026-08-31.)

## Live test evidence (2026-08-31, from VPS)
1. Plain non-stream call: `GLM53_PLAIN_OK` returned, finish_reason `stop`, `reasoning_content` present.
2. Tool call: weather question -> `finish_reason: "tool_calls"` with `tool_calls[0].function.name = "get_weather"`, valid JSON args `{"city":"Panama City","country":"Panama"}`.
3. Tool-result continuation: assistant consumed tool result and produced final natural-language answer.

## Quirks
- SSE streaming by default; send `"stream": false` for single JSON.
- Reasoning arrives via `reasoning_content` fields.
- Cached tokens reported in `prompt_tokens_details.cached_tokens`.

## OpenClaw integration
- Model: `litellm/glm_5_3`, alias `theta-glm-53`, 1M context, `supportsTools: true`.
- Fallback chain (default agents): `openai/gpt-5.6-sol` (primary) -> `anthropic/claude-opus-4-7` -> `litellm/glm_5_3` -> `litellm/glm_5_2` -> `openai/gpt-5.3-codex`.
- Board Telegram session `agent:main:telegram:default:direct:671124787` pinned to `litellm/glm_5_3` (live-validated end-to-end through the gateway with tool use).

## Related Theta news (Aug 2026)
- Theta expanded project-scoped APIs + MCP server so agents can discover, deploy, and manage GPU nodes themselves (GPU discovery, deployment templates, lifecycle mgmt, status/logs, read-only billing). Blog: https://blog.thetatoken.org/ai-agents-can-now-deploy-edgecloud-gpus-themselves/
- GLM-5.3: 743B MoE (~39B active), same base as GLM-5.2 with post-training gains; CyberGym/AutomationBench leader.
