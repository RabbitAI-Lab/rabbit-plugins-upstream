## Description: <br>
A read-only Model Context Protocol server that lets AI agents retrieve Vitruveo and EVM blockchain data through the XiaoBenYang API service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent users use this skill to answer blockchain data questions such as balances, blocks, transactions, contract reads, token metadata, and NFT ownership without writing transactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends wallet addresses, token IDs, transaction hashes, contract query data, and the XBY API key to a third-party API service. <br>
Mitigation: Install only when the XiaoBenYang service is trusted for the intended data, avoid sending sensitive identifiers, and rotate the API key if exposure is suspected. <br>
Risk: The skill persists the XBY API key in a local .env file. <br>
Mitigation: Restrict file access, avoid shared workspaces for the stored key, and remove or rotate the key when the skill is no longer needed. <br>
Risk: The server security summary reports stale or mismatched metadata. <br>
Mitigation: Review the release metadata, artifact frontmatter, and behavior before installation, especially the 1.0.1 release metadata versus 1.0.0 artifact frontmatter. <br>


## Reference(s): <br>
- [XiaoBenYang API key and service](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/blockchain-data-service) <br>
- [ALinkLab publisher profile](https://clawhub.ai/user/alinklab) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration guidance] <br>
**Output Format:** [Markdown summaries derived from JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY API key and returns read-only blockchain data from a third-party API service.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter is 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
