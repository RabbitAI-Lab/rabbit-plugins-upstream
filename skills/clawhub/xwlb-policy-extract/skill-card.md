## Description: <br>
新闻联播政策摘报。获取每日新闻联播主要内容并提取宏观经济政策与金融影响政策。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhutulang](https://clawhub.ai/user/zhutulang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and analysts use this skill to fetch daily Xinwen Lianbo transcript content, identify macroeconomic and finance-relevant policy items, and receive a structured policy summary. It is suited for tracking policy signals that may affect financial markets or sector expectations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on broad Chinese policy or finance-policy queries. <br>
Mitigation: Review or narrow trigger phrases if deployment should only handle explicit 新闻联播 policy-summary requests. <br>
Risk: The skill fetches public web pages and temporarily saves transcript text before running a local parser. <br>
Mitigation: Review fetched sources before use and remove temporary transcript files after parsing, as the skill workflow specifies. <br>


## Reference(s): <br>
- [宏观经济政策关键词参考](artifact/references/macro_keywords.md) <br>
- [ClawHub skill release page](https://clawhub.ai/zhutulang/skills/xwlb-policy-extract) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Shell commands, Analysis, Guidance] <br>
**Output Format:** [Markdown report with optional JSON output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes tiered policy classifications, policy-item counts, relevant keywords, content previews, and a non-policy headline summary.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and manifest.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
