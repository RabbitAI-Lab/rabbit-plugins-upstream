## Description: <br>
Four Layer Memory organizes personal AI memory into identity, working memory, short-term logs, and long-term storage so notes can accumulate without overloading context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lg0219](https://clawhub.ai/user/lg0219) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users can use this skill to maintain long-lived personal memory notes across identity, active work, recent logs, and confirmed long-term storage. It is intended for local memory organization rather than remote data transfer. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is designed for long-lived local memory notes, which could contain secrets or sensitive personal details if users store them there. <br>
Mitigation: Keep credentials and sensitive personal information out of memory files unless the storage location is intentionally protected and acceptable for that data. <br>
Risk: The documentation references Python commands for a helper script that is not included in the artifact. <br>
Mitigation: Verify or supply the helper script before running the referenced commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lg0219/skills/four-layer-memory) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands] <br>
**Output Format:** [Markdown guidance with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill describes local memory folder usage and suggested Python commands; no runnable helper script is bundled in the artifact.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
