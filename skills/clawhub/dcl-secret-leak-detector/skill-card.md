## Description: <br>
Scans AI agent outputs, tool results, and pipeline data for exposed secrets and credentials before they reach users, logs, or downstream systems. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daririnch](https://clawhub.ai/user/daririnch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, DevSecOps teams, and agent builders use this skill to review AI-generated or pipeline text for exposed API keys, tokens, private keys, database URLs, and related credential leaks. It can be used as an offline checklist or, when appropriate, with the DCL Trust Oracle MCP scan for an independently verifiable result. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Highly sensitive material may be sent to an external service when using the live MCP scan. <br>
Mitigation: Use the free instruction-only checklist when content should remain entirely inside the agent context. <br>
Risk: Live scans may create durable audit records containing input hashes and finding metadata. <br>
Mitigation: Confirm the current live scan price and audit behavior before use, and avoid submitting content when permanent on-chain metadata is unacceptable. <br>
Risk: Secret detection can produce false negatives or miss unsupported credential formats. <br>
Mitigation: Treat results as a security review aid and keep separate credential hygiene controls such as secret managers, rotation, and CI scanning in place. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/daririnch/skills/dcl-secret-leak-detector) <br>
- [DCL Trust Oracle MCP endpoint](https://mcp.fronesislabs.com/mcp) <br>
- [Fronesis Labs privacy policy](https://fronesislabs.com/#privacy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with checklist steps, JSON configuration examples, code examples, and optional MCP scan result fields.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Live scan output may include verdict, risk score, redacted findings, input hash, transaction hash, chain index, timestamp, seal text, and verification URL.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
