## Description:

Build or refactor a GameLearningRuntime adapter, runtime bridge, trainable environment, research manifest, or reward configuration for an authorized game runtime.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scaffold and validate learner-neutral GLR adapters and training environments for authorized game runtimes, with bounded actions and reproducible evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated setup, tests, or wheel checks may execute project code in a sensitive environment.

Mitigation: Run only in trusted projects and a clean shell or sandbox without cloud tokens, CI secrets, private game credentials, or broad filesystem access.

Risk: A generated loader could affect a real game runtime without appropriate authorization.

Mitigation: Require explicit operator approval before packaging or installing a loader into a real game target.

## Reference(s):

- [GLR Adapter Builder release](https://clawhub.ai/loonghao/skills/glr-adapter-builder)
- [Adapter validation gates](artifact/references/validation-gates.md)
- [Runtime host boundary](artifact/references/runtime-host.md)
- [Authorized loader-plugin integrations](artifact/references/loader-plugins.md)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Shell commands, Guidance]

**Output Format:** [Markdown guidance and commands, with generated Python code and TOML/JSON configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Synthetic checks and reproduction evidence do not establish live-game acceptance or model quality.]

## Skill Version(s):

0.24.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
