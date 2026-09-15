## Description:

Moesif provides schema-first guidance for running Moesif read actions through an OOMOL-connected account with the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and support engineers use this skill to inspect Moesif workspace and app information, including apps, workspaces, workspace templates, and individual workspaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include curl and PowerShell pipe commands that execute a remote installer without built-in verification.

Mitigation: Use an official signed package or separately downloaded installer with checksum or signature verification before installing the oo CLI.

Risk: Normal operation accesses Moesif data through OOMOL using the user's connected account.

Mitigation: Confirm the connected OOMOL account and Moesif workspace are appropriate before running connector actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-moesif)
- [Moesif Homepage](https://www.moesif.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON when the documented --json flag is used.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
