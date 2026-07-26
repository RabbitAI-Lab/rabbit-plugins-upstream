## Description: <br>
Security scanner for ClawHub skills that detects malicious code, obfuscated payloads, and social engineering before installation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sypsyp97](https://clawhub.ai/user/sypsyp97) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and security reviewers use this skill to audit ClawHub skills before installation or after local installation. It helps surface suspicious shell patterns, obfuscated payloads, and social-engineering indicators for human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a shell-based helper and may inspect local skill files. <br>
Mitigation: Run it only against specific skill directories, avoid sudo, and review the command path before execution. <br>
Risk: Audit findings are advisory and may be incomplete or include false positives. <br>
Mitigation: Use the report as review guidance rather than complete security proof, and confirm material findings manually. <br>
Risk: Suspicious snippets may be exported to a temporary file for follow-up analysis. <br>
Mitigation: Treat exported snippets as untrusted content and delete any /tmp/skill-audit-*-suspicious.txt file after review. <br>


## Reference(s): <br>
- [341 Malicious ClawHub Skills Incident](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html) <br>
- [OpenClaw Security Guide](https://docs.openclaw.ai/gateway/security) <br>
- [ClawHub skill listing](https://clawhub.ai/sypsyp97/skills/skill-auditor-pro) <br>
- [Publisher profile](https://clawhub.ai/user/sypsyp97) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and terminal text audit reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Optional Gemini CLI-assisted intent analysis; results are advisory.] <br>

## Skill Version(s): <br>
2.1.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
