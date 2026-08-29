## Description:

Search and analyse Swedish real estate on booli.se, including active for-sale listings, sold prices, area resolution, and market statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to answer Swedish real-estate questions with Booli listing, sold-price, area, and market-statistics data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Booli requests may use the Transporter browser bridge through the user's own browser session.

Mitigation: Approve pairing only for the expected Booli tab and treat the bridge as a browser-session integration.

Risk: Market-statistics summaries can be misleading when based on a small sample.

Mitigation: Check the reported sample size before relying on medians, averages, or over-under asking percentages.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/booli)
- [Booli](https://www.booli.se)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text responses with structured real-estate data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include prices in SEK, area in square meters, room counts, dates, and sample-size cautions for market statistics.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
