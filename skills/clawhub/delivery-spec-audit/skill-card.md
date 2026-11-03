## Description:

Audits a completed coding task by comparing its requirements with session or repository evidence, then reports coverage, gaps, and concrete counterexamples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill before reporting a development task complete to compare the task requirements with an available session log or repository evidence. It produces a numbered coverage matrix, verification summary, counterexamples for suspected gaps, and follow-up actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The report may treat an attempted file edit as completed work when the operation failed.

Mitigation: Confirm successful tool results or inspect repository changes before treating write evidence as completion; check actual test outcomes before relying on coverage conclusions.

Risk: Reports can expose private workspace paths.

Mitigation: Review and redact sensitive paths before sharing a report outside the workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/z-zihan/skills/delivery-spec-audit)
- [Project homepage](https://github.com/z-Zihan/awesome-skills)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Markdown coverage report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Numbered requirements, a coverage matrix, verification behavior summary, evidence-based counterexamples, and an action checklist. Findings depend on the session logs or repository evidence available.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
