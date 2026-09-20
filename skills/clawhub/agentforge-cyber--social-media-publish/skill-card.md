## Description:

Assists agents with browser-based publishing workflows for WeChat Official Accounts, Baijiahao, and Xiaohongshu.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentforge-cyber](https://clawhub.ai/user/agentforge-cyber)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through browser-assisted publishing to logged-in social media platform backends. It helps confirm the target platform, title, content, cover image needs, and final publishing action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser-assisted publishing can post or prepare public content through a logged-in social media account.

Mitigation: Keep final approval under the user's control and verify the target platform, account, title, content, and cover image before publishing.

Risk: The Xiaohongshu flow depends on a separate publishing skill.

Mitigation: Review the separate Xiaohongshu publishing skill before relying on that handoff.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agentforge-cyber/skills/social-media-publish)
- [WeChat Official Accounts platform](https://mp.weixin.qq.com/)
- [Baijiahao publishing platform](https://baijiahao.baidu.com/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration instructions]

**Output Format:** [Markdown guidance with ordered publishing steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May prompt for platform, title, content, cover image, account readiness, and user confirmation before publishing.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
