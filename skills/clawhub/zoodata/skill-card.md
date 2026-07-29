## Description: <br>
ZooData is an API reference skill for commerce and keyword-intelligence endpoints, including authentication, request parameters, response fields, credit reporting, and local review-analysis tooling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to understand and call ZooData commerce and keyword-intelligence APIs, including endpoint selection, parameter rules, field schemas, authentication, credit usage, and review-analysis workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a reusable ZooData API key and may read it from the environment or ~/.zoodata/config.json. <br>
Mitigation: Prefer ZOODATA_API_KEY as an environment variable; if a config file is used, restrict file permissions. <br>
Risk: Broad or composite ZooData workflows can make many API calls and consume account credits. <br>
Mitigation: Estimate credit use and confirm broad scans before running multi-call workflows. <br>
Risk: Sending credentials to an untrusted API base URL could expose the bearer token. <br>
Mitigation: Use the documented ZooData host allowlist behavior and avoid overriding the base URL except for trusted ZooData or local endpoints. <br>


## Reference(s): <br>
- [ZooData Skill Page](https://clawhub.ai/apiclaw/skills/zoodata) <br>
- [ZooData API Quick Reference](references/openapi-reference.md) <br>
- [ZooData Field Reference](references/reference.md) <br>
- [ZooData API Docs](https://api.zoodata.ai/api-docs) <br>
- [ZooData OpenAPI Spec](https://zoodata.ai/api/v1/openapi-spec) <br>
- [ZooData Skills Homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls, markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands, API examples, and field-reference tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY; broad API workflows may consume account credits.] <br>

## Skill Version(s): <br>
1.1.6 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
