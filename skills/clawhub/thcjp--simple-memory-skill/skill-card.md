## Description: <br>
Simple Memory Skill gives AI agents a zero-dependency local memory pattern using session state, searchable JSON memory files, and a human-readable archive. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI-agent users use this skill to add local, persistent memory workflows for preferences, decisions, facts, lessons, and active project context without external services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill encourages agents to automatically persist user information before responding, which may retain sensitive or unwanted data. <br>
Mitigation: Define what may be stored before use, avoid saving secrets or sensitive personal data unless intentionally persistent, and periodically review or delete generated memory files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/simple-memory-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent-facing memory workflow guidance and command examples; the agent may create or update local memory files when the workflow is followed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
