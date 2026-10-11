## Description:

Reviews plans, specifications, ADRs, and other documents for clarity, completeness, scope, and accuracy against available code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review brainstorms, plans, specifications, and ADRs before the next workflow step, checking structure and claims against available source code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reviewing document claims may require reading nearby source files.

Mitigation: Use only with documents and source files the agent is authorized to access.

Risk: Document changes could alter intended requirements or decisions.

Mitigation: Review findings first and permit edits only when requested or approved.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/iliaal/skills/compound-eng-document-review)
- [Optional reader test](references/reader-test.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown review findings and suggested changes; document edits when authorized]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Highlights a critical improvement and distinguishes verified from unverified claims.]

## Skill Version(s):

5.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
