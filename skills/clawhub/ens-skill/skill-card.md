## Description: <br>
Resolves ENS names (.eth) to Ethereum addresses and reverse-resolves addresses while supporting ENS profile lookup and guidance for registering, renewing, and managing .eth names. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fabriziogianni7](https://clawhub.ai/user/fabriziogianni7) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to resolve ENS names and wallet addresses, retrieve ENS profile information, and receive step-by-step guidance for ENS registration, renewal, record updates, and transaction confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ENS names and wallet addresses may be queried through third-party ENS or profile providers. <br>
Mitigation: Use lookups only when needed, cache results within the session, and avoid unnecessary repeated queries. <br>
Risk: ENS records can change, which can cause funds or record updates to target the wrong address. <br>
Mitigation: Before any registration, renewal, transfer, or record update, confirm the resolved 0x address, chain, cost, and wallet prompt with the user. <br>
Risk: .eth registration and renewal require Ethereum mainnet ETH for name cost and gas. <br>
Mitigation: Verify Ethereum mainnet as the chain, present current cost and gas context, and flag when the user may need to bridge funds before approving a transaction. <br>
Risk: Stored ENS preferences and expiry reminders are per-user data. <br>
Mitigation: Keep ENS strategy data isolated per user and never cross-read another user's stored ENS names or preferences. <br>


## Reference(s): <br>
- [ENS Documentation](https://docs.ens.domains/) <br>
- [ENS Manager App](https://ens.app/myname.eth) <br>
- [web3.bio Profile API](https://api.web3.bio/profile/vitalik.eth) <br>
- [ENS Subgraph Endpoint](https://gateway.thegraph.com/api/$GRAPH_API_KEY/subgraphs/id/5XqPmWe6gjyrJtFn9cLy237i4cWw2j9HcUJEXsP5qGtH) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, API URLs, and transaction checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include ENS names, wallet addresses, API endpoints, contract addresses, and per-user strategy JSON examples.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and user changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
