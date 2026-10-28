## Description:

当用户需要做抖音内容研究、抖音选题、热点观察、竞品内容对比、趋势判断或素材整理时使用。面向内容运营、品牌调研和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容运营人员、品牌研究者和创作者可用此技能查看抖音热榜、搜索内容样本并比较相关趋势，为选题、竞品观察和素材整理提供依据。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search topics are sent to SocialDataX and may expose sensitive research interests.

Mitigation: Avoid confidential keywords and submit only information intended for the external service.

Risk: Requests may consume paid service credits.

Mitigation: Start with a small sample and check expected usage or available credits before expanding research.

Risk: The npm CLI runs in the local environment and is not technically sandboxed by the skill.

Mitigation: Review and pin the CLI version where practical, expose only the required API key, and use limited local permissions.

## Reference(s):

- [SocialDataX API Key and service information](https://socialdatax.com/ai?from=clawhub)
- [抖音内容研究 on ClawHub](https://clawhub.ai/devinchen2014/skills/douyin-content-research)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Structured Markdown summaries; JSON when presenting returned research data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include rankings, popularity signals, titles, creator or account details, content links or IDs, and follow-up research angles.]

## Skill Version(s):

0.1.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
