## Description:

Search and analyze Swedish real estate on booli.se, including active for-sale listings, sold prices, area resolution, and market statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search and compare Swedish residential property listings, sold-price comparables, area identifiers, and market statistics from Booli. It is suited for read-only property research where prices are in SEK and areas are in square meters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may require pairing a local browser bridge with an open booli.se tab to retrieve data.

Mitigation: Install only if that browser-bridge posture is acceptable, approve pairing deliberately, run the health check before use, and review the Transporter extension and MCP tool source separately when higher assurance is required.

Risk: Market statistics based on small result sets can be misleading.

Mitigation: Check sample size before relying on medians, averages, or over/under-asking percentages for decisions.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text with structured property summaries, comparables, diagnostics, and market analysis.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only outputs may include SEK prices, square-meter areas, room counts, Booli area identifiers, residence identifiers, pagination metadata, and sample-size caveats.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
