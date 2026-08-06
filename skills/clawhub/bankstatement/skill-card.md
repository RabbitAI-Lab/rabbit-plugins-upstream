## Description:

流水报告生成，基于用户输入的Excel/PDF流水文件路径和问题，自动上传文件并生成分析报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[ufcfengbin](https://clawhub.ai/user/ufcfengbin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze Excel or PDF bank-statement files and generate a bank-statement report from a user question.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive bank statements and report prompts are sent to an external dfwytech service.

Mitigation: Use the skill only for files and prompts that may be shared with that provider, and confirm the exact file path before upload.

Risk: Broad or ambiguous file paths could result in uploading the wrong financial document.

Mitigation: Require an explicit local file path and stop the workflow when the target file is unclear or missing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ufcfengbin/skills/bankstatement)
- [ZY_TOKEN setup article](https://mp.weixin.qq.com/s/5AE3mQhsW_g-3R6C26i-9Q)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Markdown, Guidance]

**Output Format:** [Markdown guidance with bash commands; upload returns JSON and report generation returns report text or a report link.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZY_TOKEN and an explicit local bank-statement file path.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
