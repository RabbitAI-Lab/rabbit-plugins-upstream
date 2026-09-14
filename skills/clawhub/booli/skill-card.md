## Description:

Search and analyse Swedish real estate on booli.se, including active for-sale listings, sold prices (slutpriser), area resolution, and market statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to answer Swedish real-estate questions by searching Booli areas, active listings, sold-price comparables, listing details, and market statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use the user's active browser context through the Transporter extension to fetch Booli data.

Mitigation: Use a normal Booli browser tab intentionally opened for this workflow, understand the one-time pairing prompt, and keep the skill limited to Swedish property lookup tasks.

Risk: Broad housing-related trigger wording could activate the skill during ordinary housing conversation.

Mitigation: Narrow the trigger wording or invocation policy when deployment should be limited to explicit Booli or Swedish property lookup requests.

Risk: Market statistics based on small samples can be misleading.

Mitigation: Check the returned sample size before relying on medians, averages, or over-under asking percentages.

## Reference(s):

- [Booli Skill Page](https://clawhub.ai/chrischall/skills/booli)
- [Booli](https://www.booli.se)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Markdown or plain text summaries with property data and suggested tool calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only outputs may include prices in SEK, areas in square meters, room counts, sold dates, and sample sizes.]

## Skill Version(s):

1.3.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
