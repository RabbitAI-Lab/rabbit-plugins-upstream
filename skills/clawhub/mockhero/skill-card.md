## Description: <br>
Generate realistic synthetic test data - relational JSON/CSV/SQL fixtures, seed data, and QA datasets - via the MockHero MCP server or REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dinosaur24](https://clawhub.ai/user/dinosaur24) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and QA engineers use MockHero to generate realistic seed data, fixtures, and multi-table datasets with valid foreign keys for tests, demos, and application development. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Schemas, prompts, SQL, sample JSON, and billing email may be shared with MockHero during use. <br>
Mitigation: Avoid submitting sensitive production data and review inputs before sending them to the service. <br>
Risk: Generated data requests may incur metered usage after the free preview. <br>
Mitigation: Use the estimate tool or free preview before paid generation and confirm checkout before continuing. <br>
Risk: MockHero creates synthetic data and does not provide de-identification guarantees for real production data. <br>
Mitigation: Do not use the skill to anonymize or mask production datasets. <br>
Risk: MockHero API keys grant access to paid or authenticated generation. <br>
Mitigation: Keep mh_ API keys private and pass them only through supported secure configuration or authorization mechanisms. <br>


## Reference(s): <br>
- [MockHero homepage](https://mockhero.dev) <br>
- [MockHero MCP endpoint](https://mockhero.dev/mcp/agent) <br>
- [ClawHub skill page](https://clawhub.ai/dinosaur24/skills/mockhero) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON, CSV, SQL, REST, and MCP examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can guide agents to produce synthetic data requests and receive JSON, CSV, or SQL outputs from MockHero.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
