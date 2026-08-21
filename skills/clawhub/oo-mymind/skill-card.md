## Description:

mymind lets agents read, create, update, and delete mymind data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to work with a connected mymind account, including search, reading saved content, creating notes and spaces, tagging objects, and updating or removing stored data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and change data in a connected mymind account.

Mitigation: Install only when account access is intended, and review write requests before approval.

Risk: Write and destructive actions can modify, remove, or overwrite mymind content.

Mitigation: Confirm the exact target, payload, and expected effect before approving write or destructive actions.

Risk: Setup commands could initiate authentication or connector changes when they are not needed.

Mitigation: Use oo CLI setup steps only after a command reports a missing CLI, authentication, or connection problem.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mymind)
- [mymind Homepage](https://mymind.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Markdown, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
