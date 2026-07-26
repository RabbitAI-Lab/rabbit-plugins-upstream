## Description: <br>
This skill helps developers and merchants handle WeChat Pay integration questions, including product selection, official examples, integration quality checks, documentation Q&A, and APIv3 troubleshooting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tencent-adm](https://clawhub.ai/user/tencent-adm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, merchants, and payment integration teams use this skill to select WeChat Pay products, retrieve official examples, review integration quality, answer implementation questions, and troubleshoot APIv3 payment or refund queries. <br>

### Deployment Geography for Use: <br>
China domestic merchants; the artifact says overseas or cross-border scenarios should use the separate wechatpay-global-payment skill. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run a networked Python updater that downloads and replaces local WeChat Pay documentation. <br>
Mitigation: Review the updater and publisher before installation, run the update only after explicit approval, and verify that the documentation archive source is acceptable for the environment. <br>
Risk: The APIv3 troubleshooting workflow may handle payment authorization values and API query details. <br>
Mitigation: Use least-privilege credentials, avoid sharing production secrets unless required, redact sensitive values from logs and transcripts, and confirm before executing live API calls. <br>
Risk: The documentation Q&A workflow can persist merchant-role preferences into a project-wide AGENTS.md file. <br>
Mitigation: Allow AGENTS.md writes only when the user explicitly wants that preference to affect future agent sessions, and review the file after changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tencent-adm/skills/wechatpay-payment-integration) <br>
- [WeChat Pay documentation archive](https://wx.gtimg.com/resource/wechatpay_api/wechatpay-docs.zip) <br>
- [APIv3 接口动态排障](references/APIv3接口动态排障.md) <br>
- [wechatpay-dev-cli 使用说明](references/wechatpay-dev-cli使用说明.md) <br>
- [基础概念及业务介绍](references/基础概念及业务介绍.md) <br>
- [如何理解用户问题](references/如何理解用户问题.md) <br>
- [接入质量检查清单](references/接入质量检查清单.md) <br>
- [文档检索与问答](references/文档检索与问答.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown answers with command snippets, code blocks, checklists, and documentation references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Technical answers are expected to cite local documentation paths and official WeChat Pay URLs when source material is used.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and changelog; artifact frontmatter says 1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
