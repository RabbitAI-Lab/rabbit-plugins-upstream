# GLM-5.2 verified integration facts

Verified 2026-08-17 against Theta EdgeCloud and OpenClaw.

- Canonical service alias: `glm_5_2`
- Prediction: `completions`
- Default variant: `default`
- Input fields: `messages`, `max_tokens`, `temperature`, `top_p`, `stream`, `enable_thinking`
- Default `max_tokens`: 5000
- Advertised model context: 1,000,000 tokens
- License: MIT
- Raw split-price metadata observed: input 154, output 484, divisor 1,000,000; currency not asserted
- OpenClaw model: `litellm/glm_5_2`; alias `theta-glm`
- Policy: opt-in for bounded, reversible, objectively verifiable worker tasks; not Board default or automatic fallback

Runtime acceptance gates:

- `glm_5_2` is present in the chat-service allowlist.
- Live aliases/names containing `glm` categorize as `text`.
- Bundled catalog lookup exposes GLM-5.2 metadata.
- Dry-run chat accepts `glm_5_2` without `allowUnknownService`.
- Unsupported-service errors derive the known-service list from the allowlist to prevent drift.
