## Description:

Use this skill to operate Gitea through the OOMOL oo CLI for repository, issue, pull request, release, webhook, key, label, milestone, topic, and collaborator workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Gitea schemas, run Gitea connector actions, and manage repositories, issues, pull requests, releases, hooks, keys, labels, milestones, topics, and collaborators through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path tells users to run remote installer scripts when the oo CLI is missing.

Mitigation: Install the oo CLI from verified, version-pinned vendor packages when possible, or inspect and verify installer contents before execution.

Risk: The skill can perform high-impact write and destructive changes in Gitea.

Mitigation: Require exact repository targets, action names, and payloads before approving write or destructive operations.

Risk: Live Gitea action schemas may differ from assumptions in a prompt.

Mitigation: Inspect the live action schema with the oo CLI before constructing each payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gitea)
- [Gitea product page](https://about.gitea.com/products/gitea/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Gitea icon](https://static.oomol.com/logo/third-party/Gitea.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI schema inspection commands and Gitea connector run commands that return JSON responses.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
