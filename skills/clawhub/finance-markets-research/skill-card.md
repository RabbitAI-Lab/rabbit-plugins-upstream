## Description:

Helps agents research equities, crypto, SEC filings, congressional trades, and private-market profiles through Crawlora's finance APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, developers, and other users can ask an agent to investigate market prices, financial statements, SEC filings, public trading disclosures, crypto markets, or private-market profiles using the Crawlora API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key and finance-research queries are sent to Crawlora.

Mitigation: Use a dedicated API key, keep it in the CRAWLORA_API_KEY environment variable, and avoid sending sensitive queries unless comfortable sharing them with Crawlora.

Risk: Optional hiring enrichment queries public careers or ATS-derived company signals.

Mitigation: Leave hiring enrichment disabled unless those company signals are specifically needed.

## Reference(s):

- [Finance and markets endpoint reference](reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/finance-markets-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown or text with optional shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key; API responses contain public market and filing data.]

## Skill Version(s):

1.0.18 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
