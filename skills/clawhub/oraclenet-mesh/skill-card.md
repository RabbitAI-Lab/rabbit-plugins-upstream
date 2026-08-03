## Description: <br>
OracleNet routes agent tasks to live external data and MCP capabilities, starting with free discovery and exposing pricing and verification metadata before any paid route. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tooloracle](https://clawhub.ai/user/tooloracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent operators use this skill when an agent needs current data, capability discovery, route comparison, or provenance-aware results beyond the model's training cutoff. It helps agents perform free discovery first, report limitations, and stop for explicit authorization before any paid x402 route. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Routing intents are sent to an external live-data service and could expose sensitive details if the user includes secrets or personal data. <br>
Mitigation: Keep intents to short routing hints, do not include secrets or personal data, and rely on the bundled route script's credential-pattern guard as a backstop rather than as the only control. <br>
Risk: Metered x402 routes can incur payment if an agent sends a payment header after receiving a 402 quote. <br>
Mitigation: Use free discovery first, treat 402 responses as quotes, require explicit authorization and a stated budget, verify chain and asset details, and stop when settlement status is unclear. <br>
Risk: Live data responses may be unsigned, stale, incomplete, or only provenance-bearing rather than cryptographically verified. <br>
Mitigation: Report verification status explicitly, verify signatures against the JWKS when present, record timestamps and source URLs, and avoid presenting returned data as legal, financial, regulatory, or compliance decisions. <br>
Risk: Custom or non-HTTPS endpoints could bypass the documented ToolOracle security posture. <br>
Mitigation: Keep the default HTTPS endpoints unless a reviewer has approved an alternative, and avoid installing the skill when the deployment cannot permit external ToolOracle routing. <br>


## Reference(s): <br>
- [Route Recipes](references/route-recipes.md) <br>
- [Verification](references/verification.md) <br>
- [x402 Payment Safety](references/x402-safety.md) <br>
- [ToolOracle Homepage](https://tooloracle.io) <br>
- [ToolOracle Agent Discovery Card](https://tooloracle.io/.well-known/agent.json) <br>
- [OracleNet Free Handshake](https://tooloracle.io/handshake) <br>
- [OracleNet MCP Entry Point](https://tooloracle.io/quantum/mcp/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, configuration snippets, and JSON route summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include selected endpoint, price status, payment boundary, verification status, provenance, limitations, and next action.] <br>

## Skill Version(s): <br>
3.0.0 (source: frontmatter and server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
