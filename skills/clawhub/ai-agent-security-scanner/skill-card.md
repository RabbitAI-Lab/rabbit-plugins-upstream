## Description: <br>
AI Agent Security Scanner scans agent and skill code for exposed secrets, injection risks, permission issues, and related security weaknesses, then produces findings with optional AI-assisted remediation suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[g620710](https://clawhub.ai/user/g620710) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and security reviewers use this skill to check agent or skill directories before release, installation, or periodic review. It performs local static scans and can optionally use DeepSeek-compatible AI analysis to explain risk and suggest fixes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Default AI analysis can send detected findings, possible secrets, or code context to a DeepSeek-compatible API when issues are found. <br>
Mitigation: Run with --no-ai for local-only scans; enable remote AI only for code your organization permits sharing, and review generated reports for secrets before distribution. <br>
Risk: Regex-based static scanning can produce false positives and miss runtime, dependency, binary, or environment-specific issues. <br>
Mitigation: Use results as triage input, manually review high-impact findings, and supplement with dependency scanning, dynamic testing, and human security review. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/g620710/skills/ai-agent-security-scanner) <br>
- [Publisher Profile](https://clawhub.ai/user/g620710) <br>
- [AI Agent Security Checklist](artifact/references/security_checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Plain text or JSON reports with optional remediation guidance and code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write reports to a user-specified output path; exits nonzero when critical findings are present.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
