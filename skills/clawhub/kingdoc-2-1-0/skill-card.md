## Description: <br>
Kingdoc is a Kingsoft Docs integration that helps an agent create, edit, search, upload, convert, share, restore, and manage documents, spreadsheets, presentations, multidimensional tables, forms, and attachments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhangxy0204](https://clawhub.ai/user/zhangxy0204) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Use this skill when an agent needs to work with Kingsoft Docs across document creation, content editing, cloud file management, permissions, version history, recycle-bin recovery, format conversion, text extraction, notifications, and batch workflows. <br>

### Deployment Geography for Use: <br>
No geography restriction is stated in the release evidence; deploy only where Kingsoft Docs access, organizational policy, and applicable data handling requirements permit use. <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence says the skill requests broad personal and team cloud-document authority, including read, edit, overwrite, share, delete, and permanent-destroy capabilities. <br>
Mitigation: Grant only the OAuth scopes needed for the intended workflow and require human confirmation before overwrites, sharing, permission changes, rollback, deletion, or permanent destruction. <br>
Risk: The security evidence notes that several destructive-operation and credential-handling safeguards are documented but not fully enforced by the artifacts. <br>
Mitigation: Install only in an environment where plaintext configuration secrets are protected, review audit logs, and rotate the App Secret if the skill directory or logs may have been exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhangxy0204/skills/kingdoc-2-1-0) <br>
- [Publisher profile](https://clawhub.ai/user/zhangxy0204) <br>
- [Kingsoft Docs developer platform](https://developer.kdocs.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Natural-language guidance, routed tool calls, setup commands, configuration prompts, and generated or modified office-document content.] <br>
**Output Parameters:** [Kingsoft Docs App ID and App Secret, OAuth scopes, file identifiers, document type, target folder, content, permissions, conversion format, batch task options, and workflow-specific settings.] <br>
**Other Properties Related to Output:** [The skill can perform networked cloud document operations and may read, write, upload, overwrite, share, delete, restore, or roll back files depending on the granted Kingsoft Docs permissions.] <br>

## Skill Version(s): <br>
1.0.0 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
