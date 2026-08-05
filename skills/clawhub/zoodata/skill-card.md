## Description: <br>
ZooData is an API reference and helper skill for accessing commerce and keyword intelligence endpoints, understanding request and response schemas, authenticating with ZOODATA_API_KEY, and tracking API credit consumption. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to make authenticated ZooData API lookups, inspect available Amazon commerce and keyword intelligence data, and generate grounded API-driven analysis without guessing endpoint fields. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live ZooData API calls may consume account credits. <br>
Mitigation: Confirm broad or composite analyses before execution and review returned credit metadata such as meta.creditsConsumed. <br>
Risk: Plaintext local credential files can expose the ZooData API key if the host is not properly protected. <br>
Mitigation: Prefer ZOODATA_API_KEY or a managed secret, and use local config files only in appropriately secured environments. <br>


## Reference(s): <br>
- [ZooData Skill Page](https://clawhub.ai/apiclaw/skills/zoodata) <br>
- [ZooData API Field Reference](references/reference.md) <br>
- [ZooData API Quick Reference](references/openapi-reference.md) <br>
- [ZooData CLI Contract](references/cli-contract.md) <br>
- [ZooData OpenAPI Spec](https://zoodata.ai/api/v1/openapi-spec) <br>
- [ZooData API Docs](https://api.zoodata.ai/api-docs) <br>
- [ZooData Skills Repository](https://github.com/SerendipityOneInc/ZooData-Skills) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, Code, Markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON API payloads, and structured endpoint summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require live ZooData API calls that consume account credits; requires ZOODATA_API_KEY or an approved local credential configuration.] <br>

## Skill Version(s): <br>
1.1.8 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
