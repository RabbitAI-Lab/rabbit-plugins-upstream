## Description:

Manage a whole Cargo workspace as code: declare connectors, models, plays, tools, agents, MCP servers, segments, context, folders, files, workers, and apps in TypeScript, then reconcile them with `cargo-ai project`.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to manage Cargo workspaces as reproducible TypeScript infrastructure, including resource authoring, planning, deployment, drift handling, import, rollback, and CI deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses npm and npx tooling in workflows that can deploy, change, or tear down business infrastructure.

Mitigation: Pin the Cargo CLI and any skills CLI to reviewed versions, avoid ad-hoc unpinned npx execution in CI, and run `cargo-ai project plan` before deployment.

Risk: Workspace deployments can affect live resources, including destructive operations, paid scheduled workflows, mailboxes, and DNS-zone changes.

Mitigation: Use least-privilege Cargo and connector tokens, require explicit human approval for deploy, destroy, prune, mailbox, paid scheduled workflow, and DNS-zone changes, and review record counts or credit estimates before broad execution.

## Reference(s):

- [Cargo Skills Homepage](https://github.com/getcargohq/cargo-skills)
- [ClawHub Skill Page](https://clawhub.ai/cargo-ai/skills/cargo-project)
- [Authoring Resources](guides/authoring-resources.md)
- [Deploy and State](guides/deploy-and-state.md)
- [Typed Config](guides/typed-config.md)
- [Command Reference](references/commands.md)
- [Resource Reference](references/resources.md)
- [Troubleshooting](references/troubleshooting.md)
- [Cookbooks](references/cookbooks.md)
- [Full Workspace Example](references/examples/full-workspace.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with TypeScript and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Cargo CDK resource definitions, deployment plans, command sequences, and review guidance.]

## Skill Version(s):

2.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
