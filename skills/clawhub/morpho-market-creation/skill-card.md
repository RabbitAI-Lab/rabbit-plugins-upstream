## Description: <br>
Deploys Morpho markets backed by Api3 oracles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[api3dao](https://clawhub.ai/user/api3dao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and protocol operators use this skill to walk through validating Api3 data feeds, preparing Morpho oracle parameters, deploying or manually submitting an oracle transaction, and creating a Morpho market. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A full wallet mnemonic in a local .env file can expose all funds controlled by that seed phrase if the machine or project directory is compromised. <br>
Mitigation: Use a dedicated low-value deployment wallet or Safe/manual signing flow, avoid primary seed phrases, and remove local mnemonic material after use. <br>
Risk: Incorrect chain, token, oracle, IRM, or LLTV values can create irreversible or high-impact on-chain transactions. <br>
Mitigation: Verify chain ID and every address against trusted sources, test on a non-production network first, and prefer Safe or Etherscan/manual review before signing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/api3dao/skills/morpho-market-creation) <br>
- [Api3 Market](https://market.api3.org) <br>
- [Morpho Oracle Tester](https://oracles.morpho.dev/oracle-tester) <br>
- [Morpho Blue addresses](https://docs.morpho.org/get-started/resources/addresses/#morpho-blue) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with command snippets, URLs, transaction details, and JSON configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May instruct the user to edit oracle-params.json and market-params.json and may report transaction hashes, oracle addresses, and market IDs.] <br>

## Skill Version(s): <br>
0.5.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
