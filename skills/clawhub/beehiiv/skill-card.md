## Description:

Helps agents manage beehiiv publications, subscribers, posts, segments, and automations through a connected Maton account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Newsletter operators and their agents use this skill to review subscribers and publications, create posts, manage segments, and configure beehiiv-related automations with user approval for changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A connected account can expose or change newsletter and subscriber data.

Mitigation: Review requested beehiiv scopes, prefer OAuth over long-lived API keys, and confirm every write or delete.

Risk: Functions, triggers, and destinations can continue running or forwarding data after setup.

Mitigation: Review and explicitly approve each automation and destination, including its recipient, before enabling it.

## Reference(s):

- [beehiiv skill on ClawHub](https://clawhub.ai/byungkyu/skills/beehiiv)
- [Maton homepage](https://maton.ai)
- [beehiiv API reference](https://developers.beehiiv.com/api-reference)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May present selected beehiiv data; writes and new connections require user approval.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
