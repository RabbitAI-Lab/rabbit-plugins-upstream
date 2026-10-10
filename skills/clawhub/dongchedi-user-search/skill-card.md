## Description:

按关键词搜索懂车帝用户、查看其作品与互动数据，并可订阅每日作品更新。

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

内容创作者、汽车品牌和分析人员可搜索懂车帝作者、比较作品表现，并订阅指定作者的每日更新。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HTTPS certificate checks are disabled while sending a RedFox API key.

Mitigation: Restore certificate verification before using the key on untrusted networks; restrict and revoke the key if exposure is suspected.

Risk: Subscriptions create recurring daily automation tasks.

Mitigation: Confirm the recurring task with the user and explain how to cancel the subscription.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/redfox-data/skills/dongchedi-user-search)
- [RedFox API key setup](https://redfox.hk/settings/api-keys?source=clawhub)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown tables and text with links to user profiles and works]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User search supports pagination; work lists show 20 entries initially, with an option to show the remainder; subscriptions provide daily updates.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
