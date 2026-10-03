## Description:

Connects an agent to Google Calendar and Meet to manage events, invitations, meeting spaces, and call history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Developers and users connect an agent to their Google account to schedule and manage calendar events and work with Google Meet spaces and calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calendar changes and meeting actions can disrupt schedules; ending a Meet conference can proceed without an enforced confirmation gate.

Mitigation: Require explicit user approval before mutating events or ending meetings; set GOG_READONLY=1 when write access is unnecessary.

Risk: Authentication tools and optional Zoom integration may expose account or conferencing credentials to an agent.

Mitigation: Use only a trusted Google account, protect OAuth and Zoom credentials, and limit GOG_FILE_ROOTS to necessary directories.

Risk: The full set of exposed tools includes high-impact actions not fully described in the short skill instructions.

Mitigation: Review manifest.json and restrict tool access before deploying to shared or unattended agents.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/gogcli-mcp-calendar)
- [gogcli dependency documentation](https://github.com/openclaw/gogcli)

## Skill Output:

**Output Type(s):** [Text, Configuration guidance, Shell commands]

**Output Format:** [Plain text tool results and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Calendar and meeting results depend on the selected Google account and its permissions.]

## Skill Version(s):

4.6.1 (source: ClawHub release, package.json, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
