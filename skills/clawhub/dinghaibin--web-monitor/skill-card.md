## Description: <br>
Monitor web pages for content changes with CSS selector targeting, change detection via hashing, and notification integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dinghaibin](https://clawhub.ai/user/dinghaibin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and automation agents use this skill to monitor full web pages or selected elements for changes, persist snapshots, and trigger configured notifications for price tracking, content alerts, and availability monitoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Notification hooks can execute arbitrary local commands when --notify is used. <br>
Mitigation: Review and control every --notify command, do not pass untrusted text into it, and avoid running the monitor with elevated privileges. <br>
Risk: HTTPS monitoring results can be spoofed because certificate verification is disabled in the code. <br>
Mitigation: Use trusted networks or update the fetch code to verify certificates before relying on monitoring results. <br>


## Reference(s): <br>
- [Web Monitor Examples](references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and optional JSON state/output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local state/output files and may run a user-specified notification command when a change is detected.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
