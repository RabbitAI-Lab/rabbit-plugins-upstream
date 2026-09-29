## Description:

Tracks product mentions across Reddit and Hacker News through the 404 Mentions API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[404kidwiz](https://clawhub.ai/user/404kidwiz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and product teams use this skill to find recent Reddit and Hacker News discussions about a product, monitor competitors, and track launch reactions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product queries are sent to a third-party service.

Mitigation: Avoid querying confidential product names unless sharing them with the service is appropriate.

Risk: Full live searches consume paid credits.

Mitigation: Preview with sample=true before making a full live request.

Risk: The service requires an API key for full results.

Mitigation: Treat the key as a credential and do not expose it in shared output.

## Reference(s):

- [404 Mentions API](https://404kidwiz.github.io/mentions-api/)
- [ClawHub skill listing](https://clawhub.ai/404kidwiz/skills/skill)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown summaries with links to mentions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mentions may include source, title, URL, score, and creation time; API responses also report remaining credits.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
