## Description:

Build or refactor a GameLearningRuntime adapter, runtime bridge, trainable environment, knowledge research manifest, or reward configuration for an authorized game runtime.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scaffold or refactor authorized game adapters and trainable environments, with synthetic conformance checks, bounded runtime integration, and documented research and reward configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated build, test, or training commands can execute code in the target project.

Mitigation: Use trusted repositories and keep secrets out of the environment when running generated validation scripts.

Risk: Live game, loader, recorder, or installer workflows can affect a real runtime or machine.

Mitigation: Require explicit approval and an authorized runtime boundary before using these workflows.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/loonghao/skills/glr-adapter-builder)
- [Runtime host integration](artifact/references/runtime-host.md)
- [Validation gates](artifact/references/validation-gates.md)
- [Research and reward configuration](artifact/references/research-and-reward.md)

## Skill Output:

**Output Type(s):** [Code, Configuration, Shell commands, Guidance]

**Output Format:** [Markdown guidance, Python code, TOML/JSON configuration, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a synthetic adapter scaffold and validation artifacts; live integration requires separate authorized verification.]

## Skill Version(s):

0.23.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
