## Description: <br>
Stream recent logs from systemd journal <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xejrax](https://clawhub.ai/user/xejrax) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to inspect recent systemd journal logs by service unit, line count, and optional live follow mode. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: System journal logs can contain sensitive operational data such as tokens, paths, usernames, and service errors. <br>
Mitigation: Limit journalctl requests to the relevant unit, time range, priority, and line count before sharing output. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/xejrax/skills/log-tail) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline bash commands or terminal log text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can filter journal output by systemd unit, line count, and follow mode.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
