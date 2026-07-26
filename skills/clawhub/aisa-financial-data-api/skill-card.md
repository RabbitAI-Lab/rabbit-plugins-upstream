## Description: <br>
Query real-time and historical financial data across equities and crypto, including prices, market moves, metrics, and trends for analysis, alerts, and reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aisadevco](https://clawhub.ai/user/aisadevco) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to query AIsa financial-data endpoints for equities and crypto research, portfolio tracking, screening, reporting, and alert workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires AISA_API_KEY and sends financial-data queries to AIsa's external API endpoint. <br>
Mitigation: Provide only the required AISA_API_KEY, avoid including unrelated secrets or private account exports in requests, and follow the provider's data-handling documentation. <br>
Risk: Financial-data responses may influence analysis, alerts, or reporting workflows. <br>
Mitigation: Review API responses and downstream conclusions before using them for material financial decisions or external reporting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aisadevco/skills/aisa-financial-data-api) <br>
- [OpenClaw homepage](https://openclaw.ai) <br>
- [AIsa API reference](https://aisa.mintlify.app/api-reference/introduction) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash and Python command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses AISA_API_KEY and sends requests to the AIsa API endpoint.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
