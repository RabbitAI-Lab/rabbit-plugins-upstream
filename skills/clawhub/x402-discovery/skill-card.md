## Description: <br>
Discover x402-enabled services across multiple catalogs: Bazaar, Agentic Market, x402-list.com, and .well-known/x402 manifests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[marketingkioldenburg](https://clawhub.ai/user/marketingkioldenburg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to find x402-enabled services, inspect discovery catalogs and manifests, and compare endpoint metadata such as pricing, schemas, and service descriptions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill guides agents to query public discovery services and service-specific manifests, which may expose unfamiliar service URLs or paid endpoint metadata. <br>
Mitigation: Review unfamiliar service URLs and endpoint terms before using any paid x402 service; use the skill for discovery before committing to a provider. <br>
Risk: Catalogs and manifests can contain stale, inconsistent, or incomplete pricing and schema information. <br>
Mitigation: Cross-check prices and endpoint metadata across the Bazaar, x402-list.com, and service manifests before selecting a service. <br>


## Reference(s): <br>
- [x402 Homepage](https://www.x402.org) <br>
- [x402 Bazaar Discovery API](https://api.cdp.coinbase.com/x402/discovery/resources) <br>
- [x402 List Services API](https://x402-list.com/api/services) <br>
- [ClawHub Skill Page](https://clawhub.ai/marketingkioldenburg/skills/x402-discovery) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses curl-based discovery examples; no credential or payment action is required by the skill.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
