## Description:

Builds or refactors authorized GameLearningRuntime adapters, runtime bridges, trainable environments, research manifests, and reward configurations while preserving privacy and action boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scaffold and validate game-runtime adapters for reinforcement learning, behavior cloning, evaluation, and offline collection within an authorized runtime boundary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scaffolding and validation create project files and may run dependency installation, builds, tests, and synthetic training.

Mitigation: Use only in authorized GLR projects; review generated changes and run package checks in a clean workspace without sensitive environment variables.

Risk: Loader plugins and external runtime bridges can interact with a game or runtime outside the synthetic test boundary.

Mitigation: Use these lanes only with game or runtime owner permission and verify exact target binding before acting.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/loonghao/skills/glr-adapter-builder)
- [Adapter validation gates](artifact/references/validation-gates.md)
- [Runtime Host provider boundary](artifact/references/runtime-host.md)
- [Research and reward guidance](artifact/references/research-and-reward.md)

## Skill Output:

**Output Type(s):** [Code, Configuration, Markdown guidance, Shell commands]

**Output Format:** [Project files and Markdown instructions with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Synthetic conformance and reproduction artifacts require separate authorized runtime validation.]

## Skill Version(s):

0.25.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
