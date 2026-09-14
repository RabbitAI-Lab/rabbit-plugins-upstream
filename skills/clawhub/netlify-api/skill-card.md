## Description:

Netlify API integration with managed OAuth for viewing Netlify sites, deploys, builds, DNS zones, environment variables, and related administration data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Netlify account resources, review deploy and build status, and prepare approved administrative API actions through Maton-managed authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help administer Netlify resources with substantial account, DNS, build, webhook, and environment-variable impact.

Mitigation: Default to read-only inspection first and require explicit confirmation with specific resource identifiers before any write or automation.

Risk: OAuth tokens, API keys, and provider credentials can expose connected accounts if printed, stored, copied into destination headers, or passed through command lines.

Mitigation: Use managed OAuth where possible, keep credentials in the approved credential store, avoid logging secrets, and do not embed Maton or provider tokens in destinations.

Risk: Trigger destinations and hosted functions can create persistent automated data flows or actions after setup.

Mitigation: Confirm the destination host, payload fields, network policy, connection scope, and intended schedule or event source before creating or updating automation.

Risk: Local event handlers invoked through watch execution can run against untrusted event data.

Mitigation: Treat local execution as out of scope unless the user supplies or reviews the handler and separately approves the long-running automation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/netlify-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Netlify API Documentation](https://open-api.netlify.com/)
- [Netlify CLI](https://docs.netlify.com/cli/get-started/)
- [Netlify Build Hooks](https://docs.netlify.com/configure-builds/build-hooks/)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)
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

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose authenticated Netlify API calls through Maton; writes and automation require explicit user confirmation.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
