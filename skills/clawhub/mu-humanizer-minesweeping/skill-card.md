## Description:

Helps writers polish Chinese or English natural-language text through scene anchoring, style calibration, evidence-conserving rewrites, fidelity auditing, and Chinese written-risk scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[muippt](https://clawhub.ai/user/muippt)

### License/Terms of Use:

MIT

## Use Case:

External writers, editors, marketers, and business teams use this skill to make natural-language copy clearer while preserving source facts, numbers, scope, and qualifiers. It also flags Chinese written-language risks for human review instead of making automatic replacements for sensitive wording.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested rewrites could alter meaning if accepted without review.

Mitigation: Review the per-item diffs before accepting edits and rely on the fidelity audit to revert changes that drift from the source.

Risk: Chinese written-risk scanning can be mistaken for legal, policy, or multilingual compliance review.

Mitigation: Treat scan findings as editorial guidance and send high-sensitivity or compliance-critical text to qualified reviewers.

Risk: Private-rule management can change local rule files after user confirmation.

Mitigation: Use scan-only mode when rewriting is not wanted and review proposed private-rule changes before confirming them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/muippt/skills/mu-humanizer-minesweeping)
- [Landing page](https://muippt.github.io/mu-humanizer-minesweeping/)
- [Chinese AI expression patterns](references/zh-patterns.md)
- [English expression patterns](references/en-patterns.md)
- [AI argument tics](references/ai-tics.md)
- [Editing policy](references/edit-policy.md)
- [Fidelity audit](references/fidelity-audit.md)
- [Written taboo rules](references/written-taboo-rules.md)
- [Thresholds](references/thresholds.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report with rewritten text, per-item diffs, editing benefits, anchor sources, fidelity audit results, and untreated signals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not directly write back to source documents; private-rule changes require explicit user confirmation.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
