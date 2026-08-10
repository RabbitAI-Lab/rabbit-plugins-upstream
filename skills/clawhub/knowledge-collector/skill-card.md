## Description: <br>
Collect and catalog equipment-institute knowledge from group chats, manual entries, or batch imports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and internal equipment-institute teams use this skill to turn chat messages, manual notes, and folders of technical files into classified knowledge records for review and reuse. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic collection can ingest group-chat or folder content into a shared knowledge store without enough scoping or user control. <br>
Mitigation: Limit activation to approved channels or explicit commands and require preview and confirmation before saving entries. <br>
Risk: Batch import can process unintended local folders or files. <br>
Mitigation: Restrict batch imports to approved folders and document rules for sensitive data, retention, deletion, and reviewer access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/knowledge-collector) <br>
- [Artifact README](artifact/README.md) <br>
- [Sample knowledge entry](artifact/examples/sample_knowledge.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown knowledge entries, JSON import reports, and text reviewer notifications] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses configurable keyword and reviewer mappings; batch import scans supported local text and code files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
