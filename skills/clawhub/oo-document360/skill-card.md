## Description:

Document360 lets an agent search and read Document360 workspaces through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent list Document360 workspaces and articles, retrieve category hierarchies, and search workspace content through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote curl and PowerShell installer commands for the oo CLI.

Mitigation: Prefer a verified or package-manager installation path, and review installer commands before execution.

Risk: The skill can access Document360 data through OOMOL's connector using server-side credentials.

Mitigation: Install only for trusted workspaces, confirm account connection steps, and ensure the connected Document360 account has appropriate access scope.

## Reference(s):

- [Document360 homepage](https://document360.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-document360)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running actions; responses may include Document360 workspace, article, category, and search result data.]

## Skill Version(s):

1.0.3 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
