## Description:

Analyze a GitHub pull request for mergeability by assessing technical, architectural, process, social, and compliance factors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tag-assistant](https://clawhub.ai/user/tag-assistant)

### License/Terms of Use:


## Use Case:

Developers and engineering teams use this skill to evaluate whether a GitHub pull request is likely to be merged and to identify the concrete blockers, strengths, and next actions that affect acceptance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads pull request metadata, review comments, checks, changed files, and recent author history using the configured GitHub CLI access.

Mitigation: Use it only with repositories and pull requests whose discussion and metadata are appropriate for agent-assisted analysis.

Risk: Mergeability predictions can be incomplete or misleading when GitHub API calls fail, rate limits apply, or repository-specific review norms are not visible in the available data.

Mitigation: Treat the report as decision support and verify important blockers, approvals, CI status, and policy requirements in GitHub before acting.

## Reference(s):

- [PR Rejection Vector Taxonomy](references/rejection-taxonomy.md)
- [Merge Check on ClawHub](https://clawhub.ai/tag-assistant/skills/merge-check)
- [Publisher Profile](https://clawhub.ai/user/tag-assistant)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with a mergeability score, risk factors, strengths, recommendations, and a verdict; the bundled script emits JSON for analysis.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report depends on GitHub PR metadata, checks, reviews, comments, changed files, repository metadata, and recent author history available through the GitHub CLI.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
