## Description: <br>
Use Utilia's wallet-funded x402 client for live Solana mainnet priority fees, transaction diagnosis, token-risk inspection, unsigned transaction simulation, PDF-to-Markdown conversion, and audio normalization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohamedkuch](https://clawhub.ai/user/mohamedkuch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to gather live Solana preflight evidence, inspect transactions and token risk, convert public PDFs to Markdown, and normalize public audio while paying bounded USDC fees per call. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid calls can spend USDC from a configured Solana wallet. <br>
Mitigation: Use a dedicated low-balance wallet, verify the client-reported price and receipt, and keep the per-call ceiling in place. <br>
Risk: Submitted signatures, mints, transactions, account addresses, public PDFs, and public audio are sent to Utilia for processing. <br>
Mitigation: Submit only public or authorized data, avoid private documents and recordings, and confirm approval before media-processing calls. <br>
Risk: Persistent MCP configuration can expose wallet-related environment settings to future tool sessions. <br>
Mitigation: Review MCP configuration before enabling it and keep wallet secrets in the agent environment or secret manager rather than prompts, source files, or skill documents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohamedkuch/skills/utilia-solana-preflight) <br>
- [Utilia priority fees API](https://api.utilia.ink/v1/fees/priority) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration; tool responses may include structured Solana evidence, page-delimited Markdown, JSONL fee feeds, or MP3 files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Paid calls require configured Solana wallet credentials and can settle $0.002-$0.01 USDC per call.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
