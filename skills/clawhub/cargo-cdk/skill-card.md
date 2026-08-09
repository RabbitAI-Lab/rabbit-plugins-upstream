## Description:

Cargo CDK helps agents define Cargo workspaces as TypeScript code and manage the lifecycle with `cargo-ai cdk` planning, typing, deployment, import, drift, rollback, and teardown commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to manage Cargo resources as a reproducible, version-controlled workspace definition instead of performing one-off imperative operations. It supports scaffolding, authoring, planning, deploying, importing, and troubleshooting Cargo workspace resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deploy, prune, destroy, and CI commands with `--yes` can change or remove Cargo workspace resources.

Mitigation: Confirm the selected Cargo workspace, review the plan and state before execution, and treat `destroy --all` as a full teardown of CDK-managed resources.

Risk: Cargo API tokens and environment secrets can grant access to workspace or external service data.

Mitigation: Protect API tokens and secret environment variables, use `secret()` for credentials, and avoid exposing secret values in source, logs, or state files.

Risk: Missing, stale, or uncommitted `cargo.state.json` can orphan resources or make deployments target the wrong workspace state.

Mitigation: Commit and protect `cargo.state.json`, use separate state per workspace, and use plan, refresh, or import before reconciling existing resources.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cargo-ai/skills/cargo-cdk)
- [Cargo Publisher Profile](https://clawhub.ai/user/cargo-ai)
- [Cargo Skills Homepage](https://github.com/getcargohq/cargo-skills)
- [Authoring Resources](guides/authoring-resources.md)
- [Deploy & State](guides/deploy-and-state.md)
- [Typed Config](guides/typed-config.md)
- [Command Reference](references/commands.md)
- [Resource Reference](references/resources.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with TypeScript and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Cargo CLI commands, workspace-as-code configuration snippets, and operational review guidance.]

## Skill Version(s):

1.1.0 (source: frontmatter, release evidence, skill-metadata.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
