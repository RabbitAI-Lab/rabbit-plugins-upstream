## Description:

Defines Cargo workspaces as TypeScript code and guides agents through reproducible init, typing, planning, deployment, drift, import, rollback, and teardown workflows with `cargo-ai cdk`.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, review, and deploy Cargo workspace resource graphs as reproducible TypeScript CDK projects rather than one-off CLI changes. It is suited for version-controlled setup of connectors, models, agents, tools, workflows, hosted apps, and related workspace resources across environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CDK deploy, prune, destroy, and CI `--yes` flows can intentionally make high-impact changes to Cargo workspace resources.

Mitigation: Review `cargo-ai cdk plan` output, confirm the selected workspace with `cargo-ai whoami`, and require deliberate approval before `deploy`, `deploy --prune`, `destroy --all`, or non-interactive CI deploys.

Risk: Losing or failing to commit `cargo.state.json` can orphan deployed resources that do not have stable slugs.

Mitigation: Commit `cargo.state.json` after deployments and use `cargo-ai cdk import <id> <uuid>` to rebind existing live resources when state must be recovered.

Risk: Connector credentials and workspace API tokens are required for common deploy and CI workflows.

Mitigation: Store token values and `secret()` environment variables only in local or CI secrets, keep them out of source files and state, and confirm required variables are present before deploy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo-cdk)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Cargo CDK entrypoint](SKILL.md)
- [Authoring resources](guides/authoring-resources.md)
- [Deploy & state](guides/deploy-and-state.md)
- [Typed config](guides/typed-config.md)
- [Command reference](references/commands.md)
- [Resource reference](references/resources.md)
- [Troubleshooting](references/troubleshooting.md)
- [Full workspace example](references/examples/full-workspace.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with TypeScript examples, JSON snippets, and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Cargo CDK commands that create, update, prune, or destroy workspace resources; review plan output and selected workspace before execution.]

## Skill Version(s):

1.2.1 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
