## Description:

Helps agents search YouTube, inspect channels and videos, and manage playlists and comments through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

YouTube users and developers can ask an agent to search videos, retrieve channel information, and manage playlists, subscriptions, and comments with their authorized account. Account changes and automations require explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing account access or exposing a long-lived API key may grant unintended access.

Mitigation: Confirm the intended YouTube connection, prefer OAuth, and keep credentials private.

Risk: Write operations may change or delete YouTube content.

Mitigation: Confirm the target and intended effect with the user before each write.

Risk: Triggers or destinations can keep forwarding event data until removed.

Mitigation: Approve automation and destinations explicitly, review their scope, and remove them when no longer needed.

## Reference(s):

- [ClawHub YouTube skill release](https://clawhub.ai/byungkyu/skills/youtube-api-skill)
- [Maton homepage](https://maton.ai)
- [YouTube Data API documentation](https://developers.google.com/youtube/v3)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance]

**Output Format:** [Text and Markdown with optional commands and API results in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions are limited to the authorized YouTube connection; writes and automations require confirmation.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
