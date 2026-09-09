## Description:

Researches patents and patent applications via the Crawlora API, including Google Patents full-text search, bibliographic details, claims, citations, patent families, CPC classification lookup, recent-publications browsing, database coverage, and USPTO Patent Public Search results returned as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, patent researchers, and legal or product teams use this skill to search public patent data, inspect patent claims and citations, review inventor or company portfolios, and support prior-art, landscape, or freedom-to-operate research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send the Crawlora API key to unrelated Crawlora endpoints or to a redirected API host.

Mitigation: Constrain use to the documented Google Patents and USPTO Patent Public Search endpoints, avoid overriding CRAWLORA_API_BASE when using a real key, and review generated commands before execution.

Risk: The skill depends on a user-provided API key for access to Crawlora.

Mitigation: Store the key only in CRAWLORA_API_KEY and do not hardcode, pass in query parameters, commit, or share it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/patents-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON API responses with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY; uses public patent-office data exposed through the documented Crawlora endpoints.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
