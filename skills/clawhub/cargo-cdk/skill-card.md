## Description:

Cargo CDK helps agents define a Cargo workspace as TypeScript infrastructure-as-code and reconcile connectors, models, plays, tools, agents, MCP servers, files, workers, apps, and related resources with cargo-ai cdk commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scaffold, type-check, plan, deploy, update, import, and tear down Cargo workspaces from version-controlled TypeScript definitions. It is most useful when Cargo resources need to be reviewable, repeatable across environments, and committed with state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable npm or npx installs can change the CLI or CDK behavior used by the workflow.

Mitigation: Prefer pinned Cargo package versions and lockfiles, and install packages only from trusted Cargo sources.

Risk: CDK deploy, prune, destroy, and CI workflows can create, update, or delete live workspace resources.

Mitigation: Review cargo-ai cdk plan output before deploys, avoid casual use of --prune or destroy --all, and gate CI deploys to protected branches.

Risk: Workspace tokens and connector credentials are required for non-interactive deploys and integrations.

Mitigation: Keep CI tokens and connector credentials narrowly scoped to the intended workspace and provide secrets through environment variables.

Risk: Deployed plays, alerts, mailboxes, and paid provider nodes can introduce recurring or broad-scope costs.

Mitigation: Run small samples, preview alert thresholds, review record counts and credit estimates, and require approval before wide enrollment or recurring schedules.

## Reference(s):

- [Cargo Skills Repository](https://github.com/getcargohq/cargo-skills)
- [Command reference](references/commands.md)
- [Resource reference](references/resources.md)
- [Troubleshooting](references/troubleshooting.md)
- [Cookbooks](references/cookbooks.md)
- [Full workspace example](references/examples/full-workspace.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with TypeScript, JSON, YAML, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Cargo CDK project files, command sequences, deployment plans, and CI configuration for human review before execution.]

## Skill Version(s):

1.2.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
