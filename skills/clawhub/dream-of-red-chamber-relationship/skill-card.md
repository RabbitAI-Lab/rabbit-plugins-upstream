## Description: <br>
关于《红楼梦》人物之间关系的知识图谱。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to inspect and query a hosted knowledge graph of character relationships from Dream of the Red Chamber. It can retrieve graph schema information and execute read-only Cypher queries, then present the returned results to the user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security summary says the skill asks for an API key in chat and saves it in a plaintext .env file. <br>
Mitigation: Install only if you trust the XiaoBenYang service, configure the key through a platform secret store where possible, and avoid sharing sensitive credentials in chat. <br>
Risk: The server security summary notes unrelated gaokao project remnants that may make the skill purpose and provider unclear. <br>
Mitigation: Review the artifact before deployment and wait for the publisher to remove unrelated remnants or clarify the backend/provider when provenance clarity is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/dream-of-red-chamber-relationship) <br>
- [XiaoBenYang service](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, API Calls, Guidance] <br>
**Output Format:** [Markdown summaries with JSON-backed graph query results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a configured XiaoBenYang API key before tool calls can succeed.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
