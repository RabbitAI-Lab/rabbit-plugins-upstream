## Description: <br>
AI runtime security monitoring - context graph analysis, runtime audit log correlation with CVE findings, and vulnerability analytics queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and security engineers use this skill to analyze agent context graphs, correlate runtime audit logs with CVE findings, and query vulnerability trends or runtime security events. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audit logs may contain sensitive event details or credential environment variable names. <br>
Mitigation: Review audit logs before use and avoid displaying or storing raw credential values. <br>
Risk: Optional ClickHouse configuration can persist runtime analytics data. <br>
Mitigation: Configure ClickHouse only when persistent analytics storage is intentionally required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-runtime) <br>
- [agent-bom source repository](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/) <br>
- [OpenSSF Scorecard for agent-bom](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and tool-call guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference in-memory scan results and user-provided JSONL audit log files; optional ClickHouse analytics storage is operator-configured.] <br>

## Skill Version(s): <br>
0.98.3 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
