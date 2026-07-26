## Description: <br>
Provides aggregated customs-trade statistics for overseas companies by company ID, including trading frequency, shipment weight, product quantity, transaction value, partner counts, and trade date range. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Export teams, analysts, researchers, and agent operators use this skill to retrieve summarized customs-trade activity for a known company ID and role. It supports supplier screening, buyer validation, trade-scale assessment, and partner-network analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores and reads an UpKuaJing API key from a local plaintext env file. <br>
Mitigation: Use a dedicated API key, restrict access to ~/.upkuajing/.env, avoid sharing the file, and remove the key when it is no longer needed. <br>
Risk: The skill can make paid API calls and includes account top-up flows. <br>
Mitigation: Confirm pricing and obtain explicit user approval in a separate message before running any paid query or account top-up action. <br>
Risk: The package contacts UpKuaJing for both customs queries and version checks. <br>
Mitigation: Install and run it only in environments where outbound calls to UpKuaJing services are acceptable. <br>
Risk: API logging can retain sensitive supplier or trade-research data locally if enabled. <br>
Mitigation: Keep API logging disabled unless local retention is explicitly acceptable, and review any retained logs before sharing the environment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-company-stats) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [Company Basic Trade Statistics API](references/customs-company-stats-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python, httpx, UPKUAJING_API_KEY, and explicit user confirmation before paid API calls.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
