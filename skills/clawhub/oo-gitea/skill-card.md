## Description:

Gitea connector for reading, creating, updating, and deleting repositories, issues, pull requests, releases, webhooks, keys, labels, milestones, branches, tags, and related data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Gitea through an OOMOL-connected account, including repository, branch, file, tag, release, issue, milestone, label, pull request, review, webhook, collaborator, key, and topic workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to execute remote installer scripts.

Mitigation: Prefer a signed or package-manager installation path, or download and review or verify the installer before running it.

Risk: The skill can perform write and destructive Gitea actions.

Mitigation: Confirm the exact target, payload, and expected effect before running any state-changing or destructive action.

Risk: Use requires connecting a Gitea account through OOMOL's service.

Mitigation: Limit Gitea permissions to the scopes needed for the task and review permissions before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-gitea)
- [Gitea Homepage](https://about.gitea.com/products/gitea/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses may include JSON data and execution metadata.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
