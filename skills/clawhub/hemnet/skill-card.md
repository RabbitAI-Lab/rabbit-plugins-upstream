## Description:

Search and analyze Swedish real estate on hemnet.se, including active listings, sold prices, listing details, photos, market statistics, address resolution, and Swedish mortgage calculations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents assisting Swedish property seekers use this skill to search Hemnet listings, compare live and sold properties, retrieve listing details and photos, calculate Swedish mortgage costs, and summarize market statistics. It is intended for Swedish housing questions, including bostader, lagenheter, villor, and slutpriser.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Address or housing-search details provided by a user may be used to query Hemnet public data.

Mitigation: Share only details needed for the search and verify important results against Hemnet and applicable terms before relying on them.

Risk: Market statistics and derived values such as price per square meter can be misleading when source data is sparse or incomplete.

Mitigation: Check sample size, compare multiple listings or sold-price records, and treat calculations as decision support rather than a valuation guarantee.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text with structured property-search results, comparisons, market summaries, and calculator outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SEK, square meters, numeric room counts, and Hemnet location IDs when presenting real-estate results.]

## Skill Version(s):

0.6.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
