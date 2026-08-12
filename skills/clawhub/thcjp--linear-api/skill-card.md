## Description:

Helps agents draft GraphQL queries, mutations, and workflow guidance for managing project issues, projects, cycles, labels, comments, relations, and status transitions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineering teams, and workflow automation users use this skill to prepare project-management API operations for issue CRUD, project and cycle planning, labels, comments, relations, custom views, and workflow status changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad external API mutations that modify project-management data.

Mitigation: Use a narrowly scoped API key and review GraphQL mutations before execution, especially create, update, archive, relation, and state-transition operations.

Risk: Callback URLs may expose project data to an external destination.

Mitigation: Only provide trusted callback URLs and omit callback configuration when asynchronous notifications are not required.

Risk: Broad task-planning prompts may lead to unintended API actions.

Mitigation: Require explicit confirmation before executing API-changing operations and keep prompts scoped to the intended team, project, and workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/linear-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with GraphQL examples, JSON response examples, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API key configuration guidance, GraphQL request examples, error recovery steps, and security reminders.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
