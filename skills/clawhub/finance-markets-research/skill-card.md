## Description:

Researches stocks, crypto, SEC filings, insider/congressional trading, and private-market (VC/PE) profiles via the Crawlora API - Yahoo Finance quotes/financials/history/options, SEC EDGAR filings and financial statements, congressional stock disclosures, CoinGecko crypto markets, and PitchBook company/fund/investor teasers - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to query public market, SEC filing, crypto, congressional trading, and private-market teaser data through Crawlora API endpoints. It supports ticker research, filing lookup, market screening, crypto momentum checks, and private company or fund profile discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included Crawlora REST helper can make arbitrary authenticated Crawlora requests, which is broader than the finance-focused skill description.

Mitigation: Review requested paths and HTTP methods before execution, keep the Crawlora API key limited, and prefer use of the documented finance, SEC, crypto, congressional, and PitchBook endpoints.

Risk: Market, filing, crypto, congressional disclosure, and private-market teaser data can be incomplete, delayed, or unsuitable as investment advice.

Mitigation: Treat outputs as research inputs, cross-check material claims against primary sources such as SEC filings or market data providers, and avoid presenting results as investment recommendations.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/finance-markets-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the CRAWLORA_API_KEY environment variable and returns raw JSON from Crawlora endpoints when commands are executed.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
