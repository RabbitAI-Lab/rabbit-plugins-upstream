## Description:

Vercel AI Gateway API integration with managed authentication for browsing models, checking credits and usage, and routing inference through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maton](https://clawhub.ai/user/maton)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical operators use this skill to inspect Vercel AI Gateway models, pricing, credits, usage, and endpoint behavior, then run approved inference through an authenticated Maton connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid inference or write actions can spend Vercel credits or change external state.

Mitigation: Confirm the target endpoint, model, payload, and approximate request volume before any POST, PUT, PATCH, DELETE, loop, or batch.

Risk: Raw Maton API keys are long-lived credentials that can leak through environment output, logs, command history, or committed files.

Mitigation: Prefer OAuth through the Maton CLI; when raw HTTP is unavoidable, read the key only from the process environment, never print or persist it, and rotate it if exposed.

Risk: Hosted functions and trigger destinations can create persistent automation or event forwarding.

Mitigation: Use user-authored or user-reviewed handlers, keep function network policy at DENY_ALL when possible, prefer platform destinations, and require separate approval for every third-party host.

Risk: Prompt and completion content may be forwarded to upstream providers and retained in Vercel AI Gateway usage or observability records.

Mitigation: Do not send secrets in prompts, limit requests to the fields needed for the task, and treat model output as untrusted data.

Risk: Adding signing headers to platform-hosted destinations can store unnecessary secrets.

Mitigation: Omit X-Signature-Key for api.maton.ai or *.maton.app destinations unless a user-approved external receiver specifically requires its own signing secret.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/maton/skills/vercel-ai-gateway)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Vercel AI Gateway REST API](https://vercel.com/docs/ai-gateway/sdks-and-apis/rest-api)
- [Vercel AI Gateway Overview](https://vercel.com/docs/ai-gateway)
- [Vercel AI Gateway Model Catalog](https://vercel.com/ai-gateway/models)
- [Vercel AI Gateway Models and Providers](https://vercel.com/docs/ai-gateway/models-and-providers)
- [Vercel AI Gateway Authentication](https://vercel.com/docs/ai-gateway/authentication-and-byok/authentication)
- [Vercel AI Gateway Pricing and Credits](https://vercel.com/docs/ai-gateway/pricing)
- [Vercel AI Gateway Observability](https://vercel.com/docs/ai-gateway/observability-and-spend/observability)
- [Time Trigger Reference](references/time/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, code snippets, JSON examples, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide authenticated Maton CLI or API calls; connection, write, paid inference, function, and trigger actions require explicit user approval.]

## Skill Version(s):

1.2.4 (source: server release metadata; artifact frontmatter version 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
