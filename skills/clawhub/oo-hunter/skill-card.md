## Description:

Hunter (hunter.io) enables an agent to read, create, update, and delete Hunter account data through the OOMOL-connected oo CLI instead of calling the Hunter API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent perform Hunter account, enrichment, domain search, email finding, verification, discovery, and lead-management workflows through an OOMOL-connected Hunter account. The skill is intended for both read operations and user-confirmed write or destructive lead-management actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags fallback setup guidance that tells an agent to run unverified remote installer scripts directly.

Mitigation: Install the oo CLI only through a verified, user-controlled process; do not allow an agent to automatically run remote installer commands.

Risk: The skill can create, update, upsert, or delete Hunter lead data.

Mitigation: Require explicit user confirmation of the target payload and expected effect before any write or destructive Hunter action runs.

Risk: Hunter account data flows through the OOMOL connector.

Mitigation: Use the skill only when the operator trusts OOMOL and the connected Hunter account data path.

## Reference(s):

- [ClawHub Hunter skill page](https://clawhub.ai/oomol/skills/oo-hunter)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Hunter homepage](https://hunter.io)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI connector schema and run commands; state-changing Hunter actions require user confirmation before execution.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
