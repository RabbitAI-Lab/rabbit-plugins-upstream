## Description: <br>
Kdocs Skill helps an agent create, read, edit, search, share, organize, summarize, translate, and convert WPS Cloud/Kdocs documents, spreadsheets, presentations, PDFs, forms, and knowledge-base content through kdocs-cli. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kdocs-app](https://clawhub.ai/user/kdocs-app) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external collaborators, and developers use this skill when an agent needs to operate a WPS Cloud/Kdocs account. Typical tasks include drafting reports, managing cloud documents, generating slides and forms, processing PDFs and spreadsheets, archiving web content, and organizing knowledge-base material. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can broadly read, modify, share, and bulk-process cloud documents. <br>
Mitigation: Confirm the exact files, destinations, visibility, and rollback plan before bulk reads, public sharing, overwrite or replace operations, knowledge-base archiving, or URL scraping. <br>
Risk: Document contents, share links, download URLs, and Kdocs/WPS tokens are sensitive. <br>
Mitigation: Prefer browser login or keychain-backed authentication, avoid pasting tokens into chat, logs, comments, or files, and rotate credentials if exposure is suspected. <br>
Risk: The skill installs and updates kdocs-cli from a remote distribution source. <br>
Mitigation: Install only when the user intentionally wants account-level Kdocs/WPS automation, and verify available checksums and the requested CLI version before allowing updates. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kdocs-app/skills/kdocs-skill) <br>
- [Kdocs latest](https://www.kdocs.cn/latest) <br>
- [Authentication reference](references/auth.md) <br>
- [File locating guide](references/file-locating-guide.md) <br>
- [Drive operations reference](references/drive.md) <br>
- [Create and upload reference](references/drive/create_and_upload.md) <br>
- [Read and download reference](references/drive/read_and_download.md) <br>
- [Share reference](references/drive/share.md) <br>
- [Spreadsheet reference](references/sheet.md) <br>
- [Word document reference](references/wps.md) <br>
- [Presentation reference](references/wpp.md) <br>
- [PDF reference](references/pdf.md) <br>
- [AI presentation reference](references/aippt.md) <br>
- [Knowledge-base reference](references/kwiki.md) <br>
- [Multidimensional table reference](references/dbsheet.md) <br>
- [Form reference](references/form.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON payload examples, and short scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include file links, command arguments, and verification steps; does not itself cache document content.] <br>

## Skill Version(s): <br>
2.5.29 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
