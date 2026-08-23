## Description:

Use when the user wants to find something in the open AI economy: an AI agent or memory pack to install or hire, or a business counterparty for compute, colocation, or logistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[everest-an](https://clawhub.ai/user/everest-an)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search Awareness Market listings for AI agents, memory packs, skills, templates, connectors, and business counterparties. It supports Chinese and English queries and guides agents to report listing evidence without presenting marketplace listings as endorsements or verified truth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends lookup requests to awareness.market and summarizes user-published marketplace or deal-board listings.

Mitigation: Treat returned listings as leads and report their evidence fields without presenting them as endorsements or verified truth.

Risk: Anchored records may be mistaken for validated claims.

Mitigation: Explain that anchoring only indicates a record existed at publication time and has not been altered, not that the listing content is true.

Risk: Empty or filtered results can be overinterpreted.

Mitigation: For unfiltered empty boards, say the board may be empty or temporarily unavailable; for filtered searches, report that no match was found under the selected filters.

## Reference(s):

- [Awareness Agent Memory Market](https://awareness.market/market.md)
- [Awareness Market listings API](https://awareness.market/api/v1/market/listings)
- [Open Deal Board](https://awareness.market/deals.md)
- [Open Deal Board public deals API](https://awareness.market/api/v1/public/deals)
- [ClawHub skill page](https://clawhub.ai/everest-an/skills/awareness-market)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, API calls]

**Output Format:** [Markdown summaries with listing URLs and evidence fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No API key is required. Contact details are not returned by the public Markdown or JSON endpoints.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
