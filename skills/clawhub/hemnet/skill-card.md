## Description:

Search and analyse Swedish real estate on hemnet.se, including active listings, sold prices, listing details, photos, market statistics, address resolution, and Swedish mortgage calculations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to research Swedish real estate on Hemnet, compare active and sold listings, inspect listing details, and estimate Swedish monthly mortgage costs.

### Deployment Geography for Use:

Sweden

## Known Risks and Mitigations:

Risk: The skill is Sweden-specific and may present property information using Swedish market conventions that are unfamiliar outside that market.

Mitigation: Use it for Swedish property questions and confirm SEK, m2, tenure, fee, and amortization assumptions before relying on results.

Risk: Broad Swedish housing requests may activate Hemnet-focused behavior when the user wanted general housing advice.

Mitigation: State whether the task should use Hemnet data or broader housing guidance, especially for non-listing questions.

Risk: Market statistics can be misleading when sold-listing sample sizes are thin.

Mitigation: Check sample_size and corroborate thin medians or averages against comparable listings before using them for valuation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/hemnet)
- [Hemnet](https://hemnet.se)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or concise text with property data, comparisons, URLs, and calculation results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Swedish market conventions such as SEK, m2, bostadsratt, avgift, slutpriser, and amorteringskrav.]

## Skill Version(s):

1.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
