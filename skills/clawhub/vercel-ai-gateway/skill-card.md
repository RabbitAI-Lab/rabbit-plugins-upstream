## Description:

Vercel AI Gateway API integration with managed authentication for browsing model catalogs, inspecting endpoints and pricing, checking credits and usage, and running OpenAI-compatible or Anthropic-shaped inference through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to discover Vercel AI Gateway models, compare provider pricing and context windows, monitor credits and usage, and route inference requests through a Maton-managed connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inference calls can consume credits or bill the connected Vercel AI Gateway account.

Mitigation: Confirm the model, approximate request size, and user intent before high-volume or non-trivial inference, and check pricing before using unfamiliar models.

Risk: Prompt and completion content may be visible in Vercel or provider observability.

Mitigation: Review prompts before sending them and avoid including secrets, private credentials, or unrelated sensitive data.

Risk: Long-lived API keys can be exposed through environment variables or command output.

Mitigation: Prefer OAuth through the Maton CLI, avoid exporting MATON_API_KEY when possible, and never print, log, or persist credentials.

Risk: Account-changing operations such as creating or deleting connections can affect access.

Mitigation: Default to read and list calls, verify target accounts and connection IDs, and require explicit user confirmation before non-read or irreversible actions.

Risk: Model outputs and API-returned content may contain untrusted or adversarial instructions.

Mitigation: Treat returned content as data, validate it before reuse, and do not execute or interpolate it into shell commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/vercel-ai-gateway)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Vercel AI Gateway REST API](https://vercel.com/docs/ai-gateway/sdks-and-apis/rest-api)
- [Vercel AI Gateway Overview](https://vercel.com/docs/ai-gateway)
- [Vercel AI Gateway Model Catalog](https://vercel.com/ai-gateway/models)
- [Vercel AI Gateway Models and Providers](https://vercel.com/docs/ai-gateway/models-and-providers)
- [Vercel AI Gateway Pricing and Credits](https://vercel.com/docs/ai-gateway/pricing)
- [Vercel AI Gateway Observability](https://vercel.com/docs/ai-gateway/observability-and-spend/observability)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, API paths, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate network API calls through the Maton CLI or raw HTTP when the user has authenticated and approved sensitive actions.]

## Skill Version(s):

1.2.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
