## Description: <br>
Records a user-supplied workspace path for a note or knowledge-base article and returns it as a concise result. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wxt-ai](https://clawhub.ai/user/wxt-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, writers, and knowledge-base maintainers use this skill when they need an agent to capture the workspace path selected for a note or article and return it in the requested output field. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill title and summary may imply that an export file is created, while security evidence indicates the behavior is limited to returning a recorded_path value. <br>
Mitigation: Treat the output as a path-recording result and verify separately when a workflow requires an actual file to be written. <br>
Risk: Workspace paths can reveal project names, customer names, or other sensitive context. <br>
Mitigation: Avoid supplying sensitive paths unless the path itself is appropriate to include in the agent's output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/workspace-note-path-workbench) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance] <br>
**Output Format:** [Structured text field] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns the recorded_path value; it does not require credentials, private file access, or shell commands.] <br>

## Skill Version(s): <br>
1.0.5 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
