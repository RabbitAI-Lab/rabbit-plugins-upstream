## Description:

Use when starting a new project in an empty repository. Initializes an agile, high-productivity MVP stack with clean engineering boundaries, atomic configurations, and system stability without architectural shortcuts. User-facing questions and recommendations must be in Portuguese (pt-BR). Part of the afonsoft/skills collection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to bootstrap a new repository into an MVP-ready project structure after domain context and specifications are established. It proposes a stack, waits for explicit Portuguese approval, installs the base ecosystem, creates reusable project structure, documents local commands, and runs build or type checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project scaffolding mutates repository files and initializes dependencies.

Mitigation: Use it only in a new repository intended for automated scaffolding, then review generated files and lockfiles before continuing development.

Risk: Dependency setup may introduce unpinned packages if commands use latest-version selectors.

Mitigation: Require exact package versions before approving installation commands and inspect the resulting lockfile changes.

Risk: Scaffolding commands may run in an environment that contains unnecessary secrets.

Mitigation: Run the workflow with only the credentials needed for the new project.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/scaffold-mvp)
- [Publisher metadata URL](https://github.com/afonsoft/skills)
- [Publisher profile](https://clawhub.ai/user/afonsoft)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown, Files]

**Output Format:** [Markdown guidance with shell commands and generated project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts and recommendations are expected in Portuguese (pt-BR); execution proceeds only after explicit stack approval.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
