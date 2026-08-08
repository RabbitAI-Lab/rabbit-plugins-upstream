## Description: <br>
Read Instagram profiles, post and reel feeds, tagged posts, active stories, single-post detail, comments and replies, follower and following lists, and search users and hashtags. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scavio-ai](https://clawhub.ai/user/scavio-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve public Instagram profile, post, reel, story, comment, follower, following, user-search, and hashtag-search data through Scavio. It supports influencer research, competitor tracking, creator discovery, and structured social-media analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent needs access to SCAVIO_API_KEY to call Scavio endpoints. <br>
Mitigation: Install and run the skill only where the agent is allowed to use that credential, and avoid exposing the key in prompts, logs, or shared outputs. <br>
Risk: Instagram endpoints spend Scavio credits, and large follower, following, or comment collection tasks can consume credits quickly. <br>
Mitigation: Set explicit page, count, and credit limits with the user before multi-call workflows, and stop when limits or out-of-credit responses are reached. <br>
Risk: The skill retrieves public Instagram data that may raise privacy, policy, or platform-terms concerns depending on use. <br>
Mitigation: Use it only for compliant public-data workflows and avoid unnecessary collection or retention of personal data. <br>
Risk: Instagram responses are raw upstream passthroughs with variable field names and pagination tokens. <br>
Mitigation: Inspect returned keys defensively, preserve raw field names when reporting results, and do not assume pagination or sort order is guaranteed. <br>


## Reference(s): <br>
- [Scavio Instagram API documentation](https://scavio.dev/docs/instagram-api) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides API requests that return raw upstream Instagram JSON and requires SCAVIO_API_KEY.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
