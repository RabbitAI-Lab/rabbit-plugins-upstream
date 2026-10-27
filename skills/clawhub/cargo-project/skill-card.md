## Description:

Helps developers declare Cargo resources in TypeScript projects and review, deploy, and maintain them as version-controlled infrastructure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to define Cargo connectors, models, agents, and other workspace resources as code, review planned changes, and deploy repeatably across environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deploying to the wrong workspace or accepting an unexpected project plan can change live resources.

Mitigation: Confirm the active workspace and review the project plan before deploying.

Risk: Pruning or destroying a project can delete managed resources.

Mitigation: Inspect the planned deletions and explicitly approve deploy --prune or destroy --all only when intended.

Risk: Exposed CI credentials or unpinned dependencies can compromise or unpredictably change deployments.

Mitigation: Store CI tokens as secrets and pin npm package versions where reproducibility matters.

## Reference(s):

- [Cargo project homepage (listed in release metadata)](https://github.com/getcargohq/cargo-skills)
- [Cargo project commands](artifact/references/commands.md)
- [Deploy and state guide](artifact/guides/deploy-and-state.md)
- [Cargo project skill on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-project)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Shell commands, Guidance]

**Output Format:** [Markdown with TypeScript, JSON, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project plans should be reviewed before deployment.]

## Skill Version(s):

4.0.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
