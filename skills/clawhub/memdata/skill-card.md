## Description: <br>
MemData provides persistent memory for autonomous agents using wallet-based identity, pay-per-query access, and optional encrypted storage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thelabvenice](https://clawhub.ai/user/thelabvenice) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use MemData to store, retrieve, and manage persistent session memory through wallet-authenticated API endpoints. It supports standard remote storage and optional encrypted storage for private memories. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A remote service may store agent memories under a wallet identity. <br>
Mitigation: Avoid storing sensitive data in standard mode and enable encryption for private memories. <br>
Risk: Wallet-paid API calls can incur charges. <br>
Mitigation: Use a limited wallet and review payment and signature prompts before approving requests. <br>
Risk: Stored memories can be deleted through the artifact endpoint. <br>
Mitigation: Require explicit confirmation before deleting stored memories. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thelabvenice/skills/memdata) <br>
- [MemData](https://memdata.ai) <br>
- [MemData Docs](https://memdata.ai/docs) <br>
- [x402 Protocol](https://www.x402.org) <br>
- [Lit Protocol](https://litprotocol.com) <br>
- [Storacha](https://storacha.network) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API calls, configuration] <br>
**Output Format:** [Markdown with JSON request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes wallet-authenticated x402 payment flow, memory endpoint usage, optional encryption setup, and memory deletion guidance.] <br>

## Skill Version(s): <br>
1.8.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
