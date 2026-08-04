## Description: <br>
DCL Policy Enforcer audits agent or LLM outputs through a paid DCL Trust Oracle MCP service or a local checklist, returning policy verdicts and audit metadata for pre-action gating. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daririnch](https://clawhub.ai/user/daririnch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to gate risky agent actions and review generated outputs for jailbreak, safety, quality, and regulatory-theme issues before delivery or execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The live evaluation path makes paid remote MCP calls and charges USDC per call. <br>
Mitigation: Use the included manual checklist when network access, payment, or remote evaluation is not acceptable; confirm server-side tool pricing at call time. <br>
Risk: The service creates persistent hash-based audit records for evaluated outputs. <br>
Mitigation: Use the manual checklist for highly sensitive content or when durable audit metadata is not desired. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/daririnch/skills/dcl-policy-enforcer) <br>
- [DCL Trust Oracle MCP Endpoint](https://mcp.fronesislabs.com/mcp) <br>
- [Fronesis Labs DCL Security Suite](https://hub.fronesislabs.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON and Python examples; remote MCP evaluation tools return JSON verdict and audit metadata.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Paid live evaluations may produce COMMIT or NO_COMMIT verdicts, confidence, reason, tx_hash, chain_index, input_hash, policy_version, drift_mode, and drift_score.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence; artifact frontmatter states 3.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
