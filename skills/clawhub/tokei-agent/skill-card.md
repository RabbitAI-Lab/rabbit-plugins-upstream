## Description:

tokei-agent lets agents and command-line users control Tokei pre-launch, waitlist, giveaway, referral, and campaign pages through the Tokei v1 REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gilesdawe](https://clawhub.ai/user/gilesdawe)

### License/Terms of Use:

MIT

## Use Case:

Developers, operators, and AI agents use this skill to inspect, create, update, publish, and monitor Tokei launch pages and campaign workflows from the CLI or MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A read+write API key can change public campaign state, entries, media, and webhooks.

Mitigation: Use a read-only key for monitoring and require explicit human confirmation before publishing pages, creating entries, uploading public media, or creating/deleting webhooks.

Risk: API responses may include entrant email addresses, survey answers, analytics, and other account data.

Mitigation: Treat command output, logs, scripts, and agent conversation history that include CLI results as sensitive user data.

Risk: List-style update fields such as prizes, reward thresholds, and entry methods replace the entire existing list.

Mitigation: Read the page first, modify the complete list, send the full replacement, and verify the result with a follow-up read.

Risk: Uploaded media becomes a public asset used on a promotion page.

Mitigation: Upload only intended files and use the public_url returned by media:upload for page media fields.

## Reference(s):

- [Tokei agent documentation](https://tokei.io/agent)
- [Tokei API reference](https://tokei.io/docs/api)
- [Tokei OpenAPI specification](https://tokei.io/openapi.json)
- [npm package: tokei-agent](https://www.npmjs.com/package/tokei-agent)
- [ClawHub skill page](https://clawhub.ai/gilesdawe/skills/tokei-agent)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands; CLI and MCP calls return JSON envelopes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node 22+ and TOKEI_API_KEY. Command results can include rate_limit data, and write access depends on the API key scope.]

## Skill Version(s):

0.3.4 (source: package.json, CHANGELOG, server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
