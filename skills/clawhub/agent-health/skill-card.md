## Description: <br>
Monitor agent endpoints, check liveness, collect metrics, alert on failures. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, SREs, and agent operators use this skill to probe dependency endpoints, report up/down status and latency, and collect health data for deployment checks, cron jobs, dashboards, and alerts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The health checker reads endpoint lists and makes outbound checks to the listed endpoints. <br>
Mitigation: Review endpoint files before use and run checks only against systems you are authorized to probe. <br>
Risk: The optional CI verifier can execute local Python test files when run against a repository or submitted folder. <br>
Mitigation: Run the verifier only in a sandbox without secrets or sensitive filesystem access when evaluating untrusted submissions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/itspremkumar/skills/agent-health) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact Skill Definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Plain text or JSON endpoint health reports, with shell command guidance in documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Endpoint checks read local endpoint lists and may make outbound HTTP requests to those endpoints.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
