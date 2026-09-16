## Description:

GitLab (gitlab.com) supports reading, creating, updating, and deleting data through the OOMOL-connected GitLab connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to inspect GitLab action schemas and run GitLab connector actions for projects, issues, merge requests, and user data through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can execute remote installer scripts if the oo CLI is missing.

Mitigation: Prefer a verified, pinned, or inspectable oo CLI installation method before running remote shell or PowerShell installers.

Risk: GitLab connector actions can create, update, merge, or delete GitLab data.

Mitigation: Use a least-privilege GitLab connection and require explicit confirmation before write, merge, update, or destructive actions.

## Reference(s):

- [GitLab homepage](https://gitlab.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub GitLab skill](https://clawhub.ai/oomol/skills/oo-gitlab)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and may return JSON responses from GitLab connector actions.]

## Skill Version(s):

1.0.5 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
