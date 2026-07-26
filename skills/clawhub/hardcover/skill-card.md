## Description: <br>
Query Hardcover.app reading lists, reading progress, goals, and catalog data through its GraphQL API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[asaphko](https://clawhub.ai/user/asaphko) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to retrieve their Hardcover reading library, progress, goals, and catalog search results, or to prepare read-only reading data for sync to systems such as Obsidian. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Hardcover API token that can retrieve personal reading history, reviews, journals, and goals. <br>
Mitigation: Use only a token the user is comfortable giving to the agent, and review retrieved data before sharing or syncing it elsewhere. <br>
Risk: Hardcover API access is rate limited and tokens can expire. <br>
Mitigation: Keep requests within documented limits and refresh the token if authentication fails. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/asaphko/skills/hardcover) <br>
- [Hardcover.app](https://hardcover.app) <br>
- [Hardcover API token settings](https://hardcover.app/settings) <br>
- [Hardcover GraphQL endpoint](https://api.hardcover.app/v1/graphql) <br>
- [Hardcover Entity Reference](references/entities.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash and GraphQL code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires HARDCOVER_API_TOKEN for authenticated Hardcover API access.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
