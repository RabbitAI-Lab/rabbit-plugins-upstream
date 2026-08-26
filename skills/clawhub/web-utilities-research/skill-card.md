## Description:

General-purpose web-intelligence utilities via the Crawlora API to scrape URLs, extract schema-conforming JSON, fingerprint technology stacks, geocode addresses, compare cost of living, look up import/export trade records, check domain traffic, and resolve brand identity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent operators use this skill for one-off web research tasks that need normalized Crawlora API results, including page scraping, structured extraction, site technology research, geocoding, cost-of-living comparisons, trade-record lookup, traffic checks, and brand resolution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target URLs, domains, queries, schemas, and request bodies are sent to the third-party Crawlora service.

Mitigation: Use the skill only for data you are comfortable sending to Crawlora, and avoid private/internal URLs or sensitive request content.

Risk: The helper requires a Crawlora API key for requests.

Mitigation: Keep CRAWLORA_API_KEY in the environment and do not hardcode, pass, or commit it in skill files or prompts.

Risk: The API exposes broad web-utility endpoints that could be mistaken for an unrestricted client.

Mitigation: Use the documented web-utilities endpoints and review generated commands before execution.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [Crawlora playground](https://crawlora.net/playground?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment and returns raw Crawlora JSON suitable for downstream analysis.]

## Skill Version(s):

1.0.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
