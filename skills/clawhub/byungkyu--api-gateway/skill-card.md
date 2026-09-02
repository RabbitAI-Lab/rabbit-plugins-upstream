## Description:

API Gateway helps agents call user-connected third-party APIs through the Maton gateway for app actions, connection management, functions, triggers, webhook destinations, and local handlers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agent users use this skill to operate connected SaaS apps through Maton for mailbox, CRM, issue, spreadsheet, search, scraping, and automation workflows. It is intended for accounts and apps the user has already connected, with explicit approval for writes, connection changes, triggers, destinations, and local handlers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected-app API calls can access or modify data in services the user has authorized through Maton.

Mitigation: Use OAuth where possible, grant the narrowest practical scopes, and require explicit user confirmation before any write, connection, trigger, destination, or handler action.

Risk: Trigger destinations and local --exec handlers can continue forwarding or acting on future events until stopped.

Mitigation: Review every automation before approval, keep destinations and handlers narrowly scoped, and delete or disable them when no longer needed.

Risk: Long-lived API keys or provider-issued tokens may be exposed if handled casually.

Mitigation: Prefer OAuth and the operating system credential store; avoid printing credentials, passing them on command lines, or sending Maton credentials to third-party hosts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/api-gateway)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, configuration guidance, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or run Maton CLI and API calls for connected apps, subject to user authentication and confirmation requirements.]

## Skill Version(s):

1.0.152 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
