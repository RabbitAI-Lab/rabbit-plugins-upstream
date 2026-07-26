## Description: <br>
GEO品牌诊断采集品牌在豆包、元宝、通义千问三大 AI 平台上的推荐覆盖情况，并生成本地诊断报告。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hitjcl](https://clawhub.ai/user/hitjcl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing teams, brand consultants, and agent users use this skill to test whether a local brand is recommended for common industry and city queries across major Chinese AI platforms. It helps produce JSON, Markdown, and Word reports for GEO brand visibility diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses authenticated Doubao, Yuanbao, and Tongyi browser sessions and may save login state locally. <br>
Mitigation: Run it only on a trusted machine with approved accounts, and delete scripts/.chrome-profile when saved sessions should be cleared. <br>
Risk: Brand, industry, city, and scenario prompts are submitted to third-party AI platforms during collection. <br>
Mitigation: Avoid sensitive unpublished business information in inputs and review platform terms before running commercial diagnostics. <br>
Risk: Generated reports reflect platform responses at collection time and may be incomplete or misleading. <br>
Mitigation: Review the JSON, Markdown, and Word outputs before using them for client-facing or business decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hitjcl/skills/geo-brand-diagnosis) <br>
- [Doubao](https://www.doubao.com) <br>
- [Yuanbao](https://yuanbao.tencent.com) <br>
- [Tongyi Qianwen](https://tongyi.aliyun.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON, DOCX, and command-line instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local reports under reports/ and can reuse saved browser login sessions from scripts/.chrome-profile after the user's initial login.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
