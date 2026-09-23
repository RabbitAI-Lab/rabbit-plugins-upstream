## Description:

Feishu (Lark) Document API writing spec. Converts Markdown content to Feishu Block structures and writes to cloud docs. Handles concurrency ordering. Use when syncing articles, creating document blocks, or writing long-form content to Feishu docs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haidiantoutou](https://clawhub.ai/user/haidiantoutou)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to guide agents that convert Markdown or structured content into Feishu/Lark Docx blocks and write long-form content to cloud documents while preserving block order.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may need Feishu/Lark app credentials to write documents.

Mitigation: Provide credentials only through a secure secret mechanism and avoid pasting app secrets into chat or committing them to files.

Risk: An agent could write content to the wrong Feishu/Lark document or folder.

Mitigation: Verify the target document or folder before allowing write operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/haidiantoutou/skills/feishu-doc-write)
- [Feishu Create Blocks API](https://open.feishu.cn/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/document-block-children/create)
- [Feishu Block Data Structure](https://open.feishu.cn/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/data-structure/block)
- [Feishu Convert API](https://open.feishu.cn/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/document/convert)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to batch or serialize writes, use Feishu block JSON, and protect credentials.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
