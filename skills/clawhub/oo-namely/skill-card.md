## Description:

Namely enables an agent to inspect Namely connector schemas and retrieve accessible employee profile data through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, HR operators, and developers use this skill to read Namely profile records, profile field definitions, and the current connected Namely profile when an OOMOL account connection is available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive HR profile data from Namely.

Mitigation: Install only for trusted OOMOL and Namely connections, use least-privilege access, and avoid broad employee-profile listing unless needed.

Risk: The setup guidance includes remote installer commands.

Mitigation: Independently verify installer source and integrity before running curl|bash or irm|iex commands.

## Reference(s):

- [ClawHub Namely skill page](https://clawhub.ai/oomol/skills/oo-namely)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Namely homepage](https://www.namely.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and a meta.executionId value.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
