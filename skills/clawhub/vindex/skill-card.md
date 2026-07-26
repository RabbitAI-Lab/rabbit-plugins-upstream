## Description: <br>
Vehicle intelligence for AI agents: decode 17-character VINs, retrieve merged US and Canadian recalls, summarize known issues with ODI citations and reliability aggregates, and estimate itemized used-car drive-away costs for US and Canadian jurisdictions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jcislo](https://clawhub.ai/user/jcislo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and vehicle-shopping agents use Vindex to decode VINs, inspect US and Canadian recalls and known issues, and estimate US and Canadian used-car purchase costs through free samples or paid per-call API endpoints. <br>

### Deployment Geography for Use: <br>
Global use; vehicle data and purchase-cost coverage are scoped to United States and Canadian jurisdictions. <br>

## Known Risks and Mitigations: <br>
Risk: Paid API calls may trigger x402 USDC payment for non-sample endpoints. <br>
Mitigation: Use the free /v1/sample/* endpoints first, confirm active payment mode at /health, and review per-call prices before invoking paid routes. <br>
Risk: VINs and purchase-cost parameters are sent to an external API; VINs may be cached for up to 90 days. <br>
Mitigation: Avoid sending VINs considered sensitive unless the cache retention and external API use are acceptable. <br>
Risk: Vehicle safety and purchase-cost outputs are informational and not professional, legal, or purchasing advice. <br>
Mitigation: Treat responses as decision-support data and verify material recall, warranty, tax, fee, lien, accident, and odometer questions against authoritative sources. <br>


## Reference(s): <br>
- [Vindex Skill Page](https://clawhub.ai/jcislo/skills/vindex) <br>
- [Vindex Homepage](https://vindexapi.dev) <br>
- [Vindex Agent Documentation](https://api.vindexapi.dev/llms.txt) <br>
- [Vindex OpenAPI Specification](https://api.vindexapi.dev/openapi.json) <br>
- [Vindex Discovery JSON](https://api.vindexapi.dev/discovery) <br>
- [Vindex x402 Payment Manifest](https://api.vindexapi.dev/.well-known/x402) <br>
- [Vindex A2A Agent Card](https://api.vindexapi.dev/.well-known/agent-card.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with endpoint tables, curl examples, and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node for the documented agent tooling; paid calls use x402 USDC settlement, while sample endpoints are free.] <br>

## Skill Version(s): <br>
1.3.0 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
