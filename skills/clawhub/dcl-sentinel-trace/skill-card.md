## Description: <br>
Detects and redacts personally identifiable information in AI outputs before delivery, logging, storage, or downstream processing, with a free checklist mode and an optional paid live MCP regex scan. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daririnch](https://clawhub.ai/user/daririnch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, data teams, and AI system operators use this skill as a privacy checkpoint to detect and redact personal data in generated text, datasets, or retrieved content before logging, storage, delivery, or downstream processing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live MCP mode may transmit the text being scanned to Fronesis Labs and incur a per-call USDC charge. <br>
Mitigation: Use the free checklist for local-only review, and use live MCP mode only when external scanning, payment, and an on-chain verification record are acceptable. <br>
Risk: Pattern-based PII detection can miss unsupported identity formats or produce false positives. <br>
Mitigation: Treat the output as a privacy review checkpoint and keep human or policy review for high-risk releases and regulated data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/daririnch/skills/dcl-sentinel-trace) <br>
- [DCL Trust Oracle MCP endpoint](https://mcp.fronesislabs.com/mcp) <br>
- [Fronesis Labs privacy policy](https://fronesislabs.com/#privacy) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration, code, JSON] <br>
**Output Format:** [Markdown checklist guidance with JSON configuration and result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Optional live MCP mode can return a verdict, findings, redacted samples, input hash, transaction hash, and verification URL; free mode stays in the agent context.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
