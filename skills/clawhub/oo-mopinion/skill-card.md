## Description:

Mopinion lets an agent use an OOMOL-connected account to read Mopinion account, deployment, dataset, report, field, and feedback data through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Mopinion customer feedback, form, report, deployment, and account information from a connected Mopinion account without handling raw credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes direct remote installer commands that can execute unverified code in a shell.

Mitigation: Use trusted, versioned, verifiable oo CLI installation steps and do not let an agent run curl-to-shell or Invoke-Expression installer commands automatically.

Risk: The skill uses an OOMOL-mediated Mopinion connection that can access data available to the connected account.

Mitigation: Connect Mopinion only after reviewing the account and data access being granted, and install the skill only when an OOMOL-mediated connection is intended.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mopinion)
- [Mopinion Homepage](https://www.mopinion.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before constructing JSON payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
