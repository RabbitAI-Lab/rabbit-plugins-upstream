## Description: <br>
IMA.plus Skill v1.0.5 helps agents manage IMA notes and knowledge bases, including search, browsing, note creation and appending, file upload and export, zip export, folder and tag operations, permission changes, public-square discovery, and knowledge-base updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwqww1](https://clawhub.ai/user/wwqww1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to operate IMA notes and knowledge bases through Node.js command helpers. It supports content retrieval, note writing, file and URL ingestion, exports, tags, permissions, and related knowledge-base administration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow may expose IMA OpenAPI credentials if users ask another AI or copilot to print API keys into chat or store them in plaintext. <br>
Mitigation: Use an official, user-controlled secret flow where possible, avoid plaintext local configuration, and never paste credentials into shared chats or logs. <br>
Risk: The skill can perform high-impact operations such as bulk export, permission changes, joining public libraries, tag deletion or merge, and note writes. <br>
Mitigation: Require explicit user confirmation before running operations with irreversible changes, account access changes, exports, or writes. <br>
Risk: File uploads and note writes can corrupt content or upload unintended data if encoding, file naming, or unsupported media checks are skipped. <br>
Mitigation: Preserve original file bytes, validate UTF-8 for note writes, keep upload titles identical to filenames, and reject unsupported media types before calling APIs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wwqww1/skills/ima-plus-skill) <br>
- [Publisher profile](https://clawhub.ai/user/wwqww1) <br>
- [IMA service endpoint](https://ima.qq.com) <br>
- [Knowledge-base API reference](artifact/knowledge-base/references/api.md) <br>
- [Notes API reference](artifact/notes/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON request examples, and references to bundled Node.js scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and user-provisioned IMA OpenAPI credentials.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence and artifact meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
