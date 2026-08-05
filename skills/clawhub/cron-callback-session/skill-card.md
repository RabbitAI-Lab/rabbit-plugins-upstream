## Description: <br>
Guides agents through configuring OpenClaw or QClaw cron jobs and sessions_send callbacks so cron jobs, external processes, or another session can inject results into a target conversation with context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[onesfuture](https://clawhub.ai/user/onesfuture) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill when they need scheduled jobs, external processes, or separate sessions to report results back into an existing OpenClaw or QClaw conversation. It helps configure session visibility, cron callback payloads, and verification steps for same-context follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cross-session callbacks weaken session isolation for the current agent. <br>
Mitigation: Use the skill only in a controlled environment, verify the target session key, and restore tools.sessions.visibility to tree when cross-session callbacks are no longer needed. <br>
Risk: Cron jobs or external processes can inject messages into other live sessions. <br>
Mitigation: Remove callback cron jobs after use and review the intended recipient before scheduling or triggering a callback. <br>
Risk: Gateway restart steps can interrupt active sessions, cron tasks, or ongoing work. <br>
Mitigation: Keep backups, perform restart steps during a maintenance window, and confirm no important work is running before stopping gateway processes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/onesfuture/skills/cron-callback-session) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown with inline Bash, PowerShell, and JSON blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operational instructions and callback job patterns; it does not produce executable source files.] <br>

## Skill Version(s): <br>
1.0.6 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
