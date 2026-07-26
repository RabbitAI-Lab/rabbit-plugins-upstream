## Description: <br>
Admapix Free is a thin AdMapix API client for creative search, app detail lookup, and store ranking queries that returns raw structured JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and marketing analysts use this skill to query AdMapix for advertising creatives, application details, and store rankings through an agent that prepares API calls and returns the raw JSON response for downstream analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AdMapix queries and related business search criteria are sent to api.admapix.com. <br>
Mitigation: Use the skill only when that data sharing is acceptable, and review generated requests before running them when prompts include sensitive strategy or customer information. <br>
Risk: The skill requires an AdMapix API key for X-API-Key authentication. <br>
Mitigation: Keep the key in the ADMAPIX_API_KEY environment variable, do not paste it into chat, and do not print or expose the key in command output. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/admapix-free) <br>
- [Publisher Profile](https://clawhub.ai/user/thcjp) <br>
- [Skill Homepage](https://skillhub.cn) <br>
- [AdMapix Website](https://www.admapix.com) <br>
- [AdMapix API Endpoint](https://api.admapix.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, json, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and raw JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ADMAPIX_API_KEY and network access to api.admapix.com; creative search page_size is capped at 10.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
