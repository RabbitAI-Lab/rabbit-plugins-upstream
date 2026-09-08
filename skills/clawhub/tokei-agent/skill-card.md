## Description:

tokei-agent lets agents and CLI users manage Tokei pre-launch, waitlist, giveaway, referral, and launch campaigns through the Tokei v1 REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gilesdawe](https://clawhub.ai/user/gilesdawe)

### License/Terms of Use:

MIT

## Use Case:

Developers, campaign operators, and agent builders use this skill to monitor and manage Tokei launch pages, waitlists, giveaways, referrals, entrants, winners, media, and webhooks from command-line or MCP workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and change Tokei campaigns when supplied with a valid API key.

Mitigation: Use read-only API keys for monitoring, reserve read+write keys for requested changes, and confirm public changes before execution.

Risk: Command output can contain entrant emails, survey responses, analytics, and other campaign data.

Mitigation: Treat JSON output as account data and avoid exposing it outside the intended shell, script, MCP client, or agent conversation.

Risk: The optional TOKEI_API_URL override can direct API requests and credentials to a non-default host.

Mitigation: Avoid TOKEI_API_URL unless the target host is trusted and expected.

Risk: Write operations such as publishing, entry creation, webhook changes, media changes, and list replacement can affect public campaigns or downstream notifications.

Mitigation: Read current state before writes, use media:upload for page media, and get explicit approval before public or notification-triggering actions.

Risk: Running an unpinned npx command may fetch a newer package than the reviewed release.

Mitigation: Pin npx or package installation to version 0.3.6 when the reviewed package version is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gilesdawe/skills/tokei-agent)
- [Tokei agent documentation](https://tokei.io/agent)
- [Tokei API reference](https://tokei.io/docs/api)
- [Tokei OpenAPI specification](https://tokei.io/openapi.json)
- [npm package](https://www.npmjs.com/package/tokei-agent)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON CLI or MCP results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands print JSON envelopes to stdout for agent and script consumption.]

## Skill Version(s):

0.3.6 (source: package.json, server.json, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
