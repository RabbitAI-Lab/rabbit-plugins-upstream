## Description:

Callingly (callingly.com). Use this skill for Callingly requests that read, create, update, and delete data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to operate Callingly through an OOMOL-connected account, including listing and retrieving calls, leads, teams, agents, and schedules, plus creating calls and updating or deleting leads when approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Prefer manually downloading and verifying the OOMOL oo CLI installer before running it.

Risk: The skill can create calls and update or delete Callingly leads.

Mitigation: Review the live action schema, exact payload, target record, and expected effect before approving write or destructive actions.

Risk: The oo CLI operates against the user's connected Callingly account.

Mitigation: Install and use the skill only when OOMOL is trusted to broker access to the connected Callingly account.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-callingly)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Callingly Homepage](https://callingly.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Callingly App Connection](https://console.oomol.com/app-connections?provider=callingly)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
