## Description:

Helps agents manage project-management work items, projects, teams, cycles, labels, comments, relations, and views through GraphQL queries and mutations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, project operators, and automation builders use this skill to draft GraphQL queries and mutations for project-management workflows, including issue creation, updates, cycle planning, labels, comments, relations, and views. It is not intended for personnel performance evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide mutations to external project-management data, including issue, project, label, cycle, view, and comment changes.

Mitigation: Require explicit confirmation before mutations, deletes, archives, or state transitions, and restrict use to accounts where automated work-data changes are acceptable.

Risk: The skill asks for broad command and file authority through read, write, and exec tool access.

Mitigation: Run it in a least-privilege workspace and review proposed commands or file writes before execution.

Risk: API credentials could expose project-management data or allow unintended changes if over-scoped.

Mitigation: Use a least-privilege API key, store it in environment variables, and avoid sharing it with unrelated projects or sessions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/linear-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with GraphQL snippets and shell environment commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API-key setup guidance, GraphQL query or mutation examples, and operational cautions for project-management changes.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
