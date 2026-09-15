## Description:

Ringg AI lets an agent use an OOMOL-connected account to retrieve Ringg AI workspace, assistant, call, voice, and caller-number data and initiate outbound calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect Ringg AI connector schemas, retrieve Ringg AI workspace resources, and run call-related actions through an OOMOL-connected account. Outbound calls should be treated as state-changing activity and confirmed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate real outbound Ringg AI calls, which may affect users, operations, or billing.

Mitigation: Require the agent to show the exact assistant, destination number, caller number, purpose, and expected cost or billing impact, then obtain explicit user approval before initiating a call.

Risk: The setup section includes one-line remote installer commands.

Mitigation: Prefer a verified package source, or inspect and verify the installer before running curl-to-shell or PowerShell installer commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-ringg-ai)
- [Ringg AI Homepage](https://www.ringg.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions may return JSON responses containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
