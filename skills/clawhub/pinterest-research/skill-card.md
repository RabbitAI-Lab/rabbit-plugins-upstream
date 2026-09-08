## Description:

Researches Pinterest profiles, boards, pins, ideas categories, and search results via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and content researchers use this skill to inspect public Pinterest profiles, boards, pins, category feeds, and keyword search results through Crawlora instead of scraping Pinterest directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send the Crawlora API key and caller-controlled requests to broader or overridden Crawlora destinations than the Pinterest-only purpose describes.

Mitigation: Review before installing, use only a Crawlora key suitable for this helper, avoid environments where CRAWLORA_API_BASE may be set by someone else, and prefer a version that restricts requests to documented Pinterest endpoints and validates the API host.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/pinterest-research)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with inline shell commands and JSON-oriented API guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for public Pinterest data lookups and Crawlora API calls; returned API payloads are JSON.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
