## Description:

投标文件智能写作工具，凭 App Key 调用百炼标书开放 API 解读招标文件、生成投标文件，并执行废标风险与合规审查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bid teams and agents use this skill for mainland-China tender workflows: interpreting tender requirements, drafting editable bid documents, and reviewing submitted bid files for compliance risks. It requires user-provided local tender or bid files and an App Key for the 百炼标书 service.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid files can contain commercial, pricing, and personal information and are uploaded to the 百炼标书 service for processing and retention.

Mitigation: Use the skill only after confirming that the user understands and accepts the service processing and retention described in the release evidence.

Risk: The App Key is an account credential, and bid-document generation can consume account credits.

Mitigation: Keep the App Key in local config.json rather than chat, and confirm the user's intent before starting generation.

Risk: Changing the default API endpoint could send sensitive tender or bid files to an untrusted service.

Mitigation: Use the default biaoshu.zhiliaobiaoxun.com endpoint unless the alternate endpoint is explicitly trusted.

## Reference(s):

- [Usage Guide](references/usage.md)
- [API Contract Reference](references/api.md)
- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-insight)
- [百炼标书 Platform](https://biaoshu.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [text, markdown, files, configuration, guidance]

**Output Format:** [Conversational summaries plus generated HTML, Word, and .docx files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are saved under biaoshu-bailian-files/ unless another local output path is configured.]

## Skill Version(s):

1.0.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
