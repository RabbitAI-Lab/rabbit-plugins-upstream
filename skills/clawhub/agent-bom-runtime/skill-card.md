## Description: <br>
AI runtime security monitoring for context graph analysis, runtime audit log correlation with CVE findings, and vulnerability analytics queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and security engineers use this skill to inspect agent runtime security posture, correlate user-provided audit logs with CVE findings, analyze context graphs for lateral movement, and query vulnerability trends. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided audit logs may contain sensitive operational details even when raw credential values are not included. <br>
Mitigation: Review and redact audit logs before use, and avoid providing logs that contain secrets or unnecessary production details. <br>
Risk: Installing the skill adds the third-party agent-bom package through pipx or pip. <br>
Mitigation: Install in a controlled environment only after reviewing the package, source, and release evidence. <br>
Risk: Optional analytics storage can persist runtime security data when an operator configures ClickHouse. <br>
Mitigation: Use only operator-approved analytics endpoints and apply the same retention and access controls used for other security telemetry. <br>


## Reference(s): <br>
- [agent-bom GitHub repository](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/) <br>
- [OpenSSF Scorecard for agent-bom](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom) <br>
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-runtime) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with tool-oriented summaries, query suggestions, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference in-memory scan results, user-provided JSONL audit logs, and optional user-configured analytics storage.] <br>

## Skill Version(s): <br>
0.98.2 (source: artifact/SKILL.md frontmatter and evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
