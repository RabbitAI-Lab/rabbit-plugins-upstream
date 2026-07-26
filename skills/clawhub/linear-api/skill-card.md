## Description: <br>
Linear API integration with managed OAuth for querying and managing issues, projects, teams, cycles, labels, and comments using GraphQL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use this skill to query Linear work, inspect project status, and manage issues, comments, projects, teams, cycles, and labels through Maton-backed GraphQL access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help perform write operations against Linear resources, including create, update, delete, and comment actions. <br>
Mitigation: Confirm the connected account, target resource, and intended effect with the user before any write operation runs. <br>
Risk: MATON_API_KEY provides access through Maton to the user's connected Linear account. <br>
Mitigation: Store the key in environment configuration, avoid printing it in shared terminals or logs, and rotate it if exposure is suspected. <br>
Risk: When multiple Linear connections exist, requests may affect the wrong workspace or account if no connection is specified. <br>
Mitigation: Specify the intended Maton connection ID for account-sensitive actions and verify it before executing changes. <br>


## Reference(s): <br>
- [ClawHub Linear skill page](https://clawhub.ai/byungkyu/skills/linear-api) <br>
- [Linear API overview](https://linear.app/developers) <br>
- [Linear GraphQL getting started](https://linear.app/developers/graphql) <br>
- [Linear GraphQL schema reference](https://studio.apollographql.com/public/Linear-API/schema/reference?variant=current) <br>
- [Maton CLI manual](https://cli.maton.ai/manual) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell, GraphQL, JSON, Python, and JavaScript examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and explicit user approval before create, update, delete, or comment actions.] <br>

## Skill Version(s): <br>
1.0.6 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
