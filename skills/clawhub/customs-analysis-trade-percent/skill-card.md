## Description: <br>
Query trade percentage analysis retrieves company-level trade share data for a specified HS code and ranks companies by trade volume. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Trade analysts, sourcing agents, and market researchers use this skill to identify major companies trading a product, analyze market concentration, compare supplier competition, and discover potential trade partners from customs data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an UpKuaJing API key and stores or reads it from ~/.upkuajing/.env. <br>
Mitigation: Treat the API key like a password, restrict file access, and review or rotate the key if the local environment may be shared. <br>
Risk: Successful data queries incur paid API charges. <br>
Mitigation: Require explicit user confirmation before each fee-incurring query and check current pricing before execution. <br>
Risk: When balance is insufficient, the auth helper can create a recharge order and return a payment URL. <br>
Mitigation: Review any top-up prompt and payment URL before opening it or completing payment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-analysis-trade-percent) <br>
- [UpKuaJing homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [Trade Percent API reference](references/customs-analysis-trade-percent-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns ranked company trade-share records with fee information when API calls succeed; requires Python and UPKUAJING_API_KEY.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
