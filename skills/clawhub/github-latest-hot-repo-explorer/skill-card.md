## Description:

Searches GitHub for recently created popular repositories above a configurable star threshold and summarizes the highest-star repository not previously reported.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zengzuo613](https://clawhub.ai/user/zengzuo613)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to discover one highly starred, recently created GitHub repository at a time and receive a concise explanation of what it does, the problem it addresses, and how it works.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: When GITHUB_TOKEN is absent, the script also checks ~/.openclaw/.env and may use a host credential despite the documented anonymous-access default.

Mitigation: Remove the credential-file fallback before installation. If authentication is needed, provide only an explicitly authorized token with minimal public-read permissions.

Risk: The search fetches at most the first 100 star-sorted repositories, so a qualifying repository beyond that page can be missed.

Mitigation: Treat results as best effort and check additional GitHub search pages separately when broader coverage matters.

Risk: The --dry-run option expects scripts/fixtures/items.json, which is not present in the supplied release artifact.

Mitigation: Add the fixture before using --dry-run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zengzuo613/skills/github-latest-hot-repo-explorer)
- [GitHub repository search API](https://api.github.com/search/repositories)
- [GitHub repository README API](https://api.github.com/repos/{owner}/{repo}/readme)
- [Output template](references/output_template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown summary with repository metadata and answers to three questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One repository per run; README input is limited to 8,000 characters.]

## Skill Version(s):

1.0.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
