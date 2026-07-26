## Description: <br>
Security scanner for Python skills before publishing to ClawHub. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johstracke](https://clawhub.ai/user/johstracke) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and skill publishers use this skill to run a basic local static check on Python skill files before publishing, reviewing warnings for dangerous imports, unsafe functions, hardcoded secrets, and risky file operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The scanner is basic static analysis and does not provide a complete security audit. <br>
Mitigation: Use it as an initial local check, manually review warnings, and complement it with code review or additional scanners for higher-assurance releases. <br>
Risk: Warnings can require context and may not prove that code is malicious or safe. <br>
Mitigation: Read each flagged file and confirm whether the pattern is necessary, documented, and acceptable before publishing. <br>
Risk: Automated publishing gates may over-rely on scanner output. <br>
Mitigation: Confirm the scanner's exit-code behavior before using it as a required publish gate. <br>


## Reference(s): <br>
- [Security Checker on ClawHub](https://clawhub.ai/johstracke/skills/security-checker) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Console text with warning messages and summary status] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Static analysis only; warnings require manual review.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
