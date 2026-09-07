## Description:

General-purpose web-intelligence utilities via the Crawlora API for scraping URLs, extracting schema-conforming JSON, fingerprinting site tech stacks, geocoding, comparing cost of living, looking up import/export records, checking domain traffic, and resolving brand identity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research-focused agents use this skill for one-off public web intelligence lookups through Crawlora, including content scraping, structured extraction, site profiling, geocoding, cost-of-living checks, trade-record lookup, traffic overview, and brand metadata resolution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requested web-research inputs to Crawlora and should not be used with confidential prompts, private or internal URLs, secrets, or regulated data.

Mitigation: Use only public, non-sensitive inputs and review the target URL and request body before making API calls.

Risk: An undocumented CRAWLORA_API_BASE override could send the API key and request contents to another server.

Mitigation: Ensure CRAWLORA_API_BASE is unset or points only to the legitimate Crawlora API before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/web-utilities-research)
- [Crawlora](https://crawlora.net)
- [Crawlora documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [Endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Crawlora API requests, normalized JSON response summaries, and setup guidance for CRAWLORA_API_KEY.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
