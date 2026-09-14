## Description:

Compares multiple contracts based on the same template by splitting and aligning clauses, then reporting missing, extra, and changed clause text with source excerpts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Legal, procurement, audit, and operations teams use this skill to mechanically compare contracts signed from the same template, identify missing or added clauses, and review clause text differences with original excerpts. It is intended for comparison support, not legal advice or a complete contract review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat mechanical clause differences as legal advice or a complete contract review.

Mitigation: Use the output as comparison support only, and have qualified legal or business reviewers decide legal meaning, risk, and next actions.

Risk: Broad legal trigger terms could lead an agent beyond the skill's intended clause-comparison scope.

Mitigation: Keep use focused on same-template clause alignment, missing clauses, and text differences; route broader legal analysis to appropriate review processes.

Risk: Insufficient or poorly structured contract input can prevent meaningful comparison.

Mitigation: Provide at least two contracts with substantive text and clause headings; the skill should report insufficient input rather than inventing a conclusion.

Risk: Textually similar clauses may still differ in legal effect, and textually different clauses may require contextual interpretation.

Mitigation: Review source excerpts manually and do not rely on the tool for semantic equivalence or enforceability judgments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chenqg618/skills/contract-comparison-free)
- [Publisher Profile](https://clawhub.ai/user/chenqg618)
- [Free Web Checker](https://www.tokendidi.cn/check)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown text with optional JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally and can emit JSON with --json; refuses conclusions when input is insufficient.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
