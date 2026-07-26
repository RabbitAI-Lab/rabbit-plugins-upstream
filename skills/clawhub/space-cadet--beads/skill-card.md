## Description: <br>
Track tasks and ideas with beads (bd) - Dolt-powered issue tracker for AI coding workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to capture tasks, ideas, bugs, and persistent workflow notes in a local beads database across coding sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can save task, bug, idea, and memory text into a persistent local .beads database. <br>
Mitigation: Require clear user intent before persisting casual conversation content or memory-like notes. <br>
Risk: The skill can label tasks as auto for executor-eligible work. <br>
Mitigation: Only add the auto label after confirming that the task is safe for automated execution and does not require human design or architecture decisions. <br>


## Reference(s): <br>
- [ClawHub Beads skill page](https://clawhub.ai/space-cadet/skills/beads) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target the local workspace beads database under ~/.openclaw/workspace.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
