## Description:

当用户需要做小红书博主内容研究、账号内容列表、近期发布复盘、内容风格分析、创作者对标或账号追踪时使用。面向品牌、MCN、内容运营和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向品牌、MCN、内容运营和创作者，用于研究小红书创作者的近期发布、内容风格、账号表现及对标情况，并整理可复盘的内容证据和后续分析角度。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup inputs are sent to SocialDataX, and unrelated confidential text could be exposed to the third-party service.

Mitigation: Send only the creator identifier or profile information needed for the lookup; exclude unrelated confidential text.

Risk: The locally executed npm package carries ordinary third-party software installation risk, and unbounded pagination can increase usage costs.

Mitigation: Use a reviewed, pinned CLI version and set page or item limits appropriate to the task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/xhs-creator-content-research)
- [SocialDataX](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Structured creator-content summaries and research notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include titles or descriptions, summaries, publication times, engagement signals, media links, content types, and follow-up research questions.]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
