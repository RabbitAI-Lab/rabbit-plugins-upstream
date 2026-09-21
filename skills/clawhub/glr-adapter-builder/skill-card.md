## Description:

Builds or refactors GameLearningRuntime adapters, runtime bridges, trainable environments, knowledge research manifests, and reward configurations for authorized game runtimes while preserving privacy, provenance, action fencing, and learner-neutral contracts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scaffold or refactor GLR-compatible game runtime adapters, bridge contracts, training configuration, reward policy, and validation evidence for authorized runtimes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill guides command execution and generated file creation for GLR adapter projects.

Mitigation: Use it only for authorized GLR adapter development, review generated files before use, and avoid running package checks in untrusted repositories or with sensitive CI secrets.

Risk: Loader-plugin and external-attach lanes could be misapplied to runtimes that do not permit instrumentation.

Mitigation: Use loader or external lanes only with owned or explicitly authorized runtimes and verify that the runtime owner permits the integration path.

Risk: Adapter evidence and diagnostics can accidentally expose private runtime details if collected or published carelessly.

Mitigation: Publish only bounded review evidence and exclude credentials, local paths, process or window identifiers, machine bindings, private traces, and user-specific data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/loonghao/skills/glr-adapter-builder)
- [GLR downstream Python quality baseline](artifact/references/downstream-quality.md)
- [Downstream module boundaries](artifact/references/module-boundaries.md)
- [Deliver a trained stage to users](artifact/references/user-releases.md)
- [Framework upgrade and migration contract](artifact/references/framework-migration.md)
- [Multi-engine development boundaries](artifact/references/multi-engine.md)
- [Authorized loader-plugin integrations](artifact/references/loader-plugins.md)
- [Gameplay research and reward design](artifact/references/research-and-reward.md)
- [Runtime Host and provider SDK boundary](artifact/references/runtime-host.md)
- [Adapter diagnostics for the agent workbench](artifact/references/diagnostics.md)
- [Adapter validation gates](artifact/references/validation-gates.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with code blocks plus generated project files and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated scaffolds include validation gates, safety policy files, adapter templates, and review evidence guidance.]

## Skill Version(s):

0.22.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
