## Description: <br>
Helps agents write, deploy, and interact with GenLayer Python smart contracts that use LLM calls, web access, and blockchain-consensus-safe non-determinism. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[acastellana](https://clawhub.ai/user/acastellana) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to draft GenLayer Intelligent Contracts, choose storage and equivalence patterns, and run CLI workflows for local, hosted development, and testnet deployment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Deploy and write commands can affect the selected GenLayer network, account, and contract state. <br>
Mitigation: Review commands before running them, use localnet or testnet first, and confirm the active network and account before deployment or write operations. <br>
Risk: LLM prompt and web-render examples can expose secrets, personal data, internal URLs, or sensitive logs if pasted into prompts or fetched content. <br>
Mitigation: Avoid using real private keys, secrets, personal data, internal URLs, or sensitive logs in shared terminals, prompts, or web-render examples. <br>
Risk: Generated Intelligent Contract examples may contain incorrect assumptions about equivalence criteria, prompt validation, or storage constraints. <br>
Mitigation: Validate output schemas, equivalence principles, storage types, and contract behavior before deploying beyond local or test networks. <br>


## Reference(s): <br>
- [GenLayer Documentation](https://docs.genlayer.com) <br>
- [GenLayer SDK](https://sdk.genlayer.com) <br>
- [GenLayer Studio](https://studio.genlayer.com) <br>
- [GenLayer GitHub](https://github.com/genlayerlabs) <br>
- [SDK API Reference](references/sdk-api.md) <br>
- [Equivalence Principles](references/equivalence-principles.md) <br>
- [Contract Examples](references/examples.md) <br>
- [Deployment Guide](references/deployment.md) <br>
- [GenVM Internals](references/genvm-internals.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python contract snippets, bash commands, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are advisory and should be reviewed before contract deployment or write transactions.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
