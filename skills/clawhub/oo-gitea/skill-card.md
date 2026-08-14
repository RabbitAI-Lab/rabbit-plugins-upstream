## Description:

Gitea (about.gitea.com). Use this skill for ANY Gitea request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and repository maintainers use this skill to manage Gitea repositories, issues, pull requests, releases, webhooks, deploy keys, branches, files, and related project metadata through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform write and destructive Gitea operations through the user's OOMOL-connected account.

Mitigation: Review the exact action, target repository or resource, and JSON payload before approving write or destructive actions.

Risk: Repository deletion, file changes, collaborator changes, webhooks, and deploy keys can materially affect project security or availability.

Mitigation: Require explicit confirmation for destructive or permission-changing actions and verify the live connector schema before execution.

## Reference(s):

- [ClawHub Gitea skill page](https://clawhub.ai/oomol/skills/oo-gitea)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Gitea homepage](https://about.gitea.com/products/gitea/)
- [Gitea metadata icon](https://static.oomol.com/logo/third-party/Gitea.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and returns connector responses as JSON when actions run.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
