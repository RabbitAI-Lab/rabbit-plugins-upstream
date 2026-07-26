## Description: <br>
Ethereum History provides read-only factual data about historical Ethereum mainnet contracts, including deployment details, bytecode, decompiled code, and documented context when available. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cartoonitunes](https://clawhub.ai/user/cartoonitunes) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to look up historical Ethereum mainnet contract facts by address, era, or deployment time, then summarize or use the returned JSON for analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Contract addresses and query filters are sent to EthereumHistory.com during lookup. <br>
Mitigation: Avoid submitting sensitive research queries when that disclosure matters, and review network use before deployment in restricted environments. <br>
Risk: Historical or technical contract details may be incomplete or require higher-confidence confirmation. <br>
Mitigation: Verify important claims against primary blockchain data, block explorers, or other authoritative sources before relying on them. <br>
Risk: Discovery queries can return empty results when the backing data source is unavailable or not configured. <br>
Mitigation: Handle empty result sets explicitly and use address-specific lookups or independent sources when completeness matters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cartoonitunes/skills/ethereum-history) <br>
- [Ethereum History](https://ethereumhistory.com) <br>
- [Ethereum History API manifest](https://ethereumhistory.com/api/agent/manifest) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance] <br>
**Output Format:** [Markdown guidance with HTTPS GET requests and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only GET requests; no authentication required; query parameters support address, era, time range, pagination, and discovery filters.] <br>

## Skill Version(s): <br>
1.0.0 (source: target metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
