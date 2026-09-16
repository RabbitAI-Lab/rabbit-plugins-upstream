## Description:

Feedier lets an agent read, create, update, and delete Feedier report data through the OOMOL oo connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Feedier report workflows from an agent, including listing, retrieving, creating, updating, deleting reports, and generating share links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute arbitrary code if the installer source is compromised.

Mitigation: Review the setup path before installing and prefer a pinned, verifiable release or official package-manager flow.

Risk: Write and delete actions can change or remove Feedier reports.

Mitigation: Confirm the exact Feedier report, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [Feedier ClawHub Release](https://clawhub.ai/oomol/skills/oo-feedier)
- [Feedier Homepage](https://www.feedier.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to inspect live connector schemas before forming payloads and to require confirmation for write or destructive actions.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
