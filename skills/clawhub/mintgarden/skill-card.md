## Description: <br>
MintGarden helps agents browse, search, and analyze Chia NFTs, collections, profiles, marketplace activity, and trading data through the public MintGarden API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[koba42corp](https://clawhub.ai/user/koba42corp) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to answer questions about Chia NFTs, inspect collections and profiles, and retrieve marketplace activity in CLI or messaging-friendly text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Marketplace events and collection activity may be broader than a command name suggests. <br>
Mitigation: Confirm the collection or profile scope in the returned data before using results for monitoring, reporting, or downstream decisions. <br>
Risk: NFT pricing, trading, and activity data can be incomplete or time-sensitive. <br>
Mitigation: Do not rely on this skill's output alone for trading or due-diligence decisions; corroborate against MintGarden and other authoritative sources. <br>
Risk: The release has dependency hygiene concerns even though the security verdict is clean. <br>
Mitigation: Pin and refresh dependencies, then rerun security scans before deploying the skill in a managed environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/koba42corp/skills/mintgarden) <br>
- [MintGarden API documentation](https://api.mintgarden.io/docs) <br>
- [MintGarden](https://mintgarden.io) <br>
- [Chia Network](https://chia.net) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, code, guidance] <br>
**Output Format:** [Plain text responses for CLI and messaging clients, with JavaScript API usage examples in documentation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Command outputs are formatted for terminals and chat clients; API calls use public MintGarden endpoints with no API key.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, package.json, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
