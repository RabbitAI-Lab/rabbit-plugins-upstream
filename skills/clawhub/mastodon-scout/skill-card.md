## Description: <br>
Mastodon Scout is a read-only Mastodon API skill that returns human-readable timeline summaries or raw JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[patelhiren](https://clawhub.ai/user/patelhiren) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Mastodon users use this skill to fetch home timelines, mentions, their own posts, or status search results through the Mastodon API for review inside an agent session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Mastodon OAuth token that can expose account and timeline data if mishandled. <br>
Mitigation: Use a dedicated read-scoped token, keep it secret, and revoke it from the Mastodon application settings when no longer needed. <br>
Risk: Raw JSON output may include personal account, notification, and timeline details. <br>
Mitigation: Review raw JSON before sharing it outside the agent session. <br>
Risk: Using an untrusted Mastodon instance URL could send the token to the wrong server. <br>
Mitigation: Use the Mastodon instance that issued the token and avoid untrusted --instance values. <br>


## Reference(s): <br>
- [Mastodon Scout ClawHub listing](https://clawhub.ai/patelhiren/skills/mastodon-scout) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Human-readable text summaries or raw JSON from the Mastodon API, with shell commands for invocation and setup guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MASTODON_TOKEN; MASTODON_INSTANCE defaults to https://mastodon.social when unset.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
