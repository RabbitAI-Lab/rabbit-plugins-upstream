## Description:

Researches stocks, crypto, SEC filings, insider/congressional trading, and private-market (VC/PE) profiles via the Crawlora API -- Yahoo Finance quotes/financials/history/options, SEC EDGAR filings and financial statements, congressional stock disclosures, CoinGecko crypto markets, and PitchBook company/fund/investor teasers -- returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent builders use this skill to retrieve normalized market, filing, crypto, congressional-disclosure, and private-market profile data through Crawlora API calls. It is intended for finance research workflows and should not be treated as investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call arbitrary Crawlora API paths, not only the finance endpoints documented by the skill.

Mitigation: Review proposed shell commands and constrain agent use to the finance, SEC, Congress, crypto, and PitchBook endpoints listed in reference/endpoints.md.

Risk: Outbound Crawlora requests may expose sensitive prompts, credentials, or non-finance data if an agent is allowed to send arbitrary values.

Mitigation: Keep the Crawlora key in CRAWLORA_API_KEY, never place secrets in request paths or query parameters, and avoid sending private or unrelated data through the helper.

Risk: Market, filing, disclosure, crypto, and private-market teaser data can be incomplete, delayed, or unsuitable for investment decisions.

Mitigation: Use outputs as research inputs, cross-check important facts against authoritative sources, and retain the skill's not-investment-advice posture in downstream responses.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/finance-markets-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY for live API calls; returned data is normalized JSON from Crawlora-backed sources.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
