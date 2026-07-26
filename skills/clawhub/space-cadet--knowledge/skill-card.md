## Description: <br>
Unified knowledge capture and retrieval for URLs, video/article/paper extracts, social posts, and agent research outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to save, organize, search, and maintain a local markdown knowledge base for URLs, extracts, social posts, and research outputs that need to be found later. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can save local knowledge entries that may contain sensitive material. <br>
Mitigation: Set KNOWLEDGE_DIR deliberately and require confirmation before saving sensitive content. <br>
Risk: Automated cleanup can modify or remove local knowledge files. <br>
Mitigation: Run tidy in audit mode before enabling any scheduled tidy --fix job. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/space-cadet/skills/knowledge) <br>
- [ClawHub metadata link](https://clawhub.ai/ianderrington/agent-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and YAML frontmatter examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local markdown knowledge entries, an auto-maintained index, search guidance, and maintenance commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
