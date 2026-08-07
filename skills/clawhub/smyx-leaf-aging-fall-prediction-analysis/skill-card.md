## Description:

Analyzes fixed-angle indoor plant image or video sequences to detect leaf aging signals and predict likely leaf-fall risk windows over the next 3-7 days.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, plant-care operators, and developers use this skill to analyze continuous indoor plant imagery, estimate aging indicators, identify at-risk leaves, and receive directional care guidance before likely leaf drop.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant image or video content, remote URLs, identity metadata, and report-history requests may be sent to lifeemergence.com services.

Mitigation: Use the skill only when account-linked cloud processing is acceptable, and avoid submitting sensitive plant-location or environment media.

Risk: The skill may silently create or reuse an identity and persist session tokens locally.

Mitigation: Review or clear the workspace data database and tokens before and after use when account reuse or retained history is not desired.

Risk: Leaf-fall predictions and care suggestions may be incorrect or incomplete.

Mitigation: Treat results as plant-care guidance, confirm against observed plant conditions, and avoid relying on the skill for specific chemical treatment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-leaf-aging-fall-prediction-analysis)
- [Leaf aging API documentation](artifact/references/api_doc.md)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report with risk indicators, care suggestions, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save report output to a user-specified file.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata; artifact frontmatter says 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
