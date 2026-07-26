## Description: <br>
Zoodata gives agents a reference and command helper for ZooData commerce and keyword-intelligence APIs, including endpoint usage, parameters, authentication, credit tracking, and local review processing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agents use this skill to discover ZooData API endpoints, configure authentication, call commerce and keyword-intelligence workflows, and interpret returned fields and credit usage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: This release is flagged suspicious because it ships and may silently use a bundled ZooData credential and extra credential sources. <br>
Mitigation: Prefer a version that removes artifact/config.json, rotate the exposed key, and configure your own ZOODATA_API_KEY before use. <br>
Risk: ZooData API calls send user queries to ZooData and may consume account credits. <br>
Mitigation: Review requested queries before running workflows and monitor credit consumption in API metadata. <br>


## Reference(s): <br>
- [ZooData API Quick Reference](references/openapi-reference.md) <br>
- [Market Entry Analyzer API Field Reference](references/reference.md) <br>
- [Live OpenAPI Specification](https://zoodata.ai/api/v1/openapi-spec) <br>
- [ZooData API Documentation](https://api.zoodata.ai/api-docs) <br>
- [Metadata Homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ClawHub Skill Page](https://clawhub.ai/apiclaw/skills/apiclaw-core) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON request examples, and Python helper usage.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY; API calls send queries to ZooData and may consume credits.] <br>

## Skill Version(s): <br>
1.1.4 (source: evidence release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
