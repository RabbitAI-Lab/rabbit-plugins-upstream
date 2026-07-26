## Description: <br>
Contentful GraphQL helps agents search and read Contentful data through the OOMOL Contentful GraphQL connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, content operators, and agents use this skill to inspect the OOMOL connector schema and run Contentful GraphQL Content API queries against a connected Contentful space and environment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queries and results pass through the OOMOL connector and the connected Contentful account. <br>
Mitigation: Install and use the skill only when the OOMOL integration is trusted, and review query payloads before execution. <br>
Risk: First-time CLI, authentication, connection, or billing steps can affect the user's OOMOL account setup. <br>
Mitigation: Run setup and connection commands only after a matching command failure, not proactively. <br>
Risk: GraphQL queries may return sensitive Contentful content from a selected space or environment. <br>
Mitigation: Request only the needed fields and review returned data before sharing or reusing it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-contentful-graphql) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Contentful](https://www.contentful.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill checks the live connector schema before constructing JSON payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
