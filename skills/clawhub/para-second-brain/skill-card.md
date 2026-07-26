## Description: <br>
Organizes an agent's local knowledge with PARA directories, searchable notes, session transcript indexing guidance, and a context flush protocol. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[halthelobster](https://clawhub.ai/user/halthelobster) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to set up a local, file-based second brain for work continuity, project tracking, and searchable knowledge capture. It is intended for users who want offline memory structure without relying on a cloud knowledge API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent searchable memory can retain chats, personal details, or other sensitive information longer than intended. <br>
Mitigation: Before enabling agent-written memory, decide what information is allowed, avoid storing secrets or sensitive personal information, and periodically review or delete MEMORY.md and daily logs. <br>
Risk: Session transcript indexing broadens the searchable corpus to past conversations. <br>
Mitigation: Enable transcript indexing only for approved conversations and periodically prune or remove transcript archives that should not remain searchable. <br>
Risk: Agent-generated memory entries may preserve incorrect, stale, or overly private context. <br>
Mitigation: Review curated notes and daily logs before relying on them for important decisions or sharing the workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/halthelobster/skills/para-second-brain) <br>
- [PARA methodology](https://fortelabs.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON snippets, and AGENTS.md guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local memory structure and note templates; no external API calls are required by the skill itself.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
