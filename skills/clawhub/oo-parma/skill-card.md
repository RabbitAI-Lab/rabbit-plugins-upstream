## Description:

Parma (parma.ai) lets an agent read, create, update, and delete data in a connected Parma workspace through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Users with an OOMOL-connected Parma account use this skill to inspect and manage Parma relationships, notes, groups, deals, pipelines, stages, and users from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and change data in a connected Parma workspace.

Mitigation: Install it only when agent access to the connected Parma workspace is intended.

Risk: Write and destructive actions can create, update, delete, or remove Parma records.

Mitigation: Review the exact payload, target, and expected effect before approving write or destructive actions.

## Reference(s):

- [ClawHub Parma Skill](https://clawhub.ai/oomol/skills/oo-parma)
- [Parma Homepage](https://parma.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the OOMOL oo CLI connector and may return JSON responses from Parma actions.]

## Skill Version(s):

1.0.0 (source: server evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
