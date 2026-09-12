## Description:

Resolve any place or business name to Tripadvisor ids, then pull ranked restaurants, hotels and attractions in a geo, one location in full, and paged review bodies. 4 endpoints, 2 credits each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to resolve Tripadvisor place names into ids, retrieve ranked restaurants, hotels, and attractions, inspect venue details, and page through review bodies for travel research, reputation monitoring, and competitive analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key and may incur paid API usage after free credits are exhausted.

Mitigation: Confirm the key is authorized for the task, disclose credit use before calls, and avoid unnecessary lookup or pagination requests.

Risk: Tripadvisor review text and reviewer metadata may include personal or sensitive context.

Mitigation: Fetch only the review fields needed for the task, avoid unnecessary retention, and do not redistribute author-identifying details without a clear reason.

Risk: Optional SDK usage adds package dependency risk.

Mitigation: Install SDKs in an isolated environment and verify the package source before use.

## Reference(s):

- [Scavio Tripadvisor API documentation](https://scavio.dev/docs/tripadvisor-locations?utm_source=agent-skills&utm_medium=skill&utm_campaign=tripadvisor-reviews-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/tripadvisor-reviews-api)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions, API Calls]

**Output Format:** [Markdown guidance with HTTP request examples, SDK snippets, and structured JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Tripadvisor API calls consume 2 credits per endpoint.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
