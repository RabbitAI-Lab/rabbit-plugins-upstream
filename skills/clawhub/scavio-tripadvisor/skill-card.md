## Description:

Resolve any place or business name to Tripadvisor ids, then pull ranked restaurants, hotels and attractions in a geo, one location in full, and paged review bodies. 4 endpoints, 2 credits each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and travel, hospitality, or reputation-monitoring teams use this skill to resolve Tripadvisor place names to ids, retrieve ranked venue lists, fetch full venue details, and page through review bodies as structured JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key and sends search and review lookups through Scavio.

Mitigation: Keep SCAVIO_API_KEY out of source control and review Scavio's terms for Tripadvisor data use before installation.

Risk: Scavio API calls consume credits, including empty or failed lookups.

Mitigation: Resolve names first, avoid duplicate review page requests, and budget credits before running multi-step lookups.

## Reference(s):

- [Scavio Tripadvisor Locations documentation](https://scavio.dev/docs/tripadvisor-locations)
- [Scavio rate limits documentation](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-tripadvisor)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions, JSON]

**Output Format:** [Markdown with code examples and structured JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Scavio API calls consume credits, including empty or failed lookups as documented.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
