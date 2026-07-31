## Description: <br>
Purchases Api3 data feed subscriptions from market.api3.org. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[api3dao](https://clawhub.ai/user/api3dao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and blockchain operators use this skill to select an Api3 dAPI feed, choose a supported chain and deviation threshold, quote the subscription cost, execute the on-chain purchase, and optionally verify the deployed reader proxy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can sign and submit real blockchain transactions that spend funds from WALLET_MNEMONIC. <br>
Mitigation: Use a dedicated low-balance wallet, avoid storing a main wallet mnemonic in the skill directory, and verify the chain, feed, deviation, amount, and sponsor wallet before approving the purchase. <br>
Risk: A confirmed purchase transaction may be irreversible. <br>
Mitigation: Review the quoted subscription price and amount to send before execution, and use the optional provider value check to sanity-check the selected feed before paying. <br>


## Reference(s): <br>
- [Api3 Market](https://market.api3.org) <br>
- [Api3 Signed API public endpoint pattern](https://signed-api.api3.org/public/${api.airnode}) <br>
- [ClawHub skill page](https://clawhub.ai/api3dao/skills/api3-data-feed-purchase) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and summarized script output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides package installation, feed and chain validation, price quote review, purchase execution, and optional feed readback.] <br>

## Skill Version(s): <br>
0.6.0 (source: SKILL.md metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
