## Description:

Finds the highest-star GitHub repositories within a configurable creation window and summarizes their metadata and README content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zengzuo613](https://clawhub.ai/user/zengzuo613)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to discover high-star GitHub repositories created within a configurable time window. It turns repository metadata and README content into a concise, structured Markdown report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: This release can retrieve a saved GitHub token from ~/.openclaw/.env even when GITHUB_TOKEN is unset.

Mitigation: Choose a version that removes the saved-token fallback. Public discovery can run anonymously; if a token is needed, supply it explicitly with minimal permissions.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/zengzuo613/skills/github-latest-hot-repo-explorer)
- [GitHub Token Configuration](references/README.md)
- [Output Template](references/output_template.md)

## Skill Output:

**Output Type(s):** [Markdown, Analysis]

**Output Format:** [Markdown report with repository metadata and concise project analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Selects and reports one repository per run, with configurable star and recency filters.]

## Skill Version(s):

1.0.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
