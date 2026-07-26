## Description: <br>
Suggests next actions after task completion and can auto-invoke through a Stop hook when completion keywords are detected. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use Next to choose follow-up work after completed tasks, such as verifying changes, committing or pushing work, monitoring CI, creating draft pull requests, or wrapping up a session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The always-on Stop hook can prompt follow-up actions after ordinary task completion. <br>
Mitigation: Install only where automatic completion follow-ups are desired, and review or constrain the Stop hook before enabling it. <br>
Risk: Stall detection can route the agent into automatic remediation through the dependent fix workflow. <br>
Mitigation: Review the stall-detect behavior and require the expected level of user approval before any fix workflow executes. <br>
Risk: Next-action options can include repository operations such as tests, commits, pushes, pull requests, or CI monitoring. <br>
Mitigation: Inspect generated options and allow repository-changing actions only after explicit user selection. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/next) <br>
- [Skill Definition](artifact/SKILL.md) <br>
- [Ask Gates](artifact/ask-gates.md) <br>
- [Stall Detection](artifact/stall-detect.md) <br>
- [Suggestion Patterns](artifact/suggestion-patterns.md) <br>
- [Stop Hook Trigger](artifact/resources/next-trigger.sh) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Text or Markdown guidance with selectable next-action options and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May register and execute selected follow-up actions when the user chooses one or more options.] <br>

## Skill Version(s): <br>
0.6.0 (source: evidence.release.version and CHANGELOG, released 2026-07-23) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
