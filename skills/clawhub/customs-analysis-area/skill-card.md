## Description: <br>
Queries UpKuaJing customs trade area distribution data by country or region for a specified HS code, country type, and recent-month window. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Trade analysts, market researchers, and import-export professionals use this skill to compare exporter and importer country activity for a product HS code and assess geographic market distribution across customs data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores an UpKuaJing API key in a plaintext local environment file. <br>
Mitigation: Install only when local plaintext credential storage is acceptable, restrict file access, and rotate the API key if exposure is suspected. <br>
Risk: Trade queries and account actions can incur UpKuaJing charges or create top-up payment links. <br>
Mitigation: Review pricing and require explicit user confirmation before paid queries or recharge actions. <br>
Risk: The skill sends trade-query parameters and performs version-status checks against UpKuaJing services. <br>
Mitigation: Use the skill only when sharing those query parameters with UpKuaJing is acceptable for the user's workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-analysis-area) <br>
- [Area Distribution API Reference](references/customs-analysis-area-api.md) <br>
- [UpKuaJing homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing API pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API results from the helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; trade queries may incur UpKuaJing API fees and should wait for explicit user confirmation before paid calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
