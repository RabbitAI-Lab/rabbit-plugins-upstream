## Description: <br>
Use this skill to run paid pre-action audits of AI agent or LLM output via the live DCL Trust Oracle MCP server, or to apply a free manual checklist for quick local review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daririnch](https://clawhub.ai/user/daririnch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to gate risky AI actions, screen outputs for jailbreak or safety concerns, and obtain audit metadata before allowing a response or action to proceed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live evaluation sends the text being assessed to an external MCP service and may require paid USDC settlement on Base. <br>
Mitigation: Confirm network, payment, and data-sharing requirements before live use; use the free checklist path when external calls or payment are not acceptable. <br>
Risk: Server-side tool prices and behavior may change at call time. <br>
Mitigation: Review the MCP tool descriptions returned by the server and apply wallet spending controls before running paid evaluations. <br>
Risk: The manual checklist is a heuristic aid, not a certification against a specific law or standard. <br>
Mitigation: Use qualified human review for regulated, high-stakes, or legally sensitive decisions. <br>


## Reference(s): <br>
- [DCL Trust Oracle MCP endpoint](https://mcp.fronesislabs.com/mcp) <br>
- [Fronesis Labs DCL Security Suite](https://hub.fronesislabs.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, code, JSON] <br>
**Output Format:** [Markdown guidance with JSON configuration snippets, Python call examples, and JSON-shaped MCP tool responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Live evaluation tools may return verdict, confidence, reason, tx_hash, chain_index, input_hash, policy_version, drift_mode, and drift_score.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
