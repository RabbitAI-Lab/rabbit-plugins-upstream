## Description: <br>
Queries supplier or buyer Top N rankings by country route and year from Upkuajing customs trade data, with cursor-based pagination. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External trade analysts, procurement agents, and export teams use this skill to identify leading suppliers or buyers on a country-to-country trade route, assess market concentration, and support sourcing or sales planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses paid Upkuajing API calls and can check account balance, pricing, and recharge payment-order links. <br>
Mitigation: Confirm current pricing and obtain explicit user approval before running any query or recharge action. <br>
Risk: The skill may store the Upkuajing API key in a local plaintext file at ~/.upkuajing/.env. <br>
Mitigation: Prefer a managed environment secret when available, restrict file access to the current user, and rotate the key if it may have been exposed. <br>
Risk: The skill sends query parameters to the external Upkuajing OpenAPI service and returns provider-supplied trade-ranking data. <br>
Mitigation: Review query parameters before execution and treat returned rankings as provider data that should be checked against business requirements before use. <br>


## Reference(s): <br>
- [国家贸易概览-采供商TopN API 参考](references/customs-overview-top-n-api.md) <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-overview-top-n-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer portal](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The primary query returns paginated supplier or buyer ranking records and fee information from the provider API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
