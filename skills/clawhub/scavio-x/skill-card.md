## Description: <br>
Search X, read tweets and their replies and retweeters, pull user profiles and their tweets, replies, media, followers, and followings, and get trending topics as structured JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scavio-ai](https://clawhub.ai/user/scavio-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to search X, retrieve tweet conversations, inspect user profiles and activity, collect social graph data, and fetch trending topics for monitoring, research, RAG, sentiment, and brand analysis workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can collect public X posts, profile details, followers, followings, replies, and retweeter data that may be personal or sensitive in context. <br>
Mitigation: Collect only the data needed for the task, disclose monitoring or profiling uses to users, and handle returned social data according to privacy and retention requirements. <br>
Risk: Requests are sent through Scavio using SCAVIO_API_KEY, and paginated collection can increase API usage and exposure of queried topics or handles. <br>
Mitigation: Use a scoped API key where possible, avoid unnecessary bulk pagination, and tell users before retrieving many pages because each X endpoint costs one credit. <br>


## Reference(s): <br>
- [Scavio X API documentation](https://scavio.dev/docs/x-api) <br>
- [Scavio rate limits](https://scavio.dev/docs/rate-limits) <br>
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-x) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/scavio-ai) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with JSON request and response examples, shell setup commands, and Python snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; paginated endpoints may consume one credit per page.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
