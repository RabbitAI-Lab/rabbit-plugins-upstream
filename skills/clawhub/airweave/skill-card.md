## Description: <br>
Airweave lets agents search configured Airweave collections to retrieve workspace context from connected applications using semantic, keyword, or agentic search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lennertjansen](https://clawhub.ai/user/lennertjansen) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to let an agent answer questions and complete tasks with context retrieved from connected workspace applications indexed in Airweave. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an Airweave API key and collection identifier to retrieve workspace context. <br>
Mitigation: Use a least-privilege API key and limit the configured collection to data the agent is allowed to access. <br>
Risk: A custom AIRWEAVE_BASE_URL can send requests to a non-default endpoint. <br>
Mitigation: Set AIRWEAVE_BASE_URL only for trusted endpoints. <br>
Risk: Search results may include sensitive workplace content from connected applications. <br>
Mitigation: Handle retrieved content according to the organization's privacy and data-handling rules. <br>


## Reference(s): <br>
- [Airweave skill page](https://clawhub.ai/lennertjansen/skills/airweave) <br>
- [Airweave Search Parameters](references/PARAMETERS.md) <br>
- [Airweave Search Examples](references/EXAMPLES.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown search answers with sources, optional raw JSON, and shell commands for running searches] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AIRWEAVE_API_KEY and AIRWEAVE_COLLECTION_ID; AIRWEAVE_BASE_URL is optional for trusted non-default endpoints.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
