## Description:

Guides structured reviews of code changes, pull requests, and diffs with severity-ranked findings and an optional deep multi-agent review mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review code, pull requests, and diffs for correctness, security, and reliability issues and report evidence-backed findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad review scope can expose private or regulated source material to external reviewer tools.

Mitigation: Keep review scope explicit and require user approval before external dispatch; do not send sensitive diffs to another vendor.

Risk: Delegated or incomplete reviews can miss changed files or overstate readiness.

Mitigation: Track coverage of every selected file and disclose any unreviewed paths or checks before giving a merge verdict.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/iliaal/skills/compound-eng-code-review)
- [Review scope and mode selection](artifact/references/scope-and-mode-selection.md)
- [Standard review process](artifact/references/standard-review-process.md)
- [Deep review](artifact/references/deep-review.md)
- [Reviewer trust boundary](artifact/references/reviewer-trust-boundary.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown review with severity-ranked findings and a merge-readiness verdict]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes review scope, evidence, checks performed, and residual risks when applicable.]

## Skill Version(s):

5.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
