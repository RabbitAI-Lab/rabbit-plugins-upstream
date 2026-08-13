## Description:

生成小红书创作者账号诊断报告，基于用户自己的创作者后台数据分析最近笔记表现、转化漏斗健康度、同题材爆款对标和改进动作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatmind](https://clawhub.ai/user/fatmind)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and operators use this skill to diagnose their own Xiaohongshu account performance from official creator-backend analytics. It helps identify weak funnel stages, compare each note with public high-performing notes on similar topics, and produce concrete next-step guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the user's logged-in Chrome session and handles sensitive Xiaohongshu creator analytics.

Mitigation: Run it only for accounts whose analytics may be exported locally, and review generated report files before sharing them.

Risk: Generated prompts may be sent through the webclaw3 LLM pipeline, including a configurable WC3_LLM_ENDPOINT.

Mitigation: Keep WC3_LLM_ENDPOINT unset or point it only to trusted infrastructure before running the skill.

Risk: The security scan reported an obfuscated LLM helper and an under-disclosed configurable endpoint.

Mitigation: Review the skill before installation and confirm the webclaw3 runtime and endpoint configuration are expected.

Risk: The skill writes local HTML, JSON, and Markdown files containing account-analysis details.

Mitigation: Choose an appropriate output directory and protect or delete generated files according to the account owner's data-handling needs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fatmind/skills/xhs-note-analyst)
- [webclaw3 browser automation dependency](https://clawhub.ai/fatmind/skills/webclaw3-browser-automation)
- [webclaw3 installation guide](https://github.com/fatmind/webclaw3)

## Skill Output:

**Output Type(s):** [Analysis, Files, JSON, Markdown, Guidance]

**Output Format:** [HTML report, JSON status summary, Markdown data report, and stdout JSON summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local report files and may return success, partial, or failed status depending on available account data and benchmark matches.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
