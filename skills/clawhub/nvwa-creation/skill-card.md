## Description: <br>
女娲造人 helps an agent turn a person, theme, or ambiguous thinking need into a runnable persona-style skill by researching sources, extracting mental models, decision heuristics, expression patterns, and honest boundaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[golngod](https://clawhub.ai/user/golngod) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and agent users use this skill to create or update persona-style skills from a named person, topic, or thinking problem. It guides clarification, research, synthesis, testing, and final SKILL.md assembly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to create persistent local skill files. <br>
Mitigation: Run it in preview or local-only mode where possible, require the agent to list exact files before writing, and review generated skills before enabling them. <br>
Risk: The skill can perform online research and may process private source material. <br>
Mitigation: Avoid sending private source material to external services unless approved, and prefer user-provided local sources when privacy requirements allow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/golngod/skills/nvwa-creation) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with file and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces research notes and a runnable SKILL.md structure when the agent follows the workflow.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
