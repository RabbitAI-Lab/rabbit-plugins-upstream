## Description:

Researches public Threads (Meta) profiles, posts, replies, and search results via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and social-listening teams use this skill to retrieve public Threads profile metadata, posts, replies, and keyword search results through Crawlora instead of scraping Threads directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can make broader authenticated Crawlora requests than the Threads-only purpose describes.

Mitigation: Review before installing, run only in a trusted environment, and prefer restricting usage to the documented Threads GET endpoints.

Risk: Changing CRAWLORA_API_BASE can redirect authenticated requests away from the default Crawlora API base.

Mitigation: Avoid setting CRAWLORA_API_BASE unless the destination is intentional and trusted.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora requests and returns normalized JSON from public Threads endpoints.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
