## Description: <br>
Manages OpenClaw context window usage with partitioning, pre-compression checkpointing, and information lifecycle guidance for long-running sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sarielwang93](https://clawhub.ai/user/sarielwang93) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to manage long OpenClaw sessions as context usage approaches the limit, preserving task status, key decisions, and next steps before compaction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled compaction workflow may update local memory or checkpoint state and run a local OpenClaw command. <br>
Mitigation: Review the checkpoint content and the bundled script before running it, especially if the local OpenClaw workspace path differs. <br>
Risk: The artifact contains a hardcoded workspace path for the checkpoint script. <br>
Mitigation: Adjust the path for the target environment before relying on the script. <br>


## Reference(s): <br>
- [Context Budgeting on ClawHub](https://clawhub.ai/sarielwang93/skills/context-budgeting) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands] <br>
**Output Format:** [Markdown guidance with an optional shell command] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a checkpointing workflow and a bundled script for local OpenClaw session compaction.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
