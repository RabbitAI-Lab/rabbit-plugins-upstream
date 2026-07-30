## Description: <br>
Quark Cloud Drive lets an agent authenticate with Quark Drive to upload, download, save, share, search, organize, summarize, and answer questions over cloud-drive files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[quarkdrive](https://clawhub.ai/user/quarkdrive) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to work with Quark Drive files: authenticate, upload and download content, transfer shared files, create share links, search files, organize media, and ask questions or request summaries over selected drive content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Quark Drive OAuth access and can operate on cloud-drive files. <br>
Mitigation: Authorize only an intended account, use the minimum operation needed, and revoke authorization or uninstall the skill when access is no longer required. <br>
Risk: The installer can fetch and replace executable components and may attempt to install Node.js through the system package manager. <br>
Mitigation: Review the publisher and installer behavior before running it, and prefer installing Node.js manually from a trusted source. <br>
Risk: Raw prompts and selected drive-file metadata or content may be sent to Quark services during search, assistant, and file operations. <br>
Mitigation: Avoid using the skill with sensitive prompts or files unless that data sharing is acceptable. <br>
Risk: File sharing and broad uploads can expose or move more content than intended. <br>
Mitigation: Review requested paths, selected files, destination folders, and share-link settings before creating links or running broad uploads. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/quarkdrive/skills/quarkclouddrive) <br>
- [Publisher profile](https://clawhub.ai/user/quarkdrive) <br>
- [Quark Drive](https://pan.quark.cn) <br>
- [Assistant capability reference](references/assistant.md) <br>
- [Authorization and account management](references/auth.md) <br>
- [File operations reference](references/file-ops.md) <br>
- [File organization reference](references/file-organize.md) <br>
- [File read reference](references/file-read.md) <br>
- [Save shared files reference](references/file-saveas.md) <br>
- [File search reference](references/file-search.md) <br>
- [File sharing reference](references/file-share.md) <br>
- [File upload reference](references/file-upload.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and text responses with inline shell commands and NDJSON command-result handling] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May present share links, search-result tables, progress/status text, and file-operation summaries.] <br>

## Skill Version(s): <br>
1.0.10 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
