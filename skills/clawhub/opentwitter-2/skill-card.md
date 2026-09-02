## Description: <br>
Twitter/X data via the 6551 API. Supports user profiles, tweet search, user tweets, follower events, deleted tweets, and KOL followers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[infra403](https://clawhub.ai/user/infra403) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and analysts use this skill to query Twitter/X profile, tweet, follower event, deleted tweet, and KOL follower data through the 6551 API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the user's TWITTER_TOKEN and Twitter/X queries to the 6551 service. <br>
Mitigation: Install only if the 6551 API provider is trusted, use a revocable or scoped token where possible, and avoid submitting sensitive targets or searches. <br>
Risk: A long-lived bearer token may remain usable after the skill is no longer needed. <br>
Mitigation: Revoke or rotate TWITTER_TOKEN when access is no longer required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/infra403/opentwitter-2) <br>
- [6551 API token page](https://6551.io/mcp) <br>
- [6551 API base URL](https://ai.6551.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and a TWITTER_TOKEN bearer token.] <br>

## Skill Version(s): <br>
0.1.0 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
