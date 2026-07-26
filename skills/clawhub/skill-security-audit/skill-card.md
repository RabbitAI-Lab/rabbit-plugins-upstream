## Description: <br>
Conduct comprehensive security audits and vulnerability analysis on codebases. Use when explicitly asked for security analysis, code security review, vulnerability assessment, SAST scanning, or identifying security issues in source code. Covers injection flaws, broken access control, hardcoded secrets, insecure data handling, authentication weaknesses, LLM safety, and privacy violations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kylehuan](https://clawhub.ai/user/kylehuan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and security reviewers use this skill to audit codebases and agent skill instructions for security, privacy, and prompt-injection vulnerabilities. It supports evidence-based reporting with severity, location, impact, and remediation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audit reports may contain sensitive file paths, vulnerability details, or references to secrets. <br>
Mitigation: Use the skill only on repositories you are authorized to audit and treat .shield_security/ reports as sensitive. <br>
Risk: The skill includes malicious-command and prompt-injection examples as detection patterns. <br>
Mitigation: Treat those examples as inert reference material for review and do not execute them. <br>


## Reference(s): <br>
- [Prompt Injection & SKILL.md Security Patterns](references/prompt-injection-patterns.md) <br>
- [LLM Security & Malicious Action Patterns](references/vulnerability-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance, Shell commands] <br>
**Output Format:** [Markdown security report with findings, severity, evidence, and recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference read-only shell commands and may store requested audit artifacts under .shield_security/.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
