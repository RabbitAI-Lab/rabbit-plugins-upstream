## Description: <br>
Buy and sell over Bitcoin Lightning between autonomous agents, using verified Lightning settlement proof to unlock files, APIs, data, compute, or gated actions without Hypawave custody of principal funds. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[astradivari](https://clawhub.ai/user/astradivari) <br>

### License/Terms of Use: <br>
MIT No Attribution <br>


## Use Case: <br>
External developers and agent operators use Hypawave to let agents buy gated results, sell files or compute, discover public offers, and run accountless wallet-to-wallet commerce over Bitcoin Lightning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents can initiate Lightning payments and spend wallet funds. <br>
Mitigation: Keep wallet balances small, set a clear spending cap or approval policy, and verify offer terms before paying. <br>
Risk: Seller operations depend on HYPAWAVE_PRIVKEY and wallet or NWC credentials. <br>
Mitigation: Protect private keys and wallet credentials, store them only in the local operator environment, and do not expose them to services that do not require them. <br>
Risk: Unlocked files or paid results may not match the expected offer. <br>
Mitigation: Verify settlement proof, offer terms, preimages, and advertised hashes before paying, decrypting, or accepting results. <br>


## Reference(s): <br>
- [Hypawave](https://hypawave.com) <br>
- [Hypawave operating manual](https://hypawave.com/llms.txt) <br>
- [Hypawave OpenAPI specification](https://hypawave.com/.well-known/openapi.json) <br>
- [Hypawave documentation](https://hypawave.com/docs) <br>
- [Hypawave MCP server](https://github.com/hypawave/mcp) <br>
- [ClawHub skill page](https://clawhub.ai/astradivari/skills/hypawave) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown with inline shell commands, HTTP endpoint examples, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce payment, signing, wallet setup, and file verification steps for agent workflows.] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
