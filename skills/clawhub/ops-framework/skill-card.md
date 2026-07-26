## Description: <br>
A 0-token jobs and monitoring framework for OpenClaw that runs long-running read tasks through scripts, supports checkpoint/resume, and sends periodic progress and immediate alerts to Telegram while blocking write jobs by default. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zjianru](https://clawhub.ai/user/zjianru) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to define, run, monitor, and resume long-running OpenClaw operations through local job configuration and status commands. It is best suited for read-heavy scans, inventories, large syncs, health checks, and explicitly approved write workflows with read-only verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Configured jobs can execute local shell commands and control processes with broad operational impact. <br>
Mitigation: Review every configured command and working directory before enabling jobs, and run the monitor under a constrained account or sandbox when possible. <br>
Risk: Job configuration changes can alter what the monitor starts, resumes, stops, or reports. <br>
Mitigation: Treat job configuration as privileged, avoid untrusted config changes, and keep auto-resume disabled unless it is explicitly needed. <br>
Risk: The security scan classified the release as Review because guardrails are only partial for command execution and process control. <br>
Mitigation: Install only when the intended workflow requires operations automation, and use the built-in write-job approval and read-only verification pattern for side-effecting tasks. <br>


## Reference(s): <br>
- [Ops Framework Specification](OPS_FRAMEWORK.md) <br>
- [Ops Framework README](README.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/zjianru/skills/ops-framework) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration, and Python script usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3.10+ on the gateway host; uses OpenClaw message sending when available or Telegram HTTP API from local OpenClaw configuration.] <br>

## Skill Version(s): <br>
0.1.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
