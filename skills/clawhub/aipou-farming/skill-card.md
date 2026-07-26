## Description: <br>
Record meaningful AI-assisted work as privacy-preserving AIPOU receipts and claim accumulated AIPOU rewards on Base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xddneto](https://clawhub.ai/user/0xddneto) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to record AI-assisted work as AIPOU receipts, inspect farming identity and receipt status, estimate rewards, and explicitly claim eligible AIPOU rewards on Base. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AIPOU settlement can submit Base onchain transactions from a farming wallet. <br>
Mitigation: Use a dedicated low-value farming wallet and carefully review any wallet signature or Base transaction before approval. <br>
Risk: Private keys, seed phrases, raw prompts, model outputs, or private file contents could be exposed through careless tool arguments. <br>
Mitigation: Never share seed phrases or private keys in chat, and pass only non-sensitive hashes, metadata, and MCP tool results. <br>
Risk: Reward estimates, validator approval, token value, and liquidity are not guaranteed. <br>
Mitigation: Label estimates as non-final, report validator skips with reasons, and state that AIPOU is experimental, unaudited, and has intentionally tiny market liquidity. <br>


## Reference(s): <br>
- [AIPOU Protocol Reference](references/protocol.md) <br>
- [AI-Proof-of-Us Source](https://github.com/0xddneto/AI-Proof-of-Us) <br>
- [ClawHub Skill Page](https://clawhub.ai/0xddneto/skills/aipou-farming) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Markdown, Configuration] <br>
**Output Format:** [Markdown guidance with MCP tool-call instructions and concise status reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports receipt IDs, reward estimates, settlement status, wallet identity, contract information, and transaction results when returned by the configured MCP server.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
