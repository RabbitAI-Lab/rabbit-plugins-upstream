## Description:

福昕 Office 文档问答技能对当前打开的 Word、Excel 或 PowerPoint 文档进行只读问答、摘要、定位和数据核对，不修改文档。

This skill is ready for commercial/non-commercial use.

## Publisher:

[foxitnet](https://clawhub.ai/user/foxitnet)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users use this skill to ask questions about the currently active Office document, summarize long content, locate relevant passages or cells, and verify document data without changing the file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad document-Q&A trigger phrases may cause the agent to read the currently active Office document when the user did not intend that document to be considered.

Mitigation: Install only when active-document reading is acceptable, keep sensitive documents closed, and use specific prompts when requesting summaries or Q&A.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/foxitnet/skills/fuxin-doc-qa)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language Markdown answers with document references when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only output based on the active Word, Excel, or PowerPoint document.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
