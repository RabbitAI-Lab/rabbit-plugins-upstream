## Description:

Automates Jira-style project management workflows for epics, stories, bugs, subtasks, sprints, boards, issue links, status transitions, JQL search, and user and project lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and project teams use this skill to create, search, link, and transition Jira-style work items and to manage sprint and board workflows through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or modify real project-management work items.

Mitigation: Use Jira tokens scoped to the minimum required projects and review proposed create, link, sprint, and transition actions before execution.

Risk: The declared local command and file-search capabilities are broader than the Jira workflow.

Mitigation: Run the skill in an agent environment where command execution and local file access can be restricted or reviewed.

Risk: API tokens and callback URLs may expose sensitive project data if misconfigured.

Mitigation: Store tokens outside version control, rotate them regularly, and allow callbacks only to trusted destinations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/jira)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration guidance]

**Output Format:** [Markdown responses with JSON examples and inline command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task status, parsed summaries, work item data, error codes, and remediation guidance.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
