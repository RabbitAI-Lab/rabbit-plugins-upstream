## Description: <br>
Security audit and threat model for OpenClaw gateway hosts, producing an OK/VULNERABLE report with evidence and fixes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[misirov](https://clawhub.ai/user/misirov) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and security engineers use this skill to audit OpenClaw gateway hosts, inspect configuration and exposure evidence, and generate a concise threat model with prioritized remediation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill directs the agent to run a local collection script immediately while inspecting sensitive host and OpenClaw configuration state. <br>
Mitigation: Review the bundled script and allowlist before use, run it in a controlled environment, and confirm that collection scope matches the audit need. <br>
Risk: The generated evidence bundle and report may contain sensitive operational details even after redaction. <br>
Mitigation: Treat generated audit artifacts as sensitive data, keep them local unless sharing is required, and review excerpts before disclosure. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/misirov/skills/clawdstrike-test) <br>
- [Required checks](artifact/references/required-checks.md) <br>
- [Report format](artifact/references/report-format.md) <br>
- [Gateway exposure and auth](artifact/references/gateway.md) <br>
- [Verified mode allowlist](artifact/references/verified-allowlist.md) <br>
- [Threat model template](artifact/references/threat-model.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown security report with a findings table, redacted evidence excerpts, threat model, and remediation plan] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local verified-bundle evidence; proposes fixes as instructions unless the user explicitly requests changes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
