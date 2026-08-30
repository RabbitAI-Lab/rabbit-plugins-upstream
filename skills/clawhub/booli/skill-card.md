## Description:

Search and analyze Swedish real estate on booli.se, including active for-sale listings, sold prices, area resolution, and market statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and real-estate analysts use this skill to search Swedish property listings, review sold-price comparables, resolve Booli area IDs, and summarize market statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a browser bridge and Transporter extension to access Booli through a user-controlled browser tab.

Mitigation: Install only if comfortable with that bridge, keep a Booli tab open deliberately, and treat the extension as a separate trust decision.

Risk: Property-market summaries can be misleading when based on thin samples or stale listings.

Mitigation: Check sample size, sold dates, pagination, and source listings before using results for financial or property decisions.

Risk: The skill returns real-estate information but does not modify accounts, files, or property data.

Mitigation: Use it for read-only lookup and analysis, and review outputs before taking external action.

## Reference(s):

- [Booli website](https://www.booli.se)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/booli)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text property-search summaries, sold-price comparisons, area IDs, and market statistics.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results use SEK for prices, m2 for areas, numeric room counts, and paginated result summaries when applicable.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
