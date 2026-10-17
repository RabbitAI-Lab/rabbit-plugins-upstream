## Description:

Helps agents read and manage Dynalist documents, folders, and inbox items through a connected OOMOL account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Dynalist users and teams can ask an agent to browse documents, organize files, update nodes, and manage an inbox in their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions offer a remotely downloaded script for CLI installation.

Mitigation: Install the oo CLI through a verified method; do not let an agent run the one-line installer automatically.

Risk: Dynalist access is mediated by OOMOL.

Mitigation: Use the skill only if the account owner accepts OOMOL as an intermediary.

Risk: Editing documents can overwrite or delete nodes, and batch file changes may partially fail.

Mitigation: Review targets and payloads before approving changes; explicitly confirm destructive edits and inspect batch results.

## Reference(s):

- [Dynalist](https://dynalist.io/)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)
- [Dynalist skill on ClawHub](https://clawhub.ai/oomol/skills/oo-dynalist)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance and Dynalist data returned as JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write and delete operations change the connected Dynalist account.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
