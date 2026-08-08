## Description:

Vercel AI Gateway API integration with managed authentication for browsing models, comparing provider endpoints and pricing, checking credits and usage, and running OpenAI- or Anthropic-compatible inference through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to discover Vercel AI Gateway models, compare pricing and provider endpoint health, check credits and generation usage, and route inference requests through Maton-managed authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inference calls can consume credits or bill the connected Vercel AI Gateway account.

Mitigation: Confirm the selected model, connection, approximate request size, and loop or batch scope before running billable inference.

Risk: Prompt and completion content is forwarded to upstream model providers and may appear in AI Gateway observability records.

Mitigation: Avoid sending secrets or sensitive data in prompts, and treat generated model output as untrusted.

Risk: Multiple Maton connections can route requests to the wrong Vercel AI Gateway account if no connection is specified.

Mitigation: Use the Maton-Connection header when more than one active connection exists.

## Reference(s):

- [ClawHub Vercel AI Gateway skill](https://clawhub.ai/byungkyu/skills/vercel-ai-gateway)
- [Maton](https://maton.ai)
- [Vercel AI Gateway REST API](https://vercel.com/docs/ai-gateway/sdks-and-apis/rest-api)
- [Vercel AI Gateway overview](https://vercel.com/docs/ai-gateway)
- [Vercel AI Gateway model catalog](https://vercel.com/ai-gateway/models)
- [Vercel AI Gateway models and providers](https://vercel.com/docs/ai-gateway/models-and-providers)
- [Vercel AI Gateway OpenAI chat completions](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions)
- [Vercel AI Gateway Responses API](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses)
- [Vercel AI Gateway authentication](https://vercel.com/docs/ai-gateway/authentication-and-byok/authentication)
- [Vercel AI Gateway pricing](https://vercel.com/docs/ai-gateway/pricing)
- [Vercel AI Gateway observability](https://vercel.com/docs/ai-gateway/observability-and-spend/observability)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, API calls, Configuration]

**Output Format:** [Markdown with inline bash, Python, HTTP, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and a valid MATON_API_KEY; inference examples may create billable AI Gateway usage.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
