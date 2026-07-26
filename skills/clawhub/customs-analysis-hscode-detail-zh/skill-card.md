## Description: <br>
Queries Upkuajing's OpenAPI for Chinese and English descriptions of a specified HS code. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External trade professionals, analysts, and import/export users use this skill to identify the product category represented by an HS code and retrieve Chinese and English descriptions before customs classification or trade-data analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid API and each HS-code detail query may incur charges. <br>
Mitigation: Tell the user a query will cost money and wait for explicit confirmation in a separate message before running paid calls. <br>
Risk: The UPKUAJING_API_KEY credential can expose account access if pasted or displayed. <br>
Mitigation: Treat UPKUAJING_API_KEY as a secret and avoid printing, pasting, or showing .env contents in chat. <br>
Risk: Recharge and payment flows can direct users to external payment pages. <br>
Mitigation: Review recharge or payment URLs with the user before payment and continue only after the user confirms payment success. <br>
Risk: Incorrect parameters can produce failed or misleading HS-code lookups. <br>
Mitigation: Check the bundled API reference for the exact hscode parameter format before running the query. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-analysis-hscode-detail-zh) <br>
- [HS code detail API reference](references/customs-analysis-hscode-detail-api.md) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON API results with concise natural-language guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires UPKUAJING_API_KEY; paid API calls should be confirmed before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
