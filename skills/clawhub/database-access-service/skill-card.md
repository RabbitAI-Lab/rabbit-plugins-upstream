## Description: <br>
Provides database table listing, schema lookup, and SQL query execution through a remote service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect database tables, retrieve table schemas, and run SQL queries through the XiaoBenYang MCP service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can execute arbitrary SQL against the connected database service. <br>
Mitigation: Use least-privilege, read-only credentials when possible and review SQL before execution. <br>
Risk: The skill stores an API key locally in a .env file. <br>
Mitigation: Use a scoped API key, protect the workspace, and rotate the key if the environment is shared or exposed. <br>
Risk: The skill depends on a remote third-party service for database access. <br>
Mitigation: Install only when the XiaoBenYang MCP service and the publisher are trusted for the target database. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/database-access-service) <br>
- [XiaoBenYang service](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown summary of JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an API key and may return raw database query results.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
