## Description: <br>
DCL Prompt Firewall helps agents screen untrusted input for prompt injection, jailbreak, role-switch, and instruction-override attempts before passing it to a model. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daririnch](https://clawhub.ai/user/daririnch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill as a pre-execution gate for user messages, tool results, web content, and retrieved documents. It supports either a paid DCL Trust Oracle MCP evaluation or a free checklist for manual screening. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The live screening path sends input to an external MCP service for evaluation. <br>
Mitigation: Use the live path only when external evaluation is acceptable for the data being screened; use the included free checklist when no network call should occur. <br>
Risk: Paid calls require a wallet-enabled client and per-call USDC payment. <br>
Mitigation: Configure the MCP endpoint and payment flow deliberately, and confirm server-reported prices before using the paid tools. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/daririnch/skills/dcl-prompt-firewall) <br>
- [DCL Trust Oracle MCP endpoint](https://mcp.fronesislabs.com/mcp) <br>
- [DCL Security Suite hub](https://hub.fronesislabs.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, API Calls, JSON] <br>
**Output Format:** [Markdown guidance with JSON configuration and tool-call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Paid live calls can return verdict metadata, confidence, hashes, policy version, drift fields, and an audit transaction hash; the free checklist returns text guidance only.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
