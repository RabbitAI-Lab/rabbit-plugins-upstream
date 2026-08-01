## Description: <br>
IMA.plus helps agents manage IMA notes and knowledge bases, including searching, browsing, creating and editing notes, uploading or exporting files, managing folders and tags, and adjusting knowledge-base settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwqww1](https://clawhub.ai/user/wwqww1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent operate their IMA note and knowledge-base account after they provide IMA OpenAPI credentials. It is suited for note search and editing, knowledge-base upload and export, folder and tag management, permission updates, and public knowledge-base discovery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make real account and content changes, including editing notes, moving knowledge items, joining public knowledge bases, deleting or merging tags, changing permissions, and exporting content. <br>
Mitigation: Require explicit user confirmation before writes, permission changes, tag deletion or rename, moves, joins, and exports; review command parameters before execution. <br>
Risk: Export flows can expose signed URLs, request headers, or local export paths in logs or shared outputs. <br>
Mitigation: Avoid pasting export headers or signed URLs into shared logs, and prefer patched export behavior that redacts headers and sanitizes output paths. <br>
Risk: IMA credentials can enable reading, exporting, and modifying notes and knowledge bases. <br>
Mitigation: Install only for trusted IMA integrations, use user-provisioned IMA credentials, and keep credentials out of logs and files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wwqww1/skills/ima-plus-skill) <br>
- [IMA official site](https://ima.qq.com) <br>
- [IMA OpenAPI credential page](https://ima.qq.com/agent-interface) <br>
- [Knowledge-base API reference](artifact/knowledge-base/references/api.md) <br>
- [Notes API reference](artifact/notes/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read, export, and modify user notes and knowledge bases through user-provided IMA OpenAPI credentials.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata and artifact/meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
