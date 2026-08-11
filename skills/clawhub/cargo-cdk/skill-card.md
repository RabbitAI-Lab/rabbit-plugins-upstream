## Description:

Cargo CDK helps agents define Cargo workspace resources in TypeScript and deploy them declaratively with cargo-ai cdk for repeatable, version-controlled workspace management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when they want an agent to scaffold, author, plan, deploy, or maintain Cargo workspace resources as code instead of performing one-off Cargo CLI operations. It is suited to reproducible multi-resource workspace changes that should be reviewed, committed, and redeployed across environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deploy, prune, destroy, and CI --yes flows can make high-impact changes to managed Cargo workspace resources.

Mitigation: Confirm the selected workspace, review cargo-ai cdk plan output, and treat destroy --all as a managed-resource teardown command before execution.

Risk: Cargo API tokens and integration credentials are required for deployment workflows.

Mitigation: Keep API tokens and secret() environment variables in secret storage, and avoid committing token values or generated working files that may expose local state.

Risk: Losing or misusing cargo.state.json can orphan deployed plays, agents, or alerts or reconcile code against the wrong workspace.

Mitigation: Commit cargo.state.json for managed environments, preserve one state file per workspace, and use import or rollback workflows when recovering state.

## Reference(s):

- [ClawHub skill page: cargo-cdk](https://clawhub.ai/cargo-ai/skills/cargo-cdk)
- [Cargo skills repository homepage](https://github.com/getcargohq/cargo-skills)
- [Command reference: cargo-ai cdk](references/commands.md)
- [Resource reference](references/resources.md)
- [Deploy & state guide](guides/deploy-and-state.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with TypeScript examples, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include deployment plans, Cargo CDK project structure, TypeScript resource definitions, CI steps, and review guidance.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
