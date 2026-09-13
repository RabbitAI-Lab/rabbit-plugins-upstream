## Description:

Vercel AI Gateway provides managed-authentication access to the Vercel AI Gateway for catalog discovery, pricing and usage inspection, credit checks, and approved inference calls through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI operators use this skill to discover Vercel AI Gateway models, compare pricing and limits, monitor credits and generation usage, and route approved inference requests through a connected account. It is also useful for setting up user-approved Maton functions or time/event triggers that call Vercel AI Gateway actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inference calls can consume paid Vercel AI Gateway credits or bill the connected account.

Mitigation: Confirm the model, approximate request size, loop or batch size, and spending intent before running inference, especially for high-token or repeated calls.

Risk: Maton API keys are long-lived credentials when the CLI cannot be used.

Mitigation: Prefer OAuth through the Maton CLI; when raw HTTP is necessary, keep the key in the process environment, never print or persist it, send it only to api.maton.ai, and rotate it if exposed.

Risk: Functions, triggers, destinations, and watch --exec can create ongoing automation or persistent data forwarding.

Mitigation: Require explicit user approval for each account, scope, destination host, payload field, handler, network policy, and cleanup step; keep destinations inside Maton unless the user approves a named external host.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/vercel-ai-gateway)
- [Maton Homepage](https://maton.ai)
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
- [Time Trigger Reference](references/time/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent instructions for authenticated API calls through Maton; no hidden executable code is bundled.]

## Skill Version(s):

1.2.4 (source: server release metadata; skill frontmatter version 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
