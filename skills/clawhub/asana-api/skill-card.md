## Description:

Asana API integration with managed OAuth for accessing tasks, projects, workspaces, users, and webhooks through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Asana work items, track projects, inspect workspace and user data, and integrate Asana workflows through authenticated Maton CLI or API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify Asana data through a connected Maton account.

Mitigation: Prefer OAuth, approve only the needed Asana account and scopes, and review proposed write, webhook, or membership changes before they run.

Risk: Using API keys instead of OAuth can expose a long-lived credential.

Mitigation: Use OAuth where possible; if an API key is required, do not print, persist, or pass it on the command line.

Risk: Ambiguous defaults may target the wrong Maton profile or Asana connection.

Mitigation: Specify the intended profile and connection when multiple accounts or connections are available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/asana-api)
- [Maton homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Asana API Documentation](https://developers.asana.com)
- [Asana API Reference](https://developers.asana.com/reference)
- [Asana LLM Reference](https://developers.asana.com/llms.txt)
- [Related api-gateway skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline shell commands, JSON examples, and API request guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands, raw HTTP fallback examples, jq filters, and SDK snippets for Asana operations.]

## Skill Version(s):

1.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
