## Description:

Vercel AI Gateway helps agents use Maton-managed authentication to browse AI Gateway models, inspect pricing and usage, monitor credits, and run OpenAI- or Anthropic-compatible inference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to discover and compare Vercel AI Gateway models and providers, monitor credits and usage, and route inference through a connected account with user-approved authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or use a Vercel AI Gateway connection through Maton.

Mitigation: Require deliberate approval before creating a connection, and select the intended Maton profile and connection when multiple accounts are available.

Risk: Inference calls can consume credits or bill the connected account.

Mitigation: Confirm billed POST requests, model choice, and approximate request size before running inference, especially in loops or batches.

Risk: Prompts and completions may be forwarded to upstream model providers and retained in usage records.

Mitigation: Do not include secrets or sensitive credentials in prompts, and treat generated model output as untrusted data.

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

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, API calls]

**Output Format:** [Markdown with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and deliberate approval for connection creation or billed inference.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
