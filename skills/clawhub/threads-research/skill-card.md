## Description:

Researches public Threads (Meta) profiles, posts, replies, and search results via the Crawlora API and returns clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research teams use this skill to retrieve public Threads profile data, posts, replies, and keyword search results for social listening, brand monitoring, and post analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can send requests and JSON bodies beyond the documented Threads endpoints.

Mitigation: Restrict use to the documented public Threads endpoints or wrap the helper with an allowlist before deployment.

Risk: Private workspace text or secrets could be passed into API requests by mistake.

Mitigation: Use the skill only for public Threads lookups and keep credentials in CRAWLORA_API_KEY rather than hardcoding or sharing them.

## Reference(s):

- [Threads endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/threads-research)
- [Publisher profile](https://clawhub.ai/user/tonywangcn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora API calls and returns normalized JSON from public Threads endpoints.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
