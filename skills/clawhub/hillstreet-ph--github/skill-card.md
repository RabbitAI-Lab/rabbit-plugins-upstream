## Description:

GitHub CLI for issues, PRs, CI/check logs, comments, reviews, releases, repos, and gh api queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill with GitHub CLI to inspect and manage issues, pull requests, CI runs, reviews, releases, and repository data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Adding a runtime session URL to a pull request can disclose session information.

Mitigation: Before publishing the URL, confirm it is appropriate to share; include it only when the runtime provides the exact session URL, as the skill directs.

Risk: The available security evidence is incomplete because a referenced local path could not be matched to a bundled artifact.

Mitigation: Review the complete source and any unmatched referenced files before relying on the security assessment.

## Reference(s):

- [GitHub skill on ClawHub](https://clawhub.ai/hillstreet-ph/skills/github)
- [Publisher profile](https://clawhub.ai/user/hillstreet-ph)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and guidance use the repository, issue, pull request, or run identifiers supplied for the task.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
