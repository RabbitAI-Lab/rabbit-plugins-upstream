## Description:

Use when a selective defect needs IS/IS-NOT difference analysis or a consequential option choice needs must/want weighting and adverse-consequence comparison.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tjboudreaux](https://clawhub.ai/user/tjboudreaux)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to structure Kepner-Tregoe problem analysis for selective defects and decision analysis for consequential option choices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unsupported criteria, boundaries, or scores can make the resulting analysis look more certain than the evidence warrants.

Mitigation: Require explicit IS/IS-NOT contrasts, MUST/WANT criteria, adverse consequences, and next verification steps before acting on the output.

Risk: The full method can be over-applied to trivial choices, obvious causes, or issues settled by a cheap one-shot check.

Mitigation: Use the skill's stop conditions and skip the full matrix when the cause is already verified or the option is robust enough for the stated stakes.

## Reference(s):

- [ClawHub skill release: thinking-kepner-tregoe](https://clawhub.ai/tjboudreaux/skills/thinking-kepner-tregoe)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown structured as a mode-specific analysis artifact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include IS/IS-NOT matrices, MUST/WANT score tables, adverse-consequence tables, sensitivity notes, and next verification steps.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
