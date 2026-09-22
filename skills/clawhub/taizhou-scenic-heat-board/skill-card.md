## Description:

台州景区热度榜 helps tourism and cultural-travel teams see which Taizhou scenic areas are hottest or rising, with 30-day visitor and overnight-stay trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Tourism operators, cultural-travel teams, and planning analysts use this skill to fetch current Taizhou scenic-area heat rankings and recent trend data for staffing, supply, promotion, and traffic-analysis decisions.

### Deployment Geography for Use:

Global; the skill's data coverage is limited to Taizhou, China.

## Known Risks and Mitigations:

Risk: The skill contacts an external data service to retrieve scenic-area popularity data.

Mitigation: Install and run it only where outbound access to that service is acceptable for the deployment environment.

Risk: The skill may store product access state such as an API key, install ID, and cookies locally under .odf.

Mitigation: Protect that local credential directory, avoid sharing it, and remove stored access state when decommissioning the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/taizhou-scenic-heat-board)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Plain text or Markdown-style report with scenic-area rankings, trend summaries, and status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access to an external data service and may store product access state such as an API key, install ID, and cookies locally under .odf.]

## Skill Version(s):

1.0.20 (source: server release, SKILL.md frontmatter, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
