## Description: <br>
This skill helps agents query UpKuajing's global company database for a person's work-history timeline by person ID, including company names, job titles, tenure dates, current status, and summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, HR teams, sales teams, and hiring managers can use this skill to retrieve a target person's employment history from a global company database, enrich B2B contact profiles, and review career trajectory. The skill requires a person ID from a compatible search workflow and can optionally filter results by company ID. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and write a local UPKUAJING API key and can request a new key. <br>
Mitigation: Prefer supplying the API key through a managed secret mechanism, protect the local key file, and review prompts before allowing key-generation actions. <br>
Risk: The skill contacts openapi.upkuajing.com and can make paid API calls, including account and recharge actions. <br>
Mitigation: Confirm the user understands the cost before each paid operation, use the pricing query or pricing page for current pricing, and require explicit separate confirmation before execution. <br>
Risk: The security evidence reports account, credential, recharge, and automatic version-check behavior that users should review carefully. <br>
Mitigation: Review the credential, recharge, and version-check behavior before installation or execution, and run the skill only in an environment where those outbound actions are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/global-company-person-experience-zh) <br>
- [UpKuajing homepage](https://www.upkuajing.com) <br>
- [UpKuajing developer portal](https://developer.upkuajing.com/) <br>
- [Person experience list API reference](references/person-experience-list-api.md) <br>
- [UpKuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; API calls may incur per-request fees and can return paginated results.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
