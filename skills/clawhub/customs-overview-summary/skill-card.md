## Description: <br>
Retrieves aggregated annual trade totals, quarterly trade volume, and supplier and buyer counts by country pair from the UpKuaJing Open Platform API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External trade analysts, export teams, and market researchers use this skill to request high-level country-pair customs summaries for a selected year before deeper market analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Fee-bearing API calls, pricing checks, or top-up order creation could incur account charges or start a payment workflow. <br>
Mitigation: Tell the user a fee may apply, check current pricing when needed, and wait for explicit confirmation in a separate message before executing paid calls or top-up order creation. <br>
Risk: The skill stores or reads the UpKuaJing API key from a local plaintext file. <br>
Mitigation: Protect ~/.upkuajing/.env with appropriate local file permissions, avoid exposing terminal output that includes keys, and rotate the key if it is shared accidentally. <br>
Risk: Trade queries, account information, and payment-related requests are sent to UpKuaJing services. <br>
Mitigation: Install and run the skill only when the user trusts UpKuaJing with the trade queries and account workflow. <br>
Risk: If API logging is enabled, request and response data can be retained in local log files. <br>
Mitigation: Keep API logging disabled unless local retention is intended, and review or remove ~/.upkuajing/logs when retention is no longer needed. <br>


## Reference(s): <br>
- [Overview Summary API Reference](references/customs-overview-summary-api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-overview-summary) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing API Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with Python shell commands and formatted JSON API results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python, httpx, and UPKUAJING_API_KEY; fee-bearing API calls require explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md metadata and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
