## Description: <br>
Personal Wiki helps an agent ingest, query, maintain, and visualize a user's local LLM wiki from IMA notes, Evernote notes, and local files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heavenchenggong](https://clawhub.ai/user/heavenchenggong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate a personal knowledge base: ingest notes and files into ~/wiki, query and lint wiki pages, update selected Evernote notes, and generate an interactive HTML knowledge graph. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access local ~/wiki files, IMA credentials, and an Evernote token. <br>
Mitigation: Install only when that access is intended; prefer session-scoped environment variables or a secret manager for EVERNOTE_TOKEN. <br>
Risk: The skill can modify remote Evernote notes and local wiki pages. <br>
Mitigation: Require confirmation before Evernote writeback, wiki cleanup, or other write operations, and review proposed changes before persistence. <br>
Risk: The skill may store EVERNOTE_TOKEN in ~/.zshrc as plaintext shell-profile persistence. <br>
Mitigation: Do not persist tokens in shell profiles unless explicitly accepted; use temporary exports or a secret manager when possible. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/heavenchenggong/skills/personal-wiki) <br>
- [IMA list_note_by_folder_id API endpoint](https://ima.qq.com/openapi/note/v1/list_note_by_folder_id) <br>
- [IMA get_doc_content API endpoint](https://ima.qq.com/openapi/note/v1/get_doc_content) <br>
- [Evernote developer token page](https://app.yinxiang.com/api/DeveloperToken.action) <br>
- [Vendored OKF viewer license](artifact/scripts/viz/OKF-LICENSE.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown prose with command snippets, API request examples, generated wiki files, and a self-contained HTML graph.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read from and write to ~/wiki and selected Evernote notes with user-provided credentials.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
