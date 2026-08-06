## Description: <br>
Reviews code for security vulnerabilities, authentication flows, dependency risks, and security compliance, then produces structured findings and improvement guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security reviewers, and engineering teams use this skill to review codebases for common vulnerabilities, authentication weaknesses, dependency concerns, and security compliance issues. It is intended for code-level assessment, not unauthorized penetration testing or non-code physical or social-engineering evaluations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is designed to read repository content and may run commands while auditing code, which can expose secrets or production configuration if used on broad workspaces. <br>
Mitigation: Give the agent access only to the codebase intended for review and deliberately approve command execution, especially in repositories containing credentials or production settings. <br>
Risk: Security review output can be incomplete or contain false positives because the skill relies on available context and agent analysis. <br>
Mitigation: Treat findings as review input, validate high-impact results manually, and run established security scanners or human review before relying on remediation decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/security-auditor) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON-style structured security report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include security grades, vulnerability findings, CVE or CWE mapping, dependency audit notes, and prioritized remediation suggestions when supported by the supplied repository context.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
