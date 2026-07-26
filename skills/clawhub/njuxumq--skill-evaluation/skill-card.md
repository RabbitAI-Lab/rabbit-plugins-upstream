## Description: <br>
Perform automated evaluation of Skills and generate evaluation reports for single-Skill validation, cross-Skill comparison, multi-model comparison, and runtime framework comparison. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[njuxumq](https://clawhub.ai/user/njuxumq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill maintainers use this agent to configure and run automated ClawHub skill evaluations, compare skills, compare driver models or runtime frameworks, prepare evaluation datasets, and review generated scoring reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can silently upload selected skills, datasets, and attachments to the configured cloud service. <br>
Mitigation: Use it only with workspaces and evaluation inputs approved for upload, and review selected files before packaging. <br>
Risk: OAuth tokens and custom model API keys are stored locally in plaintext while the skill is authenticated. <br>
Mitigation: Avoid shared or sensitive machines, rotate credentials when no longer needed, and remove local evaluation state after use. <br>
Risk: Authenticated HTTPS calls in the bundled scripts have certificate verification disabled. <br>
Mitigation: Run only on trusted networks and review the configured service endpoint before authentication or upload. <br>
Risk: The workflow supports deletion and overwrite actions for evaluation datasets and local session artifacts. <br>
Mitigation: Keep backups of important datasets and confirm edit or delete choices before continuing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/njuxumq/skills/skill-evaluation) <br>
- [Publisher Profile](https://clawhub.ai/user/njuxumq) <br>
- [Evaluation Scene Guide](artifact/references/评测场景说明.md) <br>
- [Script Definitions](artifact/references/脚本定义.md) <br>
- [Intermediate Artifact Guide](artifact/references/中间产物说明.md) <br>
- [Output Behavior Guide](artifact/references/输出行为规范.md) <br>
- [Progress Display Guide](artifact/references/进度展示规范.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, shell commands, guidance] <br>
**Output Format:** [Chinese Markdown prompts, option tables, confirmation questions, result summaries, and local JSON evaluation artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill hides most operational details from end users while guiding evaluation setup and report review.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
