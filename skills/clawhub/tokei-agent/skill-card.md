## Description:

Tokei-agent lets agents and command-line users manage Tokei pre-launch, waitlist, giveaway, referral, and launch campaigns through the Tokei v1 REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gilesdawe](https://clawhub.ai/user/gilesdawe)

### License/Terms of Use:

MIT

## Use Case:

Developers, operators, and AI-agent users use this skill to inspect, create, update, publish, monitor, and automate Tokei campaign pages while preserving JSON command output for scripts and MCP clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A read-write Tokei API key can change pages, entries, media, and webhooks.

Mitigation: Use a read-only key for monitoring and provide a read-write key only when changes are intended.

Risk: Command output can include sensitive campaign data such as emails, survey answers, and analytics.

Mitigation: Treat command output and agent transcripts as sensitive when they contain campaign or entrant data.

Risk: Public-facing writes, webhook changes, and entry imports can affect entrants or third parties.

Mitigation: Confirm these actions with a human before running them.

Risk: Broad request bodies passed with --data can send more fields than the command name alone implies.

Mitigation: Review --data payloads carefully before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gilesdawe/skills/tokei-agent)
- [Tokei Agent Docs](https://tokei.io/agent)
- [Tokei API Reference](https://tokei.io/docs/api)
- [npm Package](https://www.npmjs.com/package/tokei-agent)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, MCP configuration examples, and JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON envelopes for non-interactive agent, script, CI, and MCP use.]

## Skill Version(s):

0.3.5 (source: package.json, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
