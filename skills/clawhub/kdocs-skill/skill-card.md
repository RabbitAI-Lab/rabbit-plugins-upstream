## Description: <br>
Kdocs Skill helps agents create, read, edit, search, share, organize, summarize, translate, and convert Kdocs/WPS cloud documents, spreadsheets, PDFs, presentations, forms, and knowledge-base content through the kdocs-cli tool. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kdocs-app](https://clawhub.ai/user/kdocs-app) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, developers, and document-workflow agents use this skill to operate Kdocs/WPS cloud documents for writing reports, processing contracts or invoices, creating forms, clipping webpages, converting PDFs, generating presentations, organizing files, and managing knowledge-base content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud-document operations can create, overwrite, delete, share, or change access to documents and knowledge-base content. <br>
Mitigation: Require explicit user confirmation for destructive, public-sharing, permission, upload, overwrite, form-change, and visibility-change actions, then verify completed write operations with an independent read. <br>
Risk: Kdocs accounts may contain confidential business or personal documents. <br>
Mitigation: Install and authenticate only when the publisher and CLI source are trusted, keep tokens out of logs and chat, and avoid processing sensitive documents unless the user has authorized the operation. <br>
Risk: URL clipping, uploads, PDF result links, and generated sharing links can persist or expose content beyond the current conversation. <br>
Mitigation: Confirm the target, visibility, and sensitivity of content before clipping, uploading, exporting, or sharing, and prefer restricted links or private destinations when possible. <br>
Risk: The setup and update workflows can execute local installation or upgrade scripts for kdocs-cli. <br>
Mitigation: Review installation scripts and run setup or upgrade commands only in an environment where local CLI installation from the publisher-controlled source is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kdocs-app/skills/kdocs-skill) <br>
- [Kdocs latest page](https://www.kdocs.cn/latest) <br>
- [Kdocs CLI skill guide](SKILL.md) <br>
- [Authentication reference](references/auth.md) <br>
- [Drive operations reference](references/drive.md) <br>
- [File locating guide](references/file-locating-guide.md) <br>
- [Spreadsheet reference](references/sheet.md) <br>
- [Presentation reference](references/wpp.md) <br>
- [PDF reference](references/pdf.md) <br>
- [Knowledge-base reference](references/kwiki.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON payload patterns] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to install or update kdocs-cli, authenticate through kdocs-cli, read task-specific reference files, execute cloud-document API commands, and verify write operations by reading results back.] <br>

## Skill Version(s): <br>
2.5.27 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
