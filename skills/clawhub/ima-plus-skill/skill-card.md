## Description:

IMA.plus helps an agent manage IMA notes and knowledge bases, including path-based lookup, upload and export flows, folder and item organization, tagging, permission updates, public knowledge-base discovery, and note search, creation, reading, and editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwqww1](https://clawhub.ai/user/wwqww1)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate IMA personal notes and knowledge bases through official IMA OpenAPI workflows. It is suited for organizing knowledge-base content, uploading and exporting files, managing tags and permissions, and creating or appending notes with user-provided credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires IMA OpenAPI credentials and the security summary warns that raw credentials may be revealed or stored through chat-driven setup.

Mitigation: Use a private session, avoid pasting credentials into shared chats, screenshots, terminals, or logs, and prefer a scoped official credential flow when available.

Risk: Export workflows may expose authorization headers or sensitive note and knowledge-base content in transcripts or local files.

Mitigation: Run export commands only in private environments, review generated output before sharing, and keep exported files and command transcripts access-controlled.

Risk: The skill can write to or reorganize user notes and knowledge bases when given credentials.

Mitigation: Review proposed write, move, permission, and export operations before execution, especially append, delete, permission update, and bulk export workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwqww1/skills/ima-plus-skill)
- [Publisher profile](https://clawhub.ai/user/wwqww1)
- [IMA service endpoint](https://ima.qq.com)
- [IMA agent interface](https://ima.qq.com/agent-interface)
- [Troubleshooting reference](artifact/references/troubleshooting.md)
- [Knowledge base API reference](artifact/knowledge-base/references/api.md)
- [Notes API reference](artifact/notes/references/api.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Files, Configuration]

**Output Format:** [Markdown guidance with shell commands, JSON API payloads, and generated local files such as exported knowledge-base zip archives.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18 or newer and user-provisioned IMA OpenAPI credentials; operations may read, write, upload, export, or reorganize the user's IMA notes and knowledge-base content.]

## Skill Version(s):

1.0.7 (source: server release metadata and artifact meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
