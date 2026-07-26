## Description: <br>
Real-time security monitoring for Clawdbot. Detects intrusions, unusual API calls, credential usage patterns, and alerts on breaches. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chandrasekar-r](https://clawhub.ai/user/chandrasekar-r) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to run continuous monitoring for Clawdbot deployments, including failed-login checks, port anomaly checks, process monitoring, file-change detection, Docker health checks, and alert logging. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan summary says the monitor reads a credentials file and should be reviewed before installation. <br>
Mitigation: Remove or patch the .env content read before use, and install only where host log, process, port, Docker, and /root/clawd access are acceptable. <br>
Risk: The security guidance says the advertised --threats selection should not be relied on for scoping until fixed. <br>
Mitigation: Treat enabled checks as broad host monitoring unless the threat-selection behavior is patched and reviewed. <br>
Risk: The security guidance calls out generated alert and state files as sensitive operational data. <br>
Mitigation: Protect or rotate generated alert and state files and run the monitor with the least privilege that still supports the required checks. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands] <br>
**Output Format:** [Console output and JSON alert logs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can run once or as a daemon with configurable interval; alert logs are written under /root/clawd/clawdbot-security/logs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
