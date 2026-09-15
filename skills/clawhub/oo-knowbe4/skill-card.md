## Description:

KnowBe4 (knowbe4.com). Use this skill for ANY KnowBe4 request - searching and reading data. Whenever a task involves KnowBe4, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external operators, and developers use this skill to retrieve KnowBe4 account, user, and group data through an OOMOL-connected account without handling raw API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path asks users to run remote installer scripts directly in a shell.

Mitigation: Review the installer first, prefer a signed or package-manager install if available, and avoid elevated shells.

Risk: The skill depends on an OOMOL-connected account and server-side credential handling.

Mitigation: Confirm the KnowBe4 connection, scopes, and account context before relying on returned data.

## Reference(s):

- [KnowBe4 homepage](https://www.knowbe4.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-knowbe4)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent to inspect live connector schemas before issuing read-only KnowBe4 actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
