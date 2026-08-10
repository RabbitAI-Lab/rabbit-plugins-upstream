## Description:

tokei-agent lets agents and command-line users manage Tokei pre-launch, waitlist, giveaway, referral, launch, webhook, and analytics workflows through the Tokei v1 REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gilesdawe](https://clawhub.ai/user/gilesdawe)

### License/Terms of Use:

MIT

## Use Case:

Developers, marketers, and operations teams use this skill to let an agent inspect, create, update, publish, monitor, and automate Tokei campaign pages while keeping human approval around public or entrant-impacting changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A read+write Tokei API key can let an agent change live campaigns, publish pages, create webhooks, upload media, or add entries.

Mitigation: Use a read-only TOKEI_API_KEY for reporting and monitoring; provide a read+write key only for workflows that need changes and require explicit approval before public or entrant-impacting actions.

Risk: API responses can include entrant emails, survey answers, analytics, and other campaign data that may be retained by the invoking shell, script, MCP client, or agent transcript.

Mitigation: Treat command output as personal data, limit who can see agent transcripts or logs, and avoid running broad read commands unless the task requires that data.

Risk: Bulk updates and list-valued fields such as prizes or reward thresholds can replace existing campaign configuration.

Mitigation: Read the current page state first, apply changes to the complete intended list, update once, and verify the result with a follow-up read.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gilesdawe/skills/tokei-agent)
- [Tokei agent documentation](https://tokei.io/agent)
- [Tokei API reference](https://tokei.io/docs/api)
- [npm package](https://www.npmjs.com/package/tokei-agent)
- [Agent skill reference](SKILL.md)
- [README](README.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI and MCP tools return JSON for agent consumption; most workflows require TOKEI_API_KEY.]

## Skill Version(s):

0.3.3 (source: package.json, server.json, changelog, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
