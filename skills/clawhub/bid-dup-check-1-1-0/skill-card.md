## Description: <br>
标书查重与围串标风险初筛助手，用于分析多份中文投标或招标文件中的文本雷同、关键信息碰撞、文档属性一致、表格相似和双文档差异。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External procurement teams, bidders, and tender owners use this skill to screen 2-10 Chinese-language bid or tender documents for duplicate-content and collusion-risk signals before human review. It supports preliminary self-checking and triage, not formal evaluation committee decisions or legal determinations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads bid document contents, metadata, and sensitive fields, and may leave temporary JSON, image, Word, and Markdown outputs in the workspace. <br>
Mitigation: Use it only with documents the user is authorized to process, redact unnecessary personal or banking details when possible, and clean temporary workspace outputs after use. <br>
Risk: Duplicate-content and collusion-risk findings are preliminary and may be incomplete or misleading in high-stakes procurement contexts. <br>
Mitigation: Treat results as screening guidance, review the evidence manually, and do not use the report as the sole basis for formal procurement, legal, or penalty decisions. <br>


## Reference(s): <br>
- [Bid Dup Check 1.1.0 on ClawHub](https://clawhub.ai/chesaram/skills/bid-dup-check-1-1-0) <br>
- [Detection Rules](references/detection_rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, shell commands, guidance] <br>
**Output Format:** [Markdown report, DOCX report, and structured JSON findings] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces risk summaries, detailed findings, limitations, conclusions, and temporary extraction artifacts for user-provided documents.] <br>

## Skill Version(s): <br>
1.1.0 (source: artifact/SKILL.md frontmatter and artifact/manifest.yaml; ClawHub release metadata version 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
