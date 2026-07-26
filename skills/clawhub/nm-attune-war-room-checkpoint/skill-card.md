## Description: <br>
Assesses decision reversibility and risk at critical checkpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill when command workflows reach high-stakes branches and need a structured checkpoint for reversibility, escalation, confidence, and user-confirmation decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Checkpoint and War Room audit logs may persist workflow context, including affected file paths, rationale, confidence, and escalation history, under the user's home directory. <br>
Mitigation: Use only in workspaces where local audit records are acceptable, and review or periodically clean the documented ~/.claude/memory-palace/strategeion paths on shared machines. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-war-room-checkpoint) <br>
- [Attune plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>
- [Publisher profile](https://clawhub.ai/user/athola) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown with structured checkpoint response fields and YAML-style examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include reversibility score, escalation mode, recommendation or orders, confidence, and user-confirmation status.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
