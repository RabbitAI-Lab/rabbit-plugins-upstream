## Description: <br>
Swap tokens on Solana via Jupiter aggregator and check wallet balances. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[imthatcarlos](https://clawhub.ai/user/imthatcarlos) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to check Solana wallet balances, request Jupiter swap quotes, and prepare token swaps after reviewing quote details and confirming execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The transaction-signing step uses the user's Solana keypair and depends on a helper script that is absent from the artifact. <br>
Mitigation: Review before installing, use only a limited-funds wallet, and do not run the signing step unless the exact jupiter-swap.mjs implementation is present from a trusted, reviewed source. <br>
Risk: Incorrect token mints, amounts, slippage, price impact, or minimum received values can lead to an unintended swap. <br>
Mitigation: Verify token mints, amounts, slippage, price impact, and minimum received before confirming any swap, and require explicit user confirmation before signing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/imthatcarlos/skills/solana-swaps) <br>
- [Jupiter Quote API](https://api.jup.ag/swap/v1/quote) <br>
- [Jupiter Swap API](https://api.jup.ag/swap/v1/swap) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and CLI output summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Solana CLI, SPL Token CLI, curl, jq, node, SOLANA_KEYPAIR_PATH, and JUPITER_API_KEY.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
