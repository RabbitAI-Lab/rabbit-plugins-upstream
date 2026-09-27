## Description:

Reviews plans, specs, ADRs, and other documents for clarity, completeness, structure, and claims that can be checked against project sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document authors use this skill to find gaps, unclear decisions, and inaccurate claims before a brainstorm, plan, specification, or ADR moves to the next step. It suggests focused improvements and edits documents only when requested or approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Review findings may rely on incomplete or inaccurate project context.

Mitigation: Check claims against relevant project sources and identify any claims outside the review's coverage as unverified.

Risk: Document edits could change decisions or requirements without the author's consent.

Mitigation: Provide findings without editing on review-only requests; edit only when requested or approved.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/iliaal/skills/compound-eng-document-review)
- [Optional reader test](references/reader-test.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Text or Markdown review findings; targeted document revisions when authorized]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Checks source-backed claims and highlights the most important improvement.]

## Skill Version(s):

5.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
