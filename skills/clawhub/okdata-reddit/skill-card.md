## Description:

Helps agents retrieve public Reddit posts, comments, community activity, trends, and user profiles through okdata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT

## Use Case:

External users can find public Reddit discussions, inspect post comments and subreddit activity, and review public profiles for content research and discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requests to a third-party API that charges per call; the security review is partial and medium-confidence.

Mitigation: Confirm the service is trusted, estimate call count and cost before use, set a maximum price, and keep the API key in an environment variable rather than pasting it into chat.

## Reference(s):

- [Reddit API documentation](https://okdata.online/zh/apis/reddit/)
- [ClawHub release page](https://clawhub.ai/conn-ho/skills/okdata-reddit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown summaries and structured Reddit data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include relevant Reddit post, comment, community, or profile details.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
