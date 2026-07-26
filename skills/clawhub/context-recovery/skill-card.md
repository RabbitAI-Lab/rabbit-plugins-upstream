## Description: <br>
Automatically recovers working context after session compaction or when continuation is implied but context is missing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jdrhyne](https://clawhub.ai/user/jdrhyne) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to recover recent working context from scoped channel or session history when compaction or ambiguous continuation would otherwise make the next action unclear. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill intentionally reads recent channel and session history to restore context. <br>
Mitigation: Install only where scoped history access is acceptable, keep channel permissions tight, and avoid highly sensitive channels unless access is explicitly approved. <br>
Risk: Recovered context could be persisted beyond the current interaction if optional memory or disk saving is enabled. <br>
Mitigation: Do not enable persistence unless the user has reviewed what will be saved and explicitly consents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jdrhyne/skills/context-recovery) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown summary with recovered context, recent timeline, pending actions, and a suggested continuation prompt] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses bounded channel and session history inspection; optional persistence requires user consent.] <br>

## Skill Version(s): <br>
1.2.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
