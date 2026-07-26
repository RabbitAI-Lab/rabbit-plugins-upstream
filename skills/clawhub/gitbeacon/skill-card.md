## Description: <br>
Gitbeacon gives agents GitHub trend intelligence from daily scans of trending repositories, including structured digests and enriched repository rows, with free discovery endpoints and paid x402 calls over USDC on Base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jcislo](https://clawhub.ai/user/jcislo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use Gitbeacon to inspect current GitHub repository trends, compare daily or historical digests, and retrieve enriched repository rows for downstream analysis. The skill is useful when an agent needs trend summaries, language signals, notable projects, or machine-readable API discovery before choosing whether to use paid endpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid endpoints require signing an x402 USDC authorization on Base Mainnet, which can spend funds if the challenge is accepted. <br>
Mitigation: Confirm the x402 challenge amount and network before signing, use a wallet with limited funds or spending controls, and inspect free endpoints first to understand response shapes. <br>
Risk: Digest analysis is model-generated and may be imperfect or stale for time-sensitive decisions. <br>
Mitigation: Check the scanDate or digestDate provenance included in responses and corroborate important findings before acting on them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jcislo/skills/gitbeacon) <br>
- [Gitbeacon Homepage](https://gitbeacon.dev) <br>
- [Gitbeacon API](https://api.gitbeacon.dev) <br>
- [Latest Digest Endpoint](https://api.gitbeacon.dev/v1/digests/latest) <br>
- [OpenAPI Specification](https://api.gitbeacon.dev/openapi.json) <br>
- [API Discovery](https://api.gitbeacon.dev/discovery) <br>
- [x402 Payment Manifest](https://api.gitbeacon.dev/.well-known/x402) <br>
- [A2A Agent Card](https://api.gitbeacon.dev/.well-known/agent-card.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with endpoint tables, curl examples, and TypeScript payment-client code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node for the documented x402 JavaScript client examples; paid calls require USDC on Base Mainnet.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
