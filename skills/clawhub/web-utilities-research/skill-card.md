## Description:

General-purpose web-intelligence utilities via the Crawlora API for scraping public URLs, extracting schema-conforming JSON, fingerprinting site technology, geocoding, comparing cost of living, researching trade records, checking site traffic, and resolving brand identity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and research agents use this skill for one-off web intelligence tasks that need normalized API-backed results from public web, geocoding, cost-of-living, trade-record, traffic, and brand sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send the Crawlora API key, research targets, and request bodies to Crawlora or to an environment-overridden API base.

Mitigation: Use a dedicated Crawlora key, verify CRAWLORA_API_BASE before execution, and avoid secrets, private URLs, internal addresses, credentials, or confidential research material.

Risk: The shell helper accepts arbitrary API paths and methods beyond the documented endpoints.

Mitigation: Review generated commands before running them and keep calls limited to the documented endpoint reference unless the operator has explicitly approved another Crawlora endpoint.

Risk: ImportYeti, SimilarWeb, and similar data can reflect provider refresh cadence rather than real-time state.

Mitigation: Treat time-sensitive results as directional and verify important facts against primary sources before relying on them.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora Documentation](https://crawlora.net/docs)
- [Crawlora Playground](https://crawlora.net/playground)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/web-utilities-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key for live API calls.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
