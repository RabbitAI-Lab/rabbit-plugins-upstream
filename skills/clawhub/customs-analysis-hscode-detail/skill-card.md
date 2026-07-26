## Description: <br>
Query HS code detail information by retrieving Chinese and English descriptions for a given HS code from UpKuaJing customs data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Trade professionals, analysts, and import-export practitioners use this skill to look up an 8-digit HS code and confirm the Chinese and English product descriptions before tariff classification or trade analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may manage an UpKuaJing API key in a local plaintext .env file. <br>
Mitigation: Prefer a managed secret mechanism, and avoid displaying the .env file contents in chat, logs, or shared output. <br>
Risk: The workflow can make paid API calls, check account and balance information, and create top-up payment links. <br>
Mitigation: Require explicit user confirmation before billable calls or top-up actions, and review account or billing output before sharing it. <br>
Risk: The skill performs a same-service version check and writes local cache state. <br>
Mitigation: Review the network access and local cache behavior before installation in environments with strict persistence or egress rules. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-analysis-hscode-detail) <br>
- [HS Code Detail API Reference](references/customs-analysis-hscode-detail-api.md) <br>
- [UpKuaJing homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing API pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, API calls, Configuration guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python, httpx, and UPKUAJING_API_KEY; API calls may incur fees and should be confirmed before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
