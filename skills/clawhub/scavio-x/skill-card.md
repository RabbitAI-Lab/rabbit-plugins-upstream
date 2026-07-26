## Description: <br>
Search X, read tweets and their replies and retweeters, pull user profiles and their tweets, replies, media, followers, and followings, and get trending topics as structured JSON across 11 endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scavio-ai](https://clawhub.ai/user/scavio-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and external agent users use Scavio X to search and retrieve X social content as structured JSON for social research, brand monitoring, sentiment workflows, and profile or conversation analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: X queries, handles, and social graph lookups are sent to Scavio using the configured API key. <br>
Mitigation: Use the skill only when that data sharing is acceptable, protect SCAVIO_API_KEY, and avoid submitting unnecessary sensitive queries or handles. <br>
Risk: Follower, following, profile, and tweet endpoints can expose personal or social graph data. <br>
Mitigation: Use these endpoints only for legitimate purposes, respect applicable platform terms and privacy rules, and avoid unnecessary bulk pagination or retention. <br>


## Reference(s): <br>
- [Scavio X API documentation](https://scavio.dev/docs/x-api) <br>
- [Scavio rate limits](https://scavio.dev/docs/rate-limits) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with endpoint tables, JSON field descriptions, bash setup commands, and Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents to call Scavio X POST endpoints that return structured JSON responses.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
