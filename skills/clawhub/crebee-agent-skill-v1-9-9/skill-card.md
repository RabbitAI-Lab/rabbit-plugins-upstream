## Description:

CreBee Social Media Gateway helps an AI agent manage Chinese social media accounts, publish video, image, and article content, retrieve analytics, access audience profiles, search topics and activities, and interact with platforms such as Douyin, Bilibili, Xiaohongshu, and Kuaishou.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hzygithub](https://clawhub.ai/user/hzygithub)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to guide agents through CreBee desktop-client API workflows for social media account management, batch publishing, cancellation, publish-status checks, analytics retrieval, and platform-specific request construction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish or cancel content on real social media accounts.

Mitigation: Use it only with accounts the user controls and require explicit user confirmation before publish or cancellation requests.

Risk: The skill relies on a bearer token for the local CreBee API.

Mitigation: Keep the token private, avoid embedding it in generated integrations, and refresh it only when required.

Risk: The skill can retrieve fan, audience, profile, and account analytics data.

Mitigation: Request audience or profile data only when needed for the current task and avoid unnecessary collection or disclosure.

## Reference(s):

- [CreBee website](https://www.crebee.cn)
- [CreBee download page](https://www.crebee.cn/#/download)
- [ClawHub skill page](https://clawhub.ai/hzygithub/skills/crebee-agent-skill-v1-9-9)
- [Publishing guide](references/publishing.md)
- [Douyin API reference](references/platforms/douyin.md)
- [Bilibili API reference](references/platforms/bilibili.md)
- [Xiaohongshu API reference](references/platforms/xiaohongshu.md)
- [Kuaishou API reference](references/platforms/kuaishou.md)
- [Weibo API reference](references/platforms/weibo.md)
- [Zhihu API reference](references/platforms/zhihu.md)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown with HTTP examples, JSON payloads, and integration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API endpoints, bearer-token usage, request bodies, and platform-specific publishing parameters.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
