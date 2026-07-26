## Description: <br>
Emotional processing layer for AI agents. Persistent emotional states that influence behavior and responses. Part of the AI Brain series. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[impkind](https://clawhub.ai/user/impkind) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use Amygdala Memory to maintain persistent emotional dimensions for OpenClaw agents, log or infer emotional events from conversations, and surface current mood as session context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read recent OpenClaw conversation transcripts and store transcript-derived emotional signals. <br>
Mitigation: Install only when transcript-derived emotional memory is desired, and review or delete files under ~/.openclaw/workspace/memory when that data should not persist. <br>
Risk: Generated emotional state can be injected into future sessions and influence agent responses. <br>
Mitigation: Review or remove AMYGDALA_STATE.md before sessions where emotional context should not affect behavior. <br>
Risk: Optional cron setup can process transcripts and update emotional state in the background. <br>
Mitigation: Avoid --with-cron unless background processing is intended, and review configured OpenClaw cron jobs after installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/impkind/skills/amygdala-memory) <br>
- [Publisher profile](https://clawhub.ai/user/impkind) <br>
- [Project repository from release metadata](https://github.com/ImpKind/amygdala-memory) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON state files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces and updates local emotional state, session context, event logs, and dashboard files in an OpenClaw workspace.] <br>

## Skill Version(s): <br>
1.7.0 (source: server release metadata and SKILL.md openclaw metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
