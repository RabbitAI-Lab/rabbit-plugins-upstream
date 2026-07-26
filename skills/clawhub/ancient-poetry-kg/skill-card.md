## Description: <br>
围绕中国古代诗词名称，作者，朝代，经典词句的知识图谱。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to query an ancient Chinese poetry knowledge graph for poem titles, authors, dynasties, classic lines, schema information, and read-only Cypher results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an API key and stores it in a local .env file. <br>
Mitigation: Use only trusted workspaces, keep .env out of source control, and rotate the key if it may have been exposed. <br>
Risk: The skill permits broad read-only Cypher queries against the graph service. <br>
Mitigation: Review Cypher queries before execution and avoid sending sensitive or unrelated query content to the external service. <br>
Risk: The security evidence flags stale high-school-project references that do not fully match the poetry description. <br>
Mitigation: Confirm the queried schema and returned data match the ancient-poetry use case before relying on results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/ancient-poetry-kg) <br>
- [XiaoBenYang API key service](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, configuration guidance] <br>
**Output Format:** [Markdown summary of JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided XBY_APIKEY and may return graph schema data or read-only Cypher query results.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
