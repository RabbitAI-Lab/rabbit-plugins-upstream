## Description:

ima-skill helps agents manage IMA notes and knowledge bases, including searching and browsing content, creating or appending notes, uploading files, adding URLs, and retrieving source documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate their own IMA notes and knowledge bases through an agent, including search, browsing, note creation or append, file upload, URL import, and document retrieval workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access private IMA notes and knowledge bases.

Mitigation: Install only when the user is comfortable granting that access, and avoid exposing note bodies in shared or group contexts.

Risk: The skill uses user-provisioned Client ID and API Key credentials.

Mitigation: Prefer environment variables or a secure secret manager over plaintext credential files, and send credentials only to trusted IMA endpoints.

Risk: Note creation, note append, file upload, export, and original-document retrieval can change or expose user content.

Mitigation: Confirm user intent before write, upload, export, append, or source-document retrieval operations.

Risk: A custom IMA_BASE_URL can redirect API calls away from the official IMA service.

Mitigation: Set IMA_BASE_URL only when the endpoint is fully trusted.

## Reference(s):

- [IMA homepage](https://ima.qq.com)
- [IMA agent interface](https://ima.qq.com/agent-interface)
- [IMA knowledge-base API reference](knowledge-base/references/api.md)
- [IMA notes API reference](notes/references/api.md)
- [Tencent COS authorization reference](https://cloud.tencent.com/document/product/436/7778)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code, API calls]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provisioned IMA OpenAPI credentials and Node.js 18 or later for bundled scripts.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
