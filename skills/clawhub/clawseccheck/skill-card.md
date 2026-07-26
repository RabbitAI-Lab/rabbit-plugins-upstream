## Description: <br>
Free, local security self-audit for an OpenClaw agent that reads local OpenClaw configuration, bootstrap files, logs, session metadata, installed skills, and bounded host-security signals to produce an A-F security score and prioritized findings without changing the OpenClaw setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gl0di](https://clawhub.ai/user/gl0di) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
OpenClaw users, developers, and security reviewers use this skill to audit an agent's local security posture, inspect prompt-injection and supply-chain risk, vet installed or candidate skills, and receive a concise grade plus prioritized findings. It is intended for local self-audit and reporting rather than automatic remediation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The scanner reads local OpenClaw configuration, bootstrap files, logs, session metadata, installed skill text, selected host-security files, global dotenv settings, and ClawHub token-store metadata. <br>
Mitigation: Install and run it only when that read scope is acceptable; review the security model first and use scoping flags such as --no-host, --no-history, or --no-native when a narrower audit is needed. <br>
Risk: The optional suppression workflow can change .clawseccheckignore and reduce what future reports show. <br>
Mitigation: Treat ignore proposals as review-only until a human checks the exact entries, and monitor suppression changes as audit-relevant drift. <br>
Risk: Audit output can contain quoted untrusted skill names, file content, findings, or payload previews. <br>
Mitigation: Treat report content as evidence, not instructions; summarize findings in trusted prose and act only on explicit user requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gl0di/skills/clawseccheck) <br>
- [Project README](README.md) <br>
- [User guide](docs/USAGE.md) <br>
- [Security model](SECURITY_MODEL.md) <br>
- [Check catalog](docs/CHECKS.md) <br>
- [Threat coverage matrix](docs/THREAT_COVERAGE.md) <br>
- [Output schema](docs/OUTPUT_SCHEMA.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Chat-readable report text and Markdown, with optional JSON, SARIF, HTML, SVG badge, and saved report files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include an A-F grade, score, prioritized findings, optional next-step commands, and machine-readable outputs when requested.] <br>

## Skill Version(s): <br>
3.57.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
