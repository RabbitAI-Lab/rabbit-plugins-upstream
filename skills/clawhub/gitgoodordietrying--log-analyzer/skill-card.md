## Description: <br>
Parse, search, and analyze application logs across formats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gitgoodordietrying](https://clawhub.ai/user/gitgoodordietrying) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to inspect application logs, find error patterns, parse stack traces, analyze structured JSON logs, correlate events across services, and monitor log output during debugging or operations work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Log files and example structured logs can contain tokens, user identifiers, IP addresses, request IDs, and other personal data. <br>
Mitigation: Analyze only logs the user is authorized to inspect, and redact secrets and personal data before sharing excerpts or generated reports. <br>
Risk: Structured logging examples may be copied into applications without matching the user's privacy, retention, or access-control requirements. <br>
Mitigation: Adapt the examples to local data-handling policies before production use, especially fields that capture user IDs, IP addresses, or request context. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gitgoodordietrying/skills/log-analyzer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell, Python, JavaScript, and Go code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include local command suggestions and report patterns for user-provided log files.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
