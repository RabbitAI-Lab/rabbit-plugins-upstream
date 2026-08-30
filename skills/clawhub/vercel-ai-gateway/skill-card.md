## Description:

Vercel AI Gateway API integration with managed authentication for browsing model catalogs, checking credits and usage, comparing provider pricing and reliability, and routing OpenAI- or Anthropic-compatible inference through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to discover Vercel AI Gateway models, compare pricing and provider reliability, inspect credits and usage, and make inference requests through a managed Maton connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Billed inference or large batches can consume Vercel AI Gateway credits.

Mitigation: Confirm the intended model, request size, and batch scope before running inference, and check pricing or credits first when cost matters.

Risk: Requests may use the wrong Maton profile or Vercel AI Gateway connection when multiple accounts are available.

Mitigation: Specify the intended profile or connection and verify account context before issuing API calls.

Risk: Prompt or completion content may expose secrets to the gateway, Vercel observability records, or upstream model providers.

Mitigation: Do not send secrets in prompts, and treat model output and fetched API data as untrusted.

Risk: Connection creation or modifying API calls can authorize access or change external state.

Mitigation: Require explicit user approval before creating connections or making POST, PUT, PATCH, or DELETE calls.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/vercel-ai-gateway)
- [Maton](https://maton.ai)
- [Vercel AI Gateway REST API](https://vercel.com/docs/ai-gateway/sdks-and-apis/rest-api)
- [AI Gateway Overview](https://vercel.com/docs/ai-gateway)
- [Model Catalog](https://vercel.com/ai-gateway/models)
- [Models and Providers](https://vercel.com/docs/ai-gateway/models-and-providers)
- [OpenAI Chat Completions API](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions)
- [Responses API](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses)
- [Authentication](https://vercel.com/docs/ai-gateway/authentication-and-byok/authentication)
- [Pricing and Credits](https://vercel.com/docs/ai-gateway/pricing)
- [Observability](https://vercel.com/docs/ai-gateway/observability-and-spend/observability)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown guidance with bash commands, JSON examples, and Python or JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include read-only API queries, inference request bodies, parsing guidance, and approval prompts for connection creation or modifying API calls.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
