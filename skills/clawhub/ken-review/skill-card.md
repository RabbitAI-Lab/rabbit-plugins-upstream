## Description:

Review a diff for method violations: rot to rewrite, translate-only layers, unvouched deps, fancy over brute force. One line per finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rajnandan1](https://clawhub.ai/user/rajnandan1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to review code diffs for a narrow set of method violations, including repeated patch rot, pass-through layers, unvouched dependencies, unnecessary cleverness, and process ceremony. It produces concise findings and summary metrics rather than applying fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is intentionally narrow and can omit correctness, security, and performance issues.

Mitigation: Use it as a focused method-violation pass and route broader review concerns to a normal review pass.

Risk: Ordinary surrounding text may contain phrases that exit the skill's concise review mode.

Mitigation: Confirm the intended review mode when prompts or diffs include phrases such as stop ken-review or normal mode.

## Reference(s):

- [Project homepage](https://github.com/rajnandan1/ken)
- [ClawHub skill page](https://clawhub.ai/rajnandan1/skills/ken-review)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text review findings with line references and summary metrics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not apply fixes or run tools; output is limited to Thompson-mode method violations.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
