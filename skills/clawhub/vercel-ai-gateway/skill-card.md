## Description:

Vercel AI Gateway API integration with managed authentication for browsing models, inspecting pricing and usage, checking credits, and routing OpenAI-compatible or Anthropic-shaped inference requests through Vercel AI Gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maton](https://clawhub.ai/user/maton)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect a Maton-authenticated Vercel AI Gateway account, inspect available AI Gateway models, compare pricing and usage, monitor credits, and run approved inference calls. It also documents how user-approved hosted functions and triggers can automate those calls without expanding the Vercel AI Gateway connection scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated inference can spend Vercel AI Gateway credits or bill the connected account.

Mitigation: Confirm the model, request size, and any loop or batch behavior before running inference, and prefer read-only model, credit, and usage checks first.

Risk: Connection creation, hosted functions, triggers, and destinations can create persistent access or automation.

Mitigation: Require explicit user approval for each connection, deploy, trigger, and destination action, and scope each action to the narrowest account, connection, function, host, and payload needed.

Risk: Raw Maton API keys are long-lived credentials that can leak through environment variables, logs, shell history, or destination templates.

Mitigation: Use OAuth through the Maton CLI when available; when raw HTTP is unavoidable, read keys only from the process environment, never print or persist them, and send them only to api.maton.ai.

Risk: Trigger payloads from supported event sources can contain personal, private, financial, or otherwise sensitive data.

Mitigation: Use platform-owned destinations where possible, forward only necessary fields with body templates, and get informed approval before sending event data to any external host.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/maton/skills/vercel-ai-gateway)
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
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include authenticated API responses or summaries when the user approves the relevant action.]

## Skill Version(s):

1.2.4 (source: server release metadata; skill frontmatter: 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
