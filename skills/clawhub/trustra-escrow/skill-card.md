## Description: <br>
Escrow as a Service for AI agents. Create trustless USDC escrow transactions on Solana. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xasus1](https://clawhub.ai/user/xasus1) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External agents and developers use this skill to register managed wallets and operate USDC escrow workflows on Solana, including creation, payment, delivery confirmation, disputes, cancellation, and withdrawal. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can initiate payment, release, withdrawal, cancellation, dispute, and private-key export actions. <br>
Mitigation: Require explicit human review before running any command that moves funds, changes escrow state, opens a dispute, or exports wallet keys. <br>
Risk: The skill stores or uses sensitive credentials through credentials.json and TRUSTRA_API_KEY. <br>
Mitigation: Protect credentials.json and TRUSTRA_API_KEY, avoid logging secrets, and keep only minimal funds in the managed wallet. <br>
Risk: Use depends on Trustra's API, managed-wallet model, and dispute process. <br>
Mitigation: Install and operate the skill only when the Trustra service and its escrow process are trusted for the intended transaction. <br>


## Reference(s): <br>
- [Trustra Escrow on ClawHub](https://clawhub.ai/xasus1/skills/trustra-escrow) <br>
- [Trustra homepage](https://trustra.xyz) <br>
- [Trustra API base](https://api.trustra.xyz/api/v2) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides use of local Python CLI scripts that call the Trustra API and may create or update credentials.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
