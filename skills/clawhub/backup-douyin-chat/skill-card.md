## Description: <br>
Safely guides an agent through local Douyin chat backup workflows, including QR login, conversation selection, full or incremental backup, JSON/JSONL/HTML export, completeness checks, and optional image media download. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hilper](https://clawhub.ai/user/hilper) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate a local Douyin chat exporter while keeping account state, chat records, media, and export files on the user's machine. It is suited for backing up, updating, verifying, and exporting private or group chat history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can access private Douyin conversations, media, local account state, and exported chat files. <br>
Mitigation: Operate only on conversations visible to the user's logged-in account, keep generated data local under the tool's private data directory, and do not upload or print sensitive chat contents unless the user explicitly requests a separate action. <br>
Risk: The external local exporter uses an undocumented Douyin endpoint that can change or trigger platform risk controls. <br>
Mitigation: Require explicit risk-acceptance flags for login, backup, and media operations; start with read-only checks; and report blockers instead of silently switching tools or bypassing controls. <br>
Risk: Media backup can involve expiring CDN URLs and sensitive decryption material. <br>
Mitigation: Run media dry-runs before network writes, verify local media files before claiming success, and never print signed media URLs or decryption keys. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hilper/skills/backup-douyin-chat) <br>
- [Server-resolved GitHub source](https://github.com/hilper/douyin-chat-exporter/tree/main/skills/backup-douyin-chat) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Markdown] <br>
**Output Format:** [Markdown with inline shell commands and local file links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports aggregate backup/export status, completeness checks, media handling, and export locations without printing message bodies, cookies, signed URLs, or decryption keys.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
