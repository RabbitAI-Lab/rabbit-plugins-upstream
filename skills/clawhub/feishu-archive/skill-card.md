## Description: <br>
飞书文档归档与管理。Use when needing to save analysis results, meeting notes, or documents to Feishu cloud docs, organize files in Feishu drive, or sync local content to Feishu for team sharing. Supports creating docs, uploading files, and setting permissions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scubiry-glitch](https://clawhub.ai/user/scubiry-glitch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and team collaborators use this skill to archive analysis results, meeting notes, files, and important chat content into Feishu cloud docs or Feishu drive with appropriate sharing permissions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can upload local files or notes and share Feishu cloud links. <br>
Mitigation: Before use, confirm the source content, target Feishu folder, intended recipients, access level, and whether a group-chat notification should be sent. <br>
Risk: Sensitive business data may be exposed if document permissions are too broad. <br>
Mitigation: Use least-privilege sharing, keep external users unshared by default, and review read or edit permissions before distributing links. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/scubiry-glitch/skills/feishu-archive) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown guidance with document links, file links, and permission settings] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or share Feishu cloud document and drive links through delegated Feishu skills.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
