## Description:

Searches Facebook Marketplace listings and public Facebook Page details via the Crawlora API and returns normalized JSON for location/category Marketplace research or public Page profile lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to research public Facebook Marketplace listings or public Facebook Page details through Crawlora. It supports local price checks, browse-feed review, and public business lead enrichment without using browser automation or a logged-in Facebook session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can call arbitrary Crawlora API paths and HTTP methods beyond the documented Facebook endpoints.

Mitigation: Review commands before execution and restrict use to the documented GET /facebook/marketplace/search and GET /facebook/{page} endpoints.

Risk: The skill requires a Crawlora API key and network access.

Mitigation: Provide the key only through CRAWLORA_API_KEY, do not commit it, and avoid running the helper with untrusted environment variables.

Risk: The helper allows overriding the Crawlora API base URL through CRAWLORA_API_BASE.

Mitigation: Use the default Crawlora origin or validate the origin before running the helper.

## Reference(s):

- [facebook-research on ClawHub](https://clawhub.ai/tonywangcn/skills/facebook-research)
- [facebook-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and network access to Crawlora; Marketplace results are limited to the first page returned by Facebook server-rendered results.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
