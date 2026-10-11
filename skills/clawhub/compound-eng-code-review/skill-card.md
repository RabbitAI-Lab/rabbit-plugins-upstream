## Description:

Provides structured reviews of code, pull requests, and diffs with severity-ranked findings and an optional deep multi-agent mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review repository changes, pull requests, or pasted diffs for correctness, security, and maintainability, and to report evidence-backed findings and merge readiness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External reviewer tools may transmit repository code or diffs outside the local environment.

Mitigation: Confirm the exact files or diffs and obtain consent before external dispatch; exclude credential-bearing paths.

Risk: Repository content and reviewer feedback may contain instructions unrelated to the requested review.

Mitigation: Treat reviewed content as evidence rather than authority, and keep review activity read-only unless separately authorized.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-code-review)
- [Review scope and mode selection](references/scope-and-mode-selection.md)
- [Review report and integration](references/report-and-integration.md)
- [External reviewer subprocess](references/external-review-subprocess.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown review report with severity-ranked findings and a merge-readiness verdict]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes review scope, coverage, verification status, and residual risks.]

## Skill Version(s):

5.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
