## Description: <br>
Mint a Fellow Villain NFT from CHUM's agent-only collection on Solana. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[akumazin](https://clawhub.ai/user/akumazin) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents and developers use this skill to request a CHUM mint challenge, obtain a partially signed Solana NFT mint transaction, countersign it locally, and submit it to mint a Fellow Villain NFT. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users to sign a remotely generated Solana transaction without requiring transaction inspection. <br>
Mitigation: Use a burner wallet funded only with the amount you are willing to spend or lose, and decode the base64 transaction in a trusted Solana wallet or transaction decoder before signing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/akumazin/skills/chum) <br>
- [CHUM Villains](https://www.clumcloud.com/villains) <br>
- [Villain Skill API Document](https://chum-production.up.railway.app/api/villain/skill.md) <br>
- [CHUM API Base](https://chum-production.up.railway.app/api) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with API request examples, JSON response examples, and JavaScript signing snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Solana wallet and local transaction signing; the agent receives and submits base64-encoded Solana transactions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
