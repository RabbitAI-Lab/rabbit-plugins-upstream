## Description:

Structured code reviews with severity-ranked findings and deep multi-agent mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering reviewers use this skill to review code, audit quality and security risks, and critique PR, MR, or diff changes with severity-ranked findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags ungated behavior that may persistently edit reviewer guidance during ordinary reviews.

Mitigation: Remove or gate that behavior so updates to review-traps-catalog.md require explicit maintenance approval.

Risk: The skill may consult project documentation, run authorized project checks, and use read-only specialist agents during reviews.

Mitigation: Use it only where those review actions are permitted, and require separate authority for any source, VCS, or external writes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-code-review)
- [Action Routing](artifact/references/action-routing.md)
- [Check Categories](artifact/references/check-categories.md)
- [Deep Review](artifact/references/deep-review.md)
- [False Positive Suppression](artifact/references/false-positive-suppression.md)
- [Language Profiles](artifact/references/language-profiles.md)
- [Reliability Patterns](artifact/references/reliability-patterns.md)
- [Reviewer Trust Boundary](artifact/references/reviewer-trust-boundary.md)
- [Scope Resolution](artifact/references/scope-resolution.md)
- [Security Patterns](artifact/references/security-patterns.md)
- [Severity and Confidence](artifact/references/severity-and-confidence.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Markdown review with severity-ranked findings, residual risks, and verdict]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include file and line references, confidence scores, and action-routing labels.]

## Skill Version(s):

4.4.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
