## Description: <br>
Automates a Chinese civil litigation workflow for intake, legal reasoning, document generation, case and statute research, adversarial strategy analysis, quality checks, and court-ready materials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maxiaole123](https://clawhub.ai/user/maxiaole123) <br>

### License/Terms of Use: <br>
AGPL-3.0 <br>


## Use Case: <br>
External legal professionals and litigation support staff use this skill to organize civil case evidence, apply IRAC-style legal analysis, generate litigation documents, and prepare strategy and review materials. It is designed for workflows that require human lawyer review before filing or relying on generated legal content. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles confidential litigation materials and persists case data in a local workspace. <br>
Mitigation: Use carefully selected storage locations, limit access to the workspace, and avoid placing unnecessary privileged or personal details in case files. <br>
Risk: External research features can expose sensitive case details if prompts or queries include privileged facts. <br>
Mitigation: Redact or minimize sensitive details before web or legal database searches and review each query before use. <br>
Risk: Generated legal documents or party mappings may be inaccurate or unsuitable for a specific filing posture. <br>
Mitigation: Require qualified lawyer review of party mappings, document specs, citations, and final filings before submission. <br>
Risk: The security summary flags under-disclosed licensing and accuracy risks. <br>
Mitigation: Confirm AGPL-3.0 and any commercial-use terms with the publisher before redistribution, deployment, or paid use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maxiaole123/skills/lawyer-litigation-workflow) <br>
- [律师诉讼自动化工作流 - 使用指南](artifact/references/000_使用指南_必读.md) <br>
- [诉讼自动化工作流 SOP](artifact/references/001_SOP_全流程说明.md) <br>
- [规格驱动管道说明](artifact/references/002_规格驱动管道.md) <br>
- [IRAC 推理框架](artifact/references/003_IRAC推理框架.md) <br>
- [QC 质量门控说明](artifact/references/005_QC质量门控.md) <br>
- [执业纪律铁律](artifact/references/006_执业纪律铁律.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, shell commands, JSON case data, and generated legal-document files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes local workspace outputs and explicit lawyer review checkpoints before final use.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and manifest.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
