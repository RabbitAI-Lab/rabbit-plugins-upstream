## Description: <br>
Access Chia blockchain data including blocks, transactions, addresses, CAT tokens, NFTs, network stats, and XCH price through the Spacescan.io API with an API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[koba42corp](https://clawhub.ai/user/koba42corp) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use Spacescan to retrieve Chia blockchain explorer data from Spacescan.io for blocks, transactions, addresses, coins, network status, CAT tokens, NFTs, search results, and XCH price checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Spacescan queries may include addresses, transaction IDs, NFT or CAT IDs, and search terms that are sent to Spacescan.io with the configured API key. <br>
Mitigation: Use the skill only when sharing those lookup values with Spacescan.io is acceptable. <br>
Risk: The skill requires a Spacescan API key, and storing that key in shared or synced shell profiles can expose it. <br>
Mitigation: Use a dedicated low-scope key and keep SPACESCAN_API_KEY out of shared or synced shell profiles. <br>
Risk: Running npm link creates global scan and spacescan commands on the host. <br>
Mitigation: Skip npm link when global CLI commands are not desired. <br>


## Reference(s): <br>
- [Spacescan Skill on ClawHub](https://clawhub.ai/koba42corp/skills/spacescan) <br>
- [Spacescan](https://www.spacescan.io) <br>
- [Spacescan API Plans](https://www.spacescan.io/apis) <br>
- [Chia Network](https://chia.net) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text command responses with Markdown documentation, shell examples, and JavaScript API usage snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Spacescan API key; blockchain identifiers and search queries are sent to Spacescan.io.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, package.json, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
