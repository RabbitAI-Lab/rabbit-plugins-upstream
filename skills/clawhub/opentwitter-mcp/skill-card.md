## Description: <br>
Twitter/X data via the 6551 API. Supports user profiles, tweet search, user tweets, follower events, deleted tweets, and KOL followers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[infra403](https://clawhub.ai/user/infra403) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to query Twitter/X user profiles, tweets, searches, follower events, deleted tweets, and KOL follower data through the 6551 API from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends TWITTER_TOKEN to the 6551 API service. <br>
Mitigation: Use a dedicated, revocable token and install the skill only if the 6551 API service is trusted with that credential. <br>
Risk: Twitter/X usernames, searches, follower-event checks, and deleted-tweet lookups submitted through the skill may reveal sensitive research interests or investigations. <br>
Mitigation: Minimize submitted queries, avoid sensitive investigations unless appropriate, and review the provider's privacy and retention practices before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/infra403/opentwitter-mcp) <br>
- [6551 API token page](https://6551.io/mcp) <br>
- [6551 API base endpoint](https://ai.6551.io) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text, markdown] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses curl with a TWITTER_TOKEN bearer token; API responses are returned by the 6551 service.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
