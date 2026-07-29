## Description: <br>
Comprehensive server health monitoring showing system stats, top processes, OpenClaw gateway status, and running services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bustes01](https://clawhub.ai/user/bustes01) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and administrators use this skill to run local health checks for OpenClaw hosts, including system resource usage, gateway status, running services, and alerts from the CLI or automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Health output can reveal operational details such as process names, gateway port, model choices, and OpenClaw session counts. <br>
Mitigation: Run or forward the output only in trusted administrator contexts and redact operational details before sharing logs or reports. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bustes01/skills/server-health) <br>
- [README.md](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Plain text status output, JSON, or alerts-only terminal output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports standard, --json, --alerts, and --verbose modes; verbose currently uses the standard output path.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
