## Description:

Use when starting a new .NET/Blazor/Angular MVP project in an empty repository.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to bootstrap a new MVP repository for .NET, Blazor, Angular, API, worker, or hybrid app projects after initial product specs are available. It guides stack selection, project structure, dependency setup, documentation, build checks, and local stubs for external services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to create repo-local agent configuration, hooks, rules, skills, dependency lockfiles, and git commits during MVP scaffolding.

Mitigation: Use it only in a new project intended for automated scaffolding, then review generated agent configuration, package versions, lockfiles, and commit behavior before further development.

Risk: Some required prompts and confirmations are written in Portuguese, which may be unclear to users who do not read Portuguese.

Mitigation: Ask the agent to repeat confirmations in the user's preferred language before approving stack choices or scaffold execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/scaffold-mvp)
- [Source repository URL from skill metadata](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command examples and generated repository files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create project files, documentation, agent configuration, dependency lockfiles, local service stubs, and an initial git commit when executed by an agent.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter metadata.version: 2.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
