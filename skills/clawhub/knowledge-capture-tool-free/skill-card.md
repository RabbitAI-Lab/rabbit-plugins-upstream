## Description: <br>
Extracts structured knowledge from conversations and meetings, classifies it, and saves it to a knowledge base or document system. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Personal users and agents use this skill to extract knowledge points, meeting notes, decisions, and action items from conversations or documents, then organize them for reuse. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Captured notes could be saved, exported, archived, modified, deleted, or sent to a callback URL without the intended destination being clear. <br>
Mitigation: Specify the output path or knowledge-base destination and ask for a preview or confirmation before saving, exporting, archiving, modifying, deleting, or using any callback URL. <br>
Risk: The skill can use read/write and command execution for knowledge-management tasks. <br>
Mitigation: Install and run it only in trusted workspaces, review proposed file or command actions before execution, and limit access to private conversations or documents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/knowledge-capture-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Structured text, Markdown, JSON/YAML examples, and occasional shell or Python snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and write files for knowledge-management tasks; users should specify the destination before saving or exporting results.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
