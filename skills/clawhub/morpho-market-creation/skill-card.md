## Description: <br>
Deploys Morpho markets backed by Api3 oracles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[api3dao](https://clawhub.ai/user/api3dao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and DeFi operators use this skill to validate Api3 oracle feeds, prepare Morpho oracle parameters, deploy or select an oracle, and create a Morpho market through guided steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help submit live blockchain transactions using a raw wallet mnemonic. <br>
Mitigation: Use a dedicated low-value deployer wallet, never a personal or treasury seed phrase, and prefer Safe or Etherscan signing over the mnemonic script path. <br>
Risk: Incorrect oracle or market parameters can create an unintended on-chain market. <br>
Mitigation: Review oracle-params.json and market-params.json carefully, verify Api3 feed addresses with the Morpho Oracle Tester, and confirm token contract addresses are not Api3 reader proxy addresses. <br>
Risk: Unpinned dependencies can change behavior between installs. <br>
Mitigation: Pin dependencies before using the skill for mainnet work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/api3dao/skills/morpho-market-creation) <br>
- [Api3 Market](https://market.api3.org) <br>
- [Morpho Oracle Tester](https://oracles.morpho.dev/oracle-tester) <br>
- [Morpho Blue addresses](https://docs.morpho.org/get-started/resources/addresses/#morpho-blue) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides parameter collection, feed validation, oracle deployment choices, and Morpho market creation.] <br>

## Skill Version(s): <br>
0.4.1 (source: SKILL.md frontmatter, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
