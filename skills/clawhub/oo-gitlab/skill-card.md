## Description:

Provides GitLab project, issue, and merge request workflows through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to read and manage GitLab projects, issues, and merge requests from an agent session through their connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, merge, and delete GitLab resources through the connected account.

Mitigation: Confirm the exact target, payload, and expected effect before running write, merge, update, or destructive actions.

Risk: The first-time setup path includes a remote shell installer.

Mitigation: Prefer a verified package or inspect the installer and validate checksum or signature information before execution.

Risk: GitLab operations are routed through OOMOL using the connected account's granted permissions.

Mitigation: Install only when this routing model is acceptable and grant the connected account only the GitLab permissions needed for the intended workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gitlab)
- [GitLab homepage](https://gitlab.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed and authenticated oo CLI with GitLab connected through OOMOL.]

## Skill Version(s):

1.0.6 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
