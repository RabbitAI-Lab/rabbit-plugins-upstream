## Description: <br>
Feishu Doc Write guides agents through converting Markdown content into Feishu/Lark Docx API block structures and writing them to cloud documents while preserving block order. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haidiantoutou](https://clawhub.ai/user/haidiantoutou) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to convert Markdown or long-form content into Feishu Docx API blocks and create or update Feishu/Lark cloud documents. It is suited for article syncing and document generation workflows where block ordering and Feishu-specific blocks matter. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill guides agents to create or modify live Feishu/Lark cloud documents using app credentials. <br>
Mitigation: Use least-privilege credentials from a secure source and avoid pasting secrets into chats or files. <br>
Risk: Incorrect folder or document identifiers can write content to the wrong Feishu/Lark location. <br>
Mitigation: Verify folder and document IDs before creating or modifying live documents. <br>
Risk: Concurrent block creation can produce incorrect document ordering. <br>
Mitigation: Use a single batch request when possible, or perform serial writes with explicit indexes for long content. <br>


## Reference(s): <br>
- [Feishu Create Blocks API](https://open.feishu.cn/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/document-block-children/create) <br>
- [Feishu Block Data Structure](https://open.feishu.cn/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/data-structure/block) <br>
- [Feishu Convert API](https://open.feishu.cn/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/document/convert) <br>
- [ClawHub Skill Page](https://clawhub.ai/haidiantoutou/skills/feishu-doc-write) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes Feishu block mappings, API request patterns, ordering guidance, and authentication examples.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
