## Description: <br>
Cron Worker Guardrails provides a POSIX-focused checklist for hardening OpenClaw cron and background workers against brittle shell quoting, working-directory and environment drift, pipeline failures, and unsafe automation patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to make cron and background worker prompts, scripts, and git automation more reliable, deterministic, and quiet on success for unattended jobs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated cron scripts or git commands may affect important repositories or production jobs if applied without review. <br>
Mitigation: Review commands and scripts before running them, especially against long-lived branches or production automation. <br>
Risk: POSIX shell guidance may not directly fit Windows or PowerShell environments. <br>
Mitigation: Adapt the patterns to equivalent platform-specific scripting conventions before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/cron-worker-guardrails) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell and code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No hidden actions; review generated cron scripts, git commands, and production job changes before running them.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
