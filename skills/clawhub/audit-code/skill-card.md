## Description: <br>
Security-focused code review for hardcoded secrets, dangerous calls, and common vulnerabilities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itsnishi](https://clawhub.ai/user/itsnishi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, maintainers, and security reviewers use this skill before commits, pull requests, periodic audits, or after AI-assisted code generation. It scans project files for secrets, dangerous calls, SQL injection patterns, dependency risks, sensitive files, file permission issues, and exfiltration patterns, then reports prioritized remediation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The scanner may read sensitive project files, including .env-like files, and print matched snippets in its report. <br>
Mitigation: Run it only against codebases you are authorized to inspect, review the report before sharing it, and redact any exposed secrets or sensitive snippets. <br>
Risk: Live dependency checks may send detected pip or npm package names to public registries. <br>
Mitigation: Run with network egress blocked when private dependency names should not be disclosed to PyPI or npm. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/itsnishi/skills/audit-code) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Structured Markdown report with severity-ranked findings, file locations, and remediation guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include matched snippets from scanned files and package registry verification status.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
