## Description: <br>
专治多分包、多标段的批量场景。它读完招标文件后按分包拆分任务，成批生成对应的技术标与商务标 .docx，并对每一份做废标风险与合规审查、避免遗漏。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonzu](https://clawhub.ai/user/dragonzu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External bid teams and procurement-support users use this skill to interpret tender documents, generate package-specific bid documents, and review bid files for disqualification and compliance risks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid files may contain commercial, pricing, or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing. <br>
Mitigation: Confirm user awareness and consent before upload, and use the skill only for files the user explicitly provides. <br>
Risk: The App Key can spend account points and access account data. <br>
Mitigation: Treat the App Key like a password, keep it in the local config file or environment, avoid pasting it into chat, and reset it from the service if exposure is suspected. <br>
Risk: A ZCM_BASE override can redirect API traffic away from the intended service. <br>
Mitigation: Verify any ZCM_BASE override points to the intended biaoshu.zhiliaobiaoxun.com service before use. <br>
Risk: Generated bid documents and compliance findings can be incomplete or unsuitable for submission without review. <br>
Mitigation: Review generated files, risk findings, and suggested edits before relying on them for procurement or legal decisions. <br>
Risk: Generated documents and task results are retained under the App Key account for a limited period. <br>
Mitigation: Manage retained files and history through the service account and avoid uploading material that should not be stored there. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/biaoshu-writer-power) <br>
- [API Contract Reference](references/api.md) <br>
- [Usage Guide](references/usage.md) <br>
- [招采猫 Service](https://biaoshu.zhiliaobiaoxun.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Conversational summaries with generated .docx bid files and HTML or Word reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated artifacts are written to local output paths and results may also be available in the App Key account on the cloud service.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
