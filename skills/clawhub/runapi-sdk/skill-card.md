## Description:

Choose RunAPI SDK packages for application developers building web apps, backends, workers, or libraries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to choose and integrate RunAPI SDK packages for web apps, backends, workers, libraries, and production code. It helps distinguish SDK-based integrations from one-off RunAPI CLI usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys could be exposed if copied into source code or committed configuration.

Mitigation: Keep RunAPI API keys in environment variables or managed secret storage.

Risk: A selected SDK package or provider client may not match the application's current language, model, methods, response shape, or error handling needs.

Mitigation: Review the package README or source before adding dependencies, including install commands, client methods, response shape, and error classes.

Risk: Using the RunAPI CLI as a production integration layer can create brittle application behavior.

Mitigation: Use SDK packages for application, backend, worker, library, and production integrations; reserve the CLI for one-off generation tasks.

Risk: Generated file URLs may expire before the application stores needed assets.

Mitigation: Download and store generated images, videos, audio, or other files in durable storage within the documented temporary URL window.

## Reference(s):

- [RunAPI model and SDK package catalog](https://runapi.ai/models.md)
- [RunAPI models homepage](https://runapi.ai/models)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with package names, installation commands, configuration notes, and code-oriented integration advice]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Text guidance only; no executable code is bundled with the skill.]

## Skill Version(s):

0.2.8 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
