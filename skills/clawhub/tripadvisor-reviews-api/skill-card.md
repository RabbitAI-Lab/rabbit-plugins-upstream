## Description:

Resolve any place or business name to Tripadvisor ids, then pull ranked restaurants, hotels and attractions in a geo, one location in full, and paged review bodies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to resolve Tripadvisor place identifiers, retrieve ranked restaurants, hotels, and attractions for a geography, inspect a venue, and page through review bodies for travel research, reputation monitoring, and local competitive analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests disclose the queried place or venue identifiers to Scavio as a third-party API provider.

Mitigation: Use the skill only when that disclosure is acceptable for the user's task and avoid sending sensitive internal location lists unnecessarily.

Risk: API calls use the configured Scavio key and consume credits, including some empty or failed pagination requests.

Mitigation: Resolve identifiers first, avoid unnecessary pagination, stop before pages beyond the last result, and review Scavio pricing before larger runs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/tripadvisor-reviews-api)
- [Scavio Tripadvisor Locations Documentation](https://scavio.dev/docs/tripadvisor-locations?utm_source=agent-skills&utm_medium=skill&utm_campaign=tripadvisor-reviews-api)
- [Scavio Rate Limits Documentation](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=tripadvisor-reviews-api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, API Calls, JSON]

**Output Format:** [Markdown guidance with inline shell commands and code examples that produce structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Tripadvisor endpoints consume credits and return a data envelope with response time, credits used, and credits remaining.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
