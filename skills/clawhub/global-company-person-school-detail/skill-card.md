## Description: <br>
Retrieves detailed school records, including institution type, geographic location, websites, and social media links, from UpKuaJing's global institutional data API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, researchers, analysts, and developers use this skill to verify educational institutions, enrich institutional records, and inspect academic network data for a known school ID. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid API lookups and top-up actions can incur charges. <br>
Mitigation: Tell users charges apply and wait for explicit confirmation before running fee-bearing lookup or payment-order commands. <br>
Risk: The skill stores and reads an UpKuaJing API key in ~/.upkuajing/.env. <br>
Mitigation: Protect the local API key file, avoid exposing the key in responses or logs, and remove it when it is no longer needed. <br>
Risk: Lookups send school identifiers and requests to UpKuaJing's outbound API. <br>
Mitigation: Use the skill only when the user is comfortable making outbound requests to UpKuaJing for the requested lookup. <br>
Risk: Institutional records may be incomplete, stale, or unsuitable as the sole basis for consequential decisions. <br>
Mitigation: Verify important school details against authoritative institutional sources before using results for hiring, degree verification, or compliance decisions. <br>


## Reference(s): <br>
- [School Detail API Reference](references/school-detail-api.md) <br>
- [ClawHub Skill Listing](https://clawhub.ai/upkuajing/skills/global-company-person-school-detail) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Developer Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires UPKUAJING_API_KEY; paid API calls return a single school-detail response for a supplied school ID.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
