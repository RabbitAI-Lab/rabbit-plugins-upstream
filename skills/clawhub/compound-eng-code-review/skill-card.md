## Description:

Structured code reviews with severity-ranked findings and deep multi-agent mode for reviewing code, auditing code quality, and critiquing PRs, MRs, or diffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to perform structured code reviews, audit repository changes, classify findings by severity and confidence, and decide whether a change is ready to merge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may read broad repository context, run verification commands, and use read-only subagents during review.

Mitigation: Use it only where broad repository reading is acceptable, and review command execution according to the host environment's approval controls.

Risk: Optional external reviewer delegation can transmit diffs and surrounding source to another reviewer backend.

Mitigation: Approve external dispatch only after checking the listed files and contents are acceptable to share.

Risk: A ready-to-merge result depends on complete selected-file coverage and available verification; partial or interrupted coverage can leave material issues unresolved.

Mitigation: Require the report to state scope, limitations, checks run, and coverage status before relying on a ready verdict.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-code-review)
- [Skill definition](SKILL.md)
- [Skill specification](SPEC.md)
- [Reviewer trust boundary](references/reviewer-trust-boundary.md)
- [Scope and mode selection](references/scope-and-mode-selection.md)
- [Scope and comparison-range resolution](references/scope-resolution.md)
- [Standard review process](references/standard-review-process.md)
- [Deep review process](references/deep-review.md)
- [Severity levels and confidence rubric](references/severity-and-confidence.md)
- [Report and integration](references/report-and-integration.md)
- [External reviewer subprocess](references/external-review-subprocess.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown review report with severity-ranked findings, file and line citations, residual risks, and optional shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are scoped to the selected files and reported checks; external reviewer dispatch requires explicit egress consent.]

## Skill Version(s):

4.6.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
