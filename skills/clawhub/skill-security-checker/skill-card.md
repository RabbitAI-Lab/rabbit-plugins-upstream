## Description: <br>
Skill Security Checker audits agent skill folders for static security patterns, dependency issues, permission risks, quality checks, and optional sandboxed runtime behavior, producing text, JSON, or HTML reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill publishers use this skill to check ClawHub, WorkBuddy, or SkillHub skills before release or in CI/CD, with findings, scores, and remediation guidance for security and quality issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security review flags the release as suspicious because optional dynamic scanning with allowed domains may provide broader Docker network access than the documentation implies. <br>
Mitigation: Use static scanning or dynamic scanning without allowed domains by default; enable allowed domains only for reviewed targets and treat that mode as general network access for scanned code. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/fyniujin/skills/skill-security-checker) <br>
- [Scan Patterns Reference](references/scan-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Terminal text, JSON, or HTML reports with findings, scores, and remediation suggestions.] <br>
**Output Parameters:** [1D; target skill path plus optional format, output path, update-check, dynamic scan, allow-domain, and timeout flags.] <br>
**Other Properties Related to Output:** [Runs locally; dynamic mode can execute scanned code in Docker or Windows Sandbox.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
