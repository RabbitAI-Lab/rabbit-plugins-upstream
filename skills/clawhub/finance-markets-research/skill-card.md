## Description:

Researches stocks, crypto, SEC filings, insider/congressional trading, and private-market profiles via the Crawlora API, returning clean JSON for market and company research tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill to retrieve public equities, SEC filing, congressional disclosure, crypto market, and private-market profile data through Crawlora-backed finance endpoints. It supports ticker research, market screening, filing lookup, insider and congressional trade checks, crypto momentum scans, and VC or private-company due diligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shell helper can send the Crawlora API key with arbitrary paths and methods beyond the stated finance scope.

Mitigation: Use only the documented finance endpoints and review each requested path and method before execution.

Risk: CRAWLORA_API_BASE can be overridden, which could redirect authenticated requests away from the intended Crawlora API.

Mitigation: Leave CRAWLORA_API_BASE unset or restrict it to a trusted Crawlora API base before using the helper.

Risk: The skill requires a Crawlora API key for live requests.

Mitigation: Store the key only in CRAWLORA_API_KEY and avoid hardcoding, logging, committing, or placing it in URLs.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API v1](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/finance-markets-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, json]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY for live API calls.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
