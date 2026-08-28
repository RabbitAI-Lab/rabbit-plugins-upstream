## Description:

Search and analyse Swedish real estate on booli.se, including active for-sale listings, sold prices (slutpriser), area resolution, and market statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and real estate researchers use this skill to search Swedish property listings, compare sold prices, resolve Booli area IDs, and inspect market statistics through Booli.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a browser tab and Transporter bridge to access Booli through the user's browser context.

Mitigation: Only approve bridge pairing when intending to run Booli searches, and keep the www.booli.se tab open only for that use.

Risk: Market statistics can be unreliable when based on a small sample size.

Mitigation: Check sample_size before relying on medians, averages, or over-under asking price percentages.

## Reference(s):

- [Booli](https://www.booli.se)
- [ClawHub booli skill page](https://clawhub.ai/chrischall/skills/booli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text summaries of search results, listing details, sold-price comparables, market statistics, and diagnostics.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only outputs; prices are in SEK, areas are in square meters, and dates follow the source data.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
