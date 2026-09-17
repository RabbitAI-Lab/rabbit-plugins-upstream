## Description:

Search and analyse Swedish real estate on booli.se, including active for-sale listings, sold prices, area resolution, and market statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to research Swedish residential property listings, sold-price comparables, area identifiers, and local market statistics from Booli.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a browser bridge through a user-controlled Booli browser tab, which can expose unintended browsing context if paired too broadly.

Mitigation: Use the Transporter extension only with the intended Booli workflow, approve pairing deliberately, and keep the bridge limited to Booli research.

Risk: Real estate statistics and comparable-sale summaries may be misleading when based on a small sample.

Mitigation: Check sample size before relying on medians, averages, or over/under-asking percentages.

Risk: The skill is designed for read-only property research and should not be treated as an account-management or transaction tool.

Mitigation: Use it only for searches, listing details, sold-price comparables, market statistics, and diagnostics.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured property data summaries and tool-usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs use SEK for money, m2 for areas, numeric rooms, Booli area IDs, listing residence IDs, and sold-date filters in YYYYMMDD format.]

## Skill Version(s):

1.3.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
