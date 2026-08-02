## Description: <br>
用于小红书热榜选题、小红书热点选题、小红书热榜分析、小红书热点分析和趋势选题参考。先看当前小红书热榜，再结合相关热门笔记样本，把热榜信号整理成可执行选题，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to inspect Xiaohongshu / XHS / RedNote hot-search signals and turn current trends plus public note samples into actionable content topic ideas. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends requests using SOCIALDATAX_API_KEY through the SocialDataX npm package and provider API. <br>
Mitigation: Confirm the user is comfortable with that provider and API-key use before installing or running the skill. <br>
Risk: Saved or forwarded outputs may include full Xiaohongshu result URLs with xsec_token query parameters. <br>
Mitigation: Share saved outputs only with intended recipients and avoid broader redistribution of result URLs. <br>
Risk: Trend analysis is based only on the current hot list and returned public result pages, so it may be incomplete or time-sensitive. <br>
Mitigation: Review recommendations before acting on them and refresh the hot list or note search when decisions depend on current trends. <br>


## Reference(s): <br>
- [SocialDataX AI access and documentation](https://socialdatax.com/ai?from=clawhub) <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-hot-topic-selection) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Shell commands, Guidance] <br>
**Output Format:** [Markdown with optional inline shell commands and returned public result URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include full Xiaohongshu note URLs, including xsec_token query parameters, and are limited to the current hot list and returned result pages.] <br>

## Skill Version(s): <br>
0.1.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
