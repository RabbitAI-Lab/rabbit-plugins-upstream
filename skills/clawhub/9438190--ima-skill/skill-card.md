## Description: <br>
Ima Skill helps agents manage IMA notes and knowledge bases, including searching, reading, creating or appending notes, adding URLs, and uploading supported files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[9438190](https://clawhub.ai/user/9438190) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to let an agent work with their IMA account: manage personal notes, search or browse knowledge bases, add web links, and upload supported files. It is useful when IMA OpenAPI credentials are available and the user wants agent-assisted note or knowledge-base operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles private notes, file uploads, and IMA account credentials. <br>
Mitigation: Install only when the publisher is trusted, use the least-privilege IMA credentials available, and keep credentials scoped to the official IMA workflow. <br>
Risk: Network behavior includes IMA API calls and COS upload endpoints. <br>
Mitigation: Allow requests only to ima.qq.com and the expected COS endpoints, and avoid overriding IMA_BASE_URL unless the endpoint is fully controlled and trusted. <br>
Risk: The update flow can return remote-provided update instructions before the original request proceeds. <br>
Mitigation: Review any update prompt before following it, especially when it requests credential, network, or installation changes. <br>
Risk: Note writes and appends can modify private user content and may corrupt text if encoding is wrong. <br>
Mitigation: Confirm the target note before append operations and validate text as UTF-8 before write calls. <br>
Risk: File uploads may expose user files or create incorrect knowledge-base entries if unsupported files or altered names are used. <br>
Mitigation: Run the preflight check, preserve the original filename for upload titles, reject unsupported types, and stop if COS upload fails. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/9438190/skills/ima-skill) <br>
- [IMA Homepage](https://ima.qq.com) <br>
- [IMA Agent Interface](https://ima.qq.com/agent-interface) <br>
- [Knowledge Base API Reference](artifact/knowledge-base/references/api.md) <br>
- [Notes API Reference](artifact/notes/references/api.md) <br>
- [Tencent COS Authorization Reference](https://cloud.tencent.com/document/product/436/7778) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Markdown, Configuration] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API request or response handling] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 18 or newer and user-provisioned IMA OpenAPI credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
