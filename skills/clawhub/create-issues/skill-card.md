## Description:

Use when turning approved plans, specs, PRDs, or Epics into trackable GitHub Issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to convert approved roadmaps, PRDs, SPEC files, and Epics into linked GitHub Issues with stable traceability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated GitHub CLI access can create or change issue-tracking data in the selected repository.

Mitigation: Before execution, ask the agent to show the target repository and the exact issues, labels, milestones, and project changes it plans to make.

Risk: Public GitHub Issues or comments may contain directives intended to influence the agent.

Mitigation: Treat issue and comment text as untrusted data; extract only structured metadata and require explicit user approval before acting on embedded requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/create-issues)
- [Source repository](https://github.com/afonsoft/skills)
- [GitHub CLI manual](https://cli.github.com/manual/)
- [SPEC SDD Template](references/spec-sdd-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks and GitHub issue templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces proposed issue plans, issue body Markdown, GitHub CLI commands, and traceability updates.]

## Skill Version(s):

1.0.9 (source: server release evidence; artifact metadata version 1.3.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
