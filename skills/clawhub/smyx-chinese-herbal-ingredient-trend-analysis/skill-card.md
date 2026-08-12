## Description:

Assesses medicinal herb leaf images or videos for visual indicators associated with active-ingredient accumulation, compares them with cultivar reference features, and returns a Low, Medium, High, or Peak trend level with harvest-timing guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users in Chinese medicinal herb planting bases, GAP bases, cooperatives, and pharmaceutical raw-material operations use this skill to evaluate leaf imagery and estimate harvest readiness. The result is decision support only and should be paired with formal chemical or pharmacopeia testing for quality certification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive herb images, drone footage, farm operations, or report history may be sent to remote lifeemergence.com services.

Mitigation: Review data sensitivity and obtain appropriate approval before using the skill with proprietary, regulated, or confidential media.

Risk: The skill may automatically create or reuse an account identity and store identity or token data locally.

Mitigation: Run it in a controlled workspace, inspect local data storage after use, and clear stored identity or token data when it is no longer needed.

Risk: The visual trend assessment is decision support and is not a substitute for chemical quality testing.

Mitigation: Use formal HPLC, national-standard, pharmacopeia, or equivalent professional testing for official herb quality determinations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-chinese-herbal-ingredient-trend-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [analysis, markdown, json, shell commands, guidance]

**Output Format:** [Markdown and JSON-like structured report text, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include trend level, visual-feature assessment, recommendations, historical report listings, and report export links.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
