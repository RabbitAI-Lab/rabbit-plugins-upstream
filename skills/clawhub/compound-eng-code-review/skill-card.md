## Description:

Structured code reviews with severity-ranked findings and deep multi-agent mode for reviewing code, auditing code quality, and critiquing PRs, MRs, or diffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to perform structured code review, identify correctness, security, reliability, and test-gate issues, and report severity-ranked findings with scope and coverage notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads repository source, diffs, git history, CI configuration, and documentation while performing reviews.

Mitigation: Use it only in repositories where that review access is intended, and keep sensitive files outside the selected review scope when they are not needed.

Risk: External CLI reviewer dispatch can send named diff or file context to another provider.

Mitigation: Approve external reviewer dispatch only after confirming the provider and the exact context being sent are acceptable.

Risk: Review findings and merge-readiness verdicts can be incomplete when selected-file coverage or checks are partial.

Mitigation: Require the final report to state scope, covered files, skipped checks, and residual risks before relying on its verdict.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-code-review)
- [Publisher profile](https://clawhub.ai/user/iliaal)
- [Standard review process](references/standard-review-process.md)
- [Deep review process](references/deep-review.md)
- [Reviewer trust boundary](references/reviewer-trust-boundary.md)
- [Severity and confidence rubric](references/severity-and-confidence.md)
- [Language-specific review profiles](references/language-profiles.md)
- [Action routing](references/action-routing.md)
- [Review report and integration](references/report-and-integration.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown review report with severity-ranked findings, scope and coverage notes, check results, residual risks, and merge-readiness verdicts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CR-XXX finding identifiers, file and line citations, skipped-check disclosures, and external-review consent requirements.]

## Skill Version(s):

4.5.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
