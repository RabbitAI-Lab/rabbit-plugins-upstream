## Description: <br>
Scans ClawHub skills for malicious code, obfuscated payloads, suspicious indicators, and social-engineering patterns before installation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sypsyp97](https://clawhub.ai/user/sypsyp97) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and ClawHub users use this skill as a lightweight pre-install or local review aid for checking third-party skills before deciding whether to install or trust them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill advertises LLM intent analysis, but the security evidence says that analysis is not actually run by the script. <br>
Mitigation: Treat the report as lightweight pattern and deobfuscation screening, and use separate human or model review for suspicious code intent. <br>
Risk: Suspicious snippets may be copied to temporary files during review. <br>
Mitigation: Delete the temporary suspicious-code files after review, especially when scanning skills that may contain sensitive content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sypsyp97/skills/openclaw-skill-auditor) <br>
- [341 Malicious ClawHub Skills Incident](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html) <br>
- [OpenClaw Security Guide](https://docs.openclaw.ai/gateway/security) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Terminal text report with risk findings, suspicious-code preview, and install guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns process exit codes that distinguish appears-safe, review-required, and do-not-install outcomes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
