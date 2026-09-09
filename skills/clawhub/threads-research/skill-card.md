## Description:

Researches public Threads profiles, posts, replies, and search results through the Crawlora API and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, researchers, and social-listening teams use this skill to inspect public Threads profiles, posts, replies, and keyword search results without scraping the Threads app.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included helper can send the Crawlora API key to a destination set through CRAWLORA_API_BASE.

Mitigation: Avoid setting CRAWLORA_API_BASE unless the destination is fully controlled and trusted.

Risk: The release is intended for documented public Threads read-only workflows, while the helper can call broader Crawlora API paths if directed.

Mitigation: Keep use limited to the documented Threads GET endpoints and prefer a Crawlora key restricted to public Threads read-only functionality when available.

## Reference(s):

- [Threads endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/threads-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, json, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a Crawlora API key and documented public Threads GET endpoints.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
