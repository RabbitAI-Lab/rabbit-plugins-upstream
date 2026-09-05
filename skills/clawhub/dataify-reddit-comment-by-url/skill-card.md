## Description:

Collect comments from a known Reddit post URL. Do not use for post discovery or subreddit post lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to collect comments from known Reddit post URLs through Dataify and receive the completed collection result. It is not intended for Reddit post discovery or subreddit post list collection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Reddit URLs and the user's Dataify account token to Dataify.

Mitigation: Configure DATAIFY_API_TOKEN through the shell or a secret store and do not paste the token into chat.

Risk: Submission may consume Dataify credits, especially for multi-input or high-volume collections.

Mitigation: Use no-wait behavior or explicit parameter confirmation when tighter control over credit usage is needed.

Risk: Server security evidence marks the release as suspicious because credential-handling instructions are inconsistent.

Mitigation: Review the skill before installing and confirm that token setup and execution behavior match the intended environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-reddit-comment-by-url)
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill)
- [Dataify login](https://dashboard.dataify.com/login?utm_source=skill)
- [Reddit URL scope](https://www.reddit.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON task/result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns final collected results by default; can stop after task submission when explicitly requested.]

## Skill Version(s):

1.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
