## Description: <br>
agent-bom runtime helps agents analyze context graphs, correlate runtime audit logs with CVE findings, and query vulnerability analytics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and security engineers use this skill to inspect agent runtime posture, investigate lateral movement in context graphs, correlate user-provided audit logs with CVE findings, and query vulnerability trends. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided runtime audit logs may contain sensitive operational details. <br>
Mitigation: Review and minimize audit logs before providing them to the skill. <br>
Risk: Optional ClickHouse storage can persist vulnerability analytics and runtime data. <br>
Mitigation: Configure ClickHouse only when persistent analytics storage is intended and approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-runtime) <br>
- [Project homepage](https://github.com/msaad00/agent-bom) <br>
- [PyPI package](https://pypi.org/project/agent-bom/) <br>
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with concise analysis and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference user-provided audit log paths and optional ClickHouse configuration; no API keys are required.] <br>

## Skill Version(s): <br>
0.98.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
