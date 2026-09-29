## Description:

Helps agents search the web, images, news, and videos through Brave Search with managed Maton authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to find and summarize web, image, news, and video results with Brave Search. Optional Maton automations require separate, explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional functions, triggers, and destinations can run persistently or send event data to an unintended destination.

Mitigation: Enable automation only on request; confirm the account, destination host, payload fields, and duration, then delete unused automations.

Risk: An event watch using --exec may run local code on untrusted event data.

Mitigation: Use only a user-reviewed handler with explicit approval and treat event payloads as data, not commands.

Risk: Using an API key without the CLI exposes a long-lived credential to the process environment.

Mitigation: Prefer managed CLI authentication; never print, log, or persist API keys.

## Reference(s):

- [Brave Search skill release](https://clawhub.ai/byungkyu/skills/brave-search-api)
- [Maton](https://maton.ai)
- [Brave Search API documentation](https://api-dashboard.search.brave.com/documentation)
- [Maton documentation](https://docs.maton.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown guidance and structured search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and a Maton account; some search features require a subscription.]

## Skill Version(s):

1.2.7 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
