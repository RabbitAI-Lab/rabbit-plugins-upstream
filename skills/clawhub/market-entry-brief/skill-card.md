## Description:

Creates an Amazon market-entry comparison brief from product-page and review evidence for a primary ASIN and authorized competitor ASINs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators and their agents use this skill to compare a target Amazon product page with authorized competitor pages and review evidence before market entry. It supports pre-entry research questions and validation checklists, not sales, margin, inventory, advertising, order, or return-rate forecasts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI API actions can spend account credits and send product identifiers plus review-analysis requests to ari.funewa.com.

Mitigation: Use the quote step first, proceed only after explicit user confirmation, and review account balance and request identifiers before running paid operations.

Risk: Server security evidence reports that the bundled CLI can request broader paid operations than the fixed market-entry workflow advertised by the skill.

Mitigation: Install only after review, restrict use to the documented page_compare/entry workflow, and avoid workflow or focus overrides outside the intended market-entry brief.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/market-entry-brief)
- [Amazon market-entry operation workflow](references/operation-workflow.md)
- [Amazon market-entry API reference](references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown brief with concise findings, evidence notes, checklists, and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit confirmation before paid API calls.]

## Skill Version(s):

1.4.11 (source: server release metadata, artifact _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
