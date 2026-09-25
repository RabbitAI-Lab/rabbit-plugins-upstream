## Description:

Vercel AI Gateway helps agents use Maton-managed authentication to browse AI Gateway models, inspect pricing and usage, check credits, and run OpenAI-compatible or Anthropic-shaped inference requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maton](https://clawhub.ai/user/maton)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to discover Vercel AI Gateway models, compare provider cost and capability signals, monitor credits and usage, and route approved inference requests through a managed Maton connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Vercel AI Gateway through Maton authorizes access through the user's account connection.

Mitigation: Require explicit user approval before connection creation, select the least privilege scopes available, and use only the intended connection when more than one exists.

Risk: Inference requests and some usage workflows can consume credits or depend on paid Vercel plan access.

Mitigation: Default to read and list operations, confirm inference or spend-affecting actions before running them, and surface plan or credit errors to the user.

Risk: Hosted functions and triggers can create persistent data flows to destinations the user may not expect.

Mitigation: Deploy only user-authored or user-reviewed functions, prefer a deny-all network policy, scope triggers narrowly, and confirm every destination and external host.

Risk: Long-lived API keys or trigger payloads may expose secrets or personal data if copied into prompts, logs, or environment variables.

Mitigation: Prefer OAuth, avoid exporting MATON_API_KEY except when the CLI cannot be installed, minimize forwarded payload fields, and keep secrets out of prompts and trigger payloads.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/maton/skills/vercel-ai-gateway)
- [Maton Homepage](https://maton.ai)
- [Vercel AI Gateway REST API](https://vercel.com/docs/ai-gateway/sdks-and-apis/rest-api)
- [Vercel AI Gateway Overview](https://vercel.com/docs/ai-gateway)
- [Vercel AI Gateway Model Catalog](https://vercel.com/ai-gateway/models)
- [Vercel AI Gateway Models and Providers](https://vercel.com/docs/ai-gateway/models-and-providers)
- [Vercel AI Gateway Authentication](https://vercel.com/docs/ai-gateway/authentication-and-byok/authentication)
- [Vercel AI Gateway Pricing and Credits](https://vercel.com/docs/ai-gateway/pricing)
- [Vercel AI Gateway Observability](https://vercel.com/docs/ai-gateway/observability-and-spend/observability)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell, JSON, and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide authenticated Maton CLI or HTTP calls for Vercel AI Gateway and user-approved automation.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
