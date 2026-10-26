## Description:

Provides structured code reviews of changes and pull requests with severity-ranked findings and an optional deep multi-agent mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review repository changes, pull requests, or pasted diffs for correctness, security, reliability, and test coverage before merging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository files, diffs, history, and test configuration may contain sensitive information.

Mitigation: Review access and scope before use; keep review-only work read-only and avoid including secrets in findings.

Risk: Optional external review may share a diff, source excerpts, or logs with another provider.

Mitigation: Require informed approval before dispatch, inspect the described packet, and exclude sensitive files and credentials.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-code-review)
- [Review scope and mode selection](references/scope-and-mode-selection.md)
- [Reviewer trust boundary](references/reviewer-trust-boundary.md)
- [External review protocol](references/external-review-subprocess.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown review report with severity-ranked findings, coverage limitations, and a merge verdict]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Finding identifiers and evidence-backed recommendations; no source changes in review-only mode]

## Skill Version(s):

5.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
