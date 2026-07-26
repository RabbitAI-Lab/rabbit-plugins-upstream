## Description: <br>
Retrieves detailed LinkedIn school information, including names, types, locations, websites, and social links, to help recruiters, researchers, and analysts verify institutions and enrich academic network data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, recruiters, researchers, and analysts use this skill to look up a known LinkedIn school ID and retrieve institution details for degree verification, institutional research, and academic network enrichment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses UpKuaJing as the data provider and API calls may incur fees. <br>
Mitigation: Confirm the paid-call workflow and review current pricing before approving lookups or top-up flows. <br>
Risk: The API key may be stored in a local plaintext ~/.upkuajing/.env file. <br>
Mitigation: Protect the local credential file, avoid sharing it, and rotate the key if exposure is suspected. <br>
Risk: Payment URLs and top-up flows can affect account balance. <br>
Mitigation: Review payment URLs carefully and require explicit user confirmation before creating or acting on top-up orders. <br>


## Reference(s): <br>
- [LinkedIn School Detail API Reference](references/linkedin-school-detail-api.md) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/linkedin-person-school-detail) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [JSON responses with concise Markdown guidance and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a school ID and a configured UPKUAJING_API_KEY; each lookup may incur a fee.] <br>

## Skill Version(s): <br>
1.0.4 (source: evidence release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
