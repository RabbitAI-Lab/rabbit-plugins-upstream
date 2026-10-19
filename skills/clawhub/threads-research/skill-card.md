## Description:

Researches public Threads profiles, posts, replies, and search results through the Crawlora API and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and brand teams use this skill to examine public Threads profiles and posts, read replies, and search for topics or mentions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send the Crawlora API key and requested public Threads identifiers or search queries to Crawlora.

Mitigation: Keep the key in the environment, never hardcode it, and review Crawlora's service terms and data practices before use.

## Reference(s):

- [Threads research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [threads-research on ClawHub](https://clawhub.ai/crawlora-org/skills/threads-research)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public data only; search is limited to its first page, and some replies lack a continuation cursor.]

## Skill Version(s):

1.0.17 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
