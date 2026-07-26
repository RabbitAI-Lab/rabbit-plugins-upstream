## Description: <br>
Provides agent-callable queries for UK police crime, police force, neighbourhood, outcome, and stop-and-search data through a third-party API gateway. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to have an agent retrieve and summarize UK police data for crime, force, neighbourhood, outcome, and stop-and-search queries when a valid XiaoBenYang API key is configured. <br>

### Deployment Geography for Use: <br>
Global, for queries about United Kingdom police data <br>

## Known Risks and Mitigations: <br>
Risk: Police-data queries and the API key are sent to a third-party gateway. <br>
Mitigation: Install only when the user trusts xiaobenyang.com with those queries and credentials, and avoid submitting sensitive investigative context. <br>
Risk: The skill persists the API key in a local .env file. <br>
Mitigation: Treat the .env file as a stored secret, restrict access to it, and remove the key when it is no longer needed. <br>
Risk: Copied or inconsistent gaokao/school project references may confuse review and maintenance. <br>
Mitigation: Review the package metadata and clean inconsistent references before broad deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/uk-police-data-query) <br>
- [Publisher profile](https://clawhub.ai/user/alinklab) <br>
- [XiaoBenYang API key service](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP gateway](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown summaries with JSON-like raw API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided API key and returns upstream police-data query results.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
