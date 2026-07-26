## Description: <br>
Locus payment tools for AI agents that can help send payments, check wallet balances, list tokens, approve token spending, and process payment-related email actions through wallet-connected Locus MCP tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cdermott7](https://clawhub.ai/user/cdermott7) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to configure Locus payment tools, discover wallet/payment capabilities available to their permission group, and guide payment workflows such as balance checks, token approvals, and user-approved crypto payments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can enable wallet-connected payment and token-approval actions through an agent. <br>
Mitigation: Install only when wallet-connected crypto payments are intended, and require explicit user confirmation before any payment or approval. <br>
Risk: Persistent API-key configuration may retain payment access after setup. <br>
Mitigation: Use a least-privilege Locus API key with spending limits and whitelisted recipients where available, and know how to remove the mcporter Locus config or revoke the key. <br>
Risk: Incorrect recipients, tokens, chains, or allowances can cause irreversible payment or approval mistakes. <br>
Mitigation: Manually verify every recipient, amount, token, chain, and token approval, and avoid unlimited allowances. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cdermott7/skills/locus) <br>
- [Locus website](https://paywithlocus.com) <br>
- [Locus app](https://app.paywithlocus.com) <br>
- [Locus MCP endpoint](https://mcp.paywithlocus.com/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown with inline bash commands and mcporter command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Discovers dynamic MCP tools by permission group before proposing tool calls.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
