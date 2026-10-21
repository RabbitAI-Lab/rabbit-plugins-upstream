## Description:

Helps agents research equities, crypto, SEC filings, congressional trading disclosures, and private-market profiles using Crawlora market-data APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and developers use this skill to retrieve market quotes, financials, filings, trade disclosures, crypto data, and private-market profile teasers for research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests transmit query parameters, POST bodies, and the API key to Crawlora.

Mitigation: Avoid confidential non-public data in requests unless you intend to share it with Crawlora; keep the API key in the environment rather than source files.

Risk: Market and public-record data may be mistaken for investment advice.

Mitigation: Treat results as research information and independently verify them before making financial decisions.

## Reference(s):

- [Finance & markets research endpoint reference](reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/finance-markets-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance and JSON market-data responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key; data is for research, not investment advice.]

## Skill Version(s):

1.0.19 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
