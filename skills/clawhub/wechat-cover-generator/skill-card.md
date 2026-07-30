## Description: <br>
公众号封面图制作 helps WeChat creators and content teams analyze high-performing cover patterns from RedFox data and generate cover reports, design proposals, and image-generation prompts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yuanyi-github](https://clawhub.ai/user/yuanyi-github) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External WeChat Official Account creators, content operators, MCN teams, and new media editors use this skill to research recent high-performing cover styles by keyword, produce a visual analysis report, and select one of several cover concepts for image generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends cover-topic keywords to RedFox. <br>
Mitigation: Avoid sensitive unpublished topics as keywords and use only a RedFox API key whose source, scope, validity, and revocation path are understood. <br>
Risk: The skill creates a local HTML report and may open it automatically. <br>
Mitigation: Ask the agent not to auto-open reports when path inspection is needed, and review generated report files before sharing them. <br>
Risk: The skill depends on a RedFox API key. <br>
Mitigation: Provide the key through environment configuration, do not hard-code or expose it in prompts, logs, code, or output files, and rotate it if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yuanyi-github/skills/wechat-cover-generator) <br>
- [RedFox API key setup](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [WeChat hot article data format](references/gzh_trend_data_format.md) <br>
- [HTML report template data format](references/report_template.md) <br>
- [HTML report template](references/report_template.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON report data, local HTML report files, and image-generation prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY; sends cover-topic keywords to redfox.hk; creates local HTML reports and may open them in a browser; asks the user to choose a proposal before image generation.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
