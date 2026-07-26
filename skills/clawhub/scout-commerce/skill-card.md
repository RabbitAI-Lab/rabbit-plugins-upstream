## Description: <br>
Search for products on Amazon/shopify and buy with USDC on Solana. Swap tokens using Jupiter. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xasus1](https://clawhub.ai/user/xasus1) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External shoppers and agents use this skill to search Amazon and Shopify products, create a Scout/Crossmint wallet, buy eligible U.S.-shipped products with USDC, check order status, and swap supported Solana tokens through Scout/Jupiter workflows. <br>

### Deployment Geography for Use: <br>
United States <br>

## Known Risks and Mitigations: <br>
Risk: The skill can initiate purchases and token swaps that spend wallet funds. <br>
Mitigation: Use only a low-balance wallet and personally confirm every buy or swap before execution. <br>
Risk: credentials.json can contain transaction-authorizing credentials and shipping PII in plaintext. <br>
Mitigation: Prefer SCOUT_API_KEY or a secure secret store, restrict file access, and avoid shared machines. <br>
Risk: The security verdict is suspicious because the skill combines commerce, Solana swaps, and limited safeguards. <br>
Mitigation: Review the scripts and dependency versions before installing or using the skill with real funds. <br>


## Reference(s): <br>
- [Scout Commerce on ClawHub](https://clawhub.ai/xasus1/skills/scout-commerce) <br>
- [Scout Homepage](https://scout.trustra.xyz) <br>
- [Scout API Base Endpoint](https://scout-api.trustra.xyz/api/v2) <br>
- [Jupiter Token Metadata Endpoint](https://tokens.jup.ag/tokens) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or consume local credentials.json containing API key, wallet address, and shipping profile.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
