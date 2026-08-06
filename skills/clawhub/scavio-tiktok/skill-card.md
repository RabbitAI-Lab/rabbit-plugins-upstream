## Description: <br>
Look up TikTok profiles, search videos and users, explore hashtags, read comments, and traverse the social graph (followers/followings). Eleven endpoints, all at 1 credit per request. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scavio-ai](https://clawhub.ai/user/scavio-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, and analysts use this skill to retrieve structured TikTok profile, video, comment, hashtag, search, and social graph data through Scavio. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: TikTok usernames, video IDs, hashtags, search terms, and follower or comment lookup requests are sent to Scavio. <br>
Mitigation: Use the skill only when sending those queries to Scavio is acceptable, and avoid sensitive investigations unless that data sharing has been reviewed. <br>
Risk: Bulk pagination can increase credit usage and rate-limit exposure. <br>
Mitigation: Limit pagination, inform users before making many requests, and wait or retry conservatively when rate limits or upstream errors occur. <br>
Risk: The Scavio API key can authorize paid or quota-consuming requests. <br>
Mitigation: Store SCAVIO_API_KEY securely, avoid exposing it in logs or shared outputs, and rotate it if it may have been disclosed. <br>


## Reference(s): <br>
- [Scavio TikTok API Documentation](https://scavio.dev/docs/tiktok-api) <br>
- [Scavio API Homepage](https://scavio.dev) <br>
- [Scavio TikTok ClawHub Skill](https://clawhub.ai/scavio-ai/skills/scavio-tiktok) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with API endpoint details, JSON response examples, Python examples, and shell setup commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; TikTok API calls use Scavio credits and may be paginated.] <br>

## Skill Version(s): <br>
1.0.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
