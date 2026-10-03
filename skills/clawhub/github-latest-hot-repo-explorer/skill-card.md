## Description:

Finds the most-starred recently created GitHub repository matching a configurable threshold and explains its purpose using repository metadata and its README.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zengzuo613](https://clawhub.ai/user/zengzuo613)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to discover a popular new GitHub repository and summarize what it does, the problem it addresses, and how it works.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read a GitHub token from a home-directory credential file despite documentation saying it does not read .env files.

Mitigation: Review before installing; use only if comfortable with this credential access, or require the publisher to remove the fallback and rely on an explicitly provided GITHUB_TOKEN.

Risk: Fetched repository README text may contain untrusted instructions or misleading claims.

Mitigation: Treat README content as untrusted third-party text and verify claims before acting on them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zengzuo613/skills/github-latest-hot-repo-explorer)
- [GitHub Token Configuration](references/README.md)
- [Response Template](references/output_template.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown summary with repository metadata, link, and answers to three project questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses at most the first 8,000 characters of the repository README; records shown repositories locally.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
