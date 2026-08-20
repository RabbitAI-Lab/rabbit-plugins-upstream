## Description:

Scaffold a new .NET solution (Web API + Worker microservices) using ONION architecture and EF Core, codifying battle-tested layered patterns and explicitly avoiding the common pitfalls of legacy stored-procedure-centric codebases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scaffold or extend .NET Web API and worker-service solutions with Onion architecture, EF Core persistence, layered dependency rules, and reusable project templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or modify many project files during scaffolding.

Mitigation: Run it in a version-controlled workspace and review the planned target framework, package table, and generated file changes before accepting them.

Risk: The skill may contact public package or documentation sources to resolve current .NET and package versions.

Mitigation: Use only approved network sources in restricted environments, or provide pinned versions and documentation sources before scaffolding.

Risk: Generated .NET code can depend on the chosen target framework and package versions.

Mitigation: Require the generated solution to pass dotnet build and dotnet test, and review any package/version choices before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/dotnet-onion-api)
- [.NET support policy](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core)
- [Solution layout](references/solution-layout.md)
- [Anti-patterns](references/anti-patterns.md)
- [Application settings templates](references/templates/appsettings.md)
- [Base controller template](references/templates/base-controller.cs.md)
- [Project file templates](references/templates/csproj-files.md)
- [EF Core DbContext template](references/templates/dbcontext.cs.md)
- [Exception middleware template](references/templates/exception-middleware.cs.md)
- [Feature slice template](references/templates/feature-slice.md)
- [API Program.cs template](references/templates/program-cs.md)
- [Worker Program.cs template](references/templates/worker-program.cs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Files, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with code blocks, shell commands, and generated project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify multiple .NET solution files and should report build and test results after scaffolding.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
