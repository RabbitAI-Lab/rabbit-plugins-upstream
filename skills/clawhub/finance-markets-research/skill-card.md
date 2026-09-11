## Description:

Researches stocks, crypto, SEC filings, insider and congressional trading, and private-market profiles via the Crawlora API, returning clean JSON for finance and market analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent users use this skill to retrieve normalized public market, filings, crypto, congressional trading, and private-market teaser data through Crawlora. It supports ticker research, SEC and insider-trading checks, crypto market scans, and private-company or fund profile lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Finance research queries and request bodies are sent to Crawlora using the user's Crawlora API key.

Mitigation: Use only when Crawlora is an acceptable processor for the data, and avoid sending confidential portfolio, client, or private-company information unless approved.

Risk: The Crawlora API key could be exposed if it is hardcoded, committed, or passed through unsafe channels.

Mitigation: Keep the key in CRAWLORA_API_KEY, do not commit it, and use the provided helper so the key is sent as a header rather than as a command-line argument.

Risk: Market, SEC, congressional, crypto, and private-market data can be incomplete, delayed, or unsuitable as investment advice.

Mitigation: Treat outputs as research data, verify material findings against authoritative sources, and keep human review in any investment or compliance decision.

Risk: PitchBook results are described as free-tier teaser profiles rather than full paid-platform data.

Mitigation: Use PitchBook fields directionally and confirm private-market details before relying on them.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/finance-markets-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with JSON API payloads or shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends selected finance research queries and request bodies to Crawlora.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
