## Description:

Gitea (about.gitea.com). Use this skill for ANY Gitea request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and repository operators use this skill to manage Gitea repositories, issues, pull requests, releases, webhooks, deploy keys, and related collaboration workflows through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback installer can execute remote installation code directly.

Mitigation: Use a verified oo CLI installation path and review installation commands before execution.

Risk: Write and destructive Gitea actions can change or delete repository data.

Mitigation: Require explicit user approval for the exact target and payload before running any write or destructive action.

Risk: The skill acts through an OOMOL-connected Gitea account.

Mitigation: Install only when OOMOL and the connected account scope are trusted, and prefer least-privilege account access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gitea)
- [Gitea product page](https://about.gitea.com/products/gitea/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, json, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing actions should include the exact target and payload for user confirmation before execution.]

## Skill Version(s):

1.0.5 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
