## Description: <br>
Find alumni and former colleagues in UpKuaJing's global company database using person and school identifiers for recruiting, sales, and B2B network research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, sales teams, and B2B lead generation specialists use this skill to look up alumni relationships from UpKuaJing people-data records. It can return paginated alumni identifiers for a specified person and school after the user supplies required identifiers and confirms paid API use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The advertised company/person alumni scope does not cleanly match the artifact behavior, which performs person-and-school alumni lookup. <br>
Mitigation: Use the skill only for documented person and school identifier lookups until the publisher narrows the manifest, triggers, and public description. <br>
Risk: Queries send people-data identifiers to UpKuaJing's paid API and can incur a fee for each page of results. <br>
Mitigation: Confirm the data-sharing purpose and obtain explicit user approval before each paid query or paginated follow-up call. <br>
Risk: The skill stores and reads an API key from a persistent local file under the user's home directory. <br>
Mitigation: Limit file permissions, avoid sharing the credential file, rotate exposed keys, and prefer environment-managed secrets where possible. <br>
Risk: The security verdict is suspicious because the people-data lookup scope, credential handling, and paid top-up flows require extra review. <br>
Mitigation: Review the skill, API terms, privacy obligations, and billing workflow before installation or operational use. <br>


## Reference(s): <br>
- [Alumni List API Reference](references/person-alumni-list-api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/global-company-person-alumni) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Developer Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON API responses with fee information plus concise Markdown guidance and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; API calls may incur per-page fees and require explicit user confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
