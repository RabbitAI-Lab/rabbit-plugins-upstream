## Description: <br>
Provides AI assistants with database access tools for listing tables, inspecting schemas, executing SQL, and generating query plans for SQLite, PostgreSQL, MySQL, and MariaDB. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI-agent users use this skill to inspect database structure, run SQL statements, and review query plans from an assistant workflow. It can return table lists, column details, query results, and explain output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security evidence flags the release as suspicious because the documented database purpose is mixed with an external API proxy and unrelated plaintext API-key handling. <br>
Mitigation: Confirm who operates the remote API, what database inputs and results are sent to it, and why XBY_GAOKAO/XBY_APIKEY configuration is required before using the skill. <br>
Risk: Database queries may expose production data or perform writes or DDL if write access is enabled. <br>
Mitigation: Use a read-only database account, avoid production data until the data flow is clear, and require explicit approval before writes or DDL are allowed. <br>
Risk: The skill can persist API keys in a project .env file as plaintext. <br>
Mitigation: Prefer environment-level secret management and do not store API keys in .env unless plaintext persistence is an accepted risk. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/cainingnk/skills/xby-db) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, guidance] <br>
**Output Format:** [Markdown summaries with JSON-like raw tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include raw upstream database or API response data.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
