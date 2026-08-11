## Description:

Researches stocks, crypto, SEC filings, insider/congressional trading, and private-market profiles through Crawlora API endpoints and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to retrieve finance and market research data for equities, SEC filings, congressional disclosures, crypto markets, and private-market profiles. It is suited for agent workflows that need structured JSON from documented Crawlora endpoints rather than manual website scraping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The executable client can call arbitrary Crawlora API paths beyond the advertised finance scope.

Mitigation: Use the script only with the documented Yahoo Finance, SEC, Congress, CoinGecko, and PitchBook endpoints listed in the artifact reference.

Risk: Crawlora API requests require an API key and may send prompts or identifiers to a third-party API.

Mitigation: Store CRAWLORA_API_KEY in secret storage or an environment variable, never hardcode it, and avoid sending sensitive private prompts or identifiers.

Risk: Returned market and private-company data may be incomplete, delayed, or teaser-level and is not investment advice.

Mitigation: Treat results as research inputs, verify material decisions against authoritative sources, and avoid using the output as standalone investment advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/finance-markets-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora API key signup](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora API calls and returns raw JSON suitable for jq or agent post-processing.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
