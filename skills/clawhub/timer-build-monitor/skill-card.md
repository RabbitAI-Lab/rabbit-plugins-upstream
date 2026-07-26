## Description: <br>
Set, list, and cancel one-shot async timers specialized for build monitoring using subagents to track and report task status without cron dependencies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to schedule a single delayed check for builds or other long-running tasks, then receive one status report instead of repeated reminders. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Delayed subagents may receive current context and act on broad task descriptions beyond simple build checks. <br>
Mitigation: Use the timer only for simple build or status checks, and avoid including secrets or sensitive operational details in timer descriptions or results. <br>
Risk: Subagent-based timers do not survive session restarts. <br>
Mitigation: Use a persistent scheduler or native cron-style timer for checks that must continue across restarts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/space-cadet/skills/timer-build-monitor) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON state examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces one-shot timer status text and human-readable JSON timer state; timers do not persist across session restarts.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
