## Description: <br>
凭 App Key 调用招采猫开放 API，帮助用户解读招标文件、生成投标文件并审查合规风险。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Organizations and agents preparing bid responses use this skill to process user-provided tender documents through 招采猫, generate editable .docx bid files, and produce interpretation or compliance reports after confirming upload and billing implications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid documents may contain commercial or personal information and are uploaded to 招采猫 cloud processing. <br>
Mitigation: Confirm user consent before upload and remind users that task results and generated files are described as retained on the service for about 7 days. <br>
Risk: The App Key grants access to the user's 招采猫 account and may be exposed if pasted into chat or included in links. <br>
Mitigation: Keep the App Key private, prefer manual credential-file setup for sensitive use, and never echo the key or forward links containing App Key or bind_key parameters. <br>
Risk: Bid generation can consume account credits and long-running jobs may continue after a local command stops. <br>
Mitigation: Check balance before generation, surface billing implications, and resume existing jobs by job_id instead of resubmitting work that could duplicate charges. <br>
Risk: Generated bid documents and compliance reports may be incomplete or require professional review before submission. <br>
Mitigation: Review all generated .docx files, reports, risk findings, and source evidence before relying on them for procurement decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/biaoshu-writer-transit) <br>
- [招采猫 platform](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [API contract reference](artifact/references/api.md) <br>
- [Usage guide](artifact/references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance, JSON status/results, HTML or Word reports, and generated .docx bid documents.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses user-provided local tender and bid files, an App Key credential, optional output-directory configuration, and writes generated artifacts under biaoshu-bailian-files/ unless configured otherwise.] <br>

## Skill Version(s): <br>
2.0.5 (source: server release metadata and artifact script constant) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
