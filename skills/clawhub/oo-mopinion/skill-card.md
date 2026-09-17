## Description:

Mopinion (mopinion.com). Use this skill for Mopinion requests that search and read account, deployment, dataset, report, field, and feedback data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Mopinion account information, deployments, datasets, reports, fields, and feedback through the oo CLI without directly handling Mopinion API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer scripts that are run directly in a shell.

Mitigation: Before installation, prefer a versioned package or installer with checksum or signature verification.

Risk: The skill can read Mopinion feedback and account data available through the connected OOMOL account.

Mitigation: Use a least-privileged Mopinion/OOMOL connection where possible and review retrieved data handling.

## Reference(s):

- [Mopinion homepage](https://www.mopinion.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mopinion)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON responses from the oo CLI when run with --json.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
