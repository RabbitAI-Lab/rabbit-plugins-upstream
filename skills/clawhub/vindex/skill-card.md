## Description: <br>
Vindex helps agents decode VINs, retrieve merged US and Canadian recalls, summarize known issues with source citations, and estimate used-car purchase costs through free sample endpoints and paid x402 API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jcislo](https://clawhub.ai/user/jcislo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI agents use Vindex to inspect vehicle decode, recall, warranty-term, known-issue, reliability, and purchase-cost data before deciding whether to make paid x402 calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid x402 calls can incur USDC charges for successful API responses. <br>
Mitigation: Review endpoint prices, use the free /v1/sample/* endpoints first, and configure agents to ask before making x402 payments. <br>
Risk: VINs and purchase-cost parameters are sent to the Vindex API, and VINs may be cached remotely for up to 90 days. <br>
Mitigation: Send only the vehicle and jurisdiction data needed for the task, avoid adding personal information, and account for the stated cache period. <br>
Risk: The returned vehicle information is not professional, legal, purchasing, or vehicle-history advice. <br>
Mitigation: Verify consequential decisions against source databases, official documents, professional advice, or a dedicated vehicle-history report. <br>
Risk: Upstream public-data sources can be unavailable or stale, and some known-issues requests may have insufficient complaint data. <br>
Mitigation: Handle 502 and insufficient-data responses explicitly and treat recall, complaint, and cost data as time-sensitive. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jcislo/skills/vindex) <br>
- [Vindex homepage](https://vindexapi.dev) <br>
- [Vindex API agent documentation](https://api.vindexapi.dev/llms.txt) <br>
- [Vindex OpenAPI specification](https://api.vindexapi.dev/openapi.json) <br>
- [Vindex discovery document](https://api.vindexapi.dev/discovery) <br>
- [Vindex x402 payment manifest](https://api.vindexapi.dev/.well-known/x402) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API calls, Guidance] <br>
**Output Format:** [Markdown guidance with endpoint tables, API URLs, and curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents toward paid x402 API calls after free sample endpoint checks.] <br>

## Skill Version(s): <br>
1.4.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
