## Description:

Interact with GitHub through the gh CLI for issues, pull requests, CI runs, repository health reports, changelog generation, and issue triage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and repository maintainers use this skill to inspect GitHub repository health, review pull requests and workflow runs, generate changelogs, and triage open issues through the GitHub CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs gh commands using the user's existing GitHub authentication, so local output can include private repository metadata.

Mitigation: Run it only against intended repositories and use a GitHub account or token with the least access needed for the review.

Risk: Repository health, issue triage, and changelog output is read-oriented but may be incomplete when GitHub permissions or API responses are limited.

Mitigation: Treat the generated reports as review aids and confirm important release or triage decisions in GitHub before acting.

## Reference(s):

- [ClawGit Pro on ClawHub](https://clawhub.ai/northcap-group/skills/clawgit-pro)
- [Northcap Group publisher profile](https://clawhub.ai/user/northcap-group)
- [GitHub](https://github.com)
- [GitHub API endpoint](https://api.github.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and terminal text with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the gh CLI; private repository output may depend on the user's existing GitHub authentication.]

## Skill Version(s):

1.0.7 (source: release evidence; artifact frontmatter lists 1.0.1 and _meta.json lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
