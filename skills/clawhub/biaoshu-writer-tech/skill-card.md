## Description: <br>
Biaoshu Writer Tech lets an agent use an App Key to call the Zhaocaimiao open API for tender-file interpretation, package extraction, bid document generation, and optional compliance review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and business users use this skill to process local tender and bid documents through the Zhaocaimiao cloud API, generate editable bid documents, produce reports, and review bid files for compliance risks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid documents may contain sensitive commercial, pricing, or personal information and are uploaded to the Zhaocaimiao cloud service for processing. <br>
Mitigation: Confirm user consent before upload and avoid using the skill for documents that should not leave the user's environment. <br>
Risk: App Keys can be exposed if pasted into chat history or if key-bearing recharge or bind links are shared. <br>
Mitigation: Prefer manual credential setup when users do not want keys in chat, store local credentials with restricted permissions, and never forward links containing App Key or bind_key parameters. <br>
Risk: Bid generation consumes credits tied to the App Key account. <br>
Mitigation: Check balance before generation and confirm the user intends to spend credits before submitting generation jobs. <br>
Risk: Generated bid files, interpretation reports, and compliance findings may be incomplete or require business and legal judgment. <br>
Mitigation: Review generated files and risk findings before submitting bids or relying on compliance conclusions externally. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/biaoshu-writer-tech) <br>
- [API contract reference](references/api.md) <br>
- [Usage reference](references/usage.md) <br>
- [Zhaocaimiao service](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [Zhaocaimiao open API base](https://biaoshu.zhiliaobiaoxun.com/api/open/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown and text guidance, local HTML reports, and .docx bid documents] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include absolute local file paths for generated reports or bid documents; long-running API jobs may stream progress before results are retrieved.] <br>

## Skill Version(s): <br>
2.0.5 (source: server release metadata and artifact script constant) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
