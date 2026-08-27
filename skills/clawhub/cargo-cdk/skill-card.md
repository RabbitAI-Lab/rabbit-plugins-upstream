## Description:

Cargo CDK helps developers define Cargo workspace resources in TypeScript and reconcile them with Cargo using the cargo-ai cdk lifecycle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to manage Cargo workspaces as code: scaffold CDK projects, declare resources, preview plans, deploy changes, manage state, migrate live resources, and configure CI deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deploy, prune, and destroy workflows can create, update, release, or delete live Cargo resources managed by state.

Mitigation: Run cargo-ai cdk plan before deploy, prune, or destroy; confirm the selected workspace; and treat destroy --all as deleting all state-managed resources in that workspace.

Risk: CI/API tokens and connector credentials are needed for non-interactive deploys and resource configuration.

Mitigation: Store API tokens and secret() environment variables as secrets, keep credentials out of source and state, and gate deploys to protected branches after plan review.

Risk: Losing or failing to commit cargo.state.json can orphan uuid-only resources such as plays, agents, alerts, segments, capacity, or territory resources.

Mitigation: Commit cargo.state.json after deploys and use cargo-ai cdk import to rebind existing live resources when adopting or recovering state.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cargo-ai/skills/cargo-cdk)
- [Cargo Skills Homepage](https://github.com/getcargohq/cargo-skills)
- [Command reference](references/commands.md)
- [Resource reference](references/resources.md)
- [Troubleshooting](references/troubleshooting.md)
- [Cookbooks](references/cookbooks.md)
- [Full workspace example](references/examples/full-workspace.md)
- [GTM Skills Cookbooks](https://github.com/getcargohq/gtm-skills)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with TypeScript examples, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Cargo CDK resource definitions, deployment plans, state-management guidance, and CI configuration guidance.]

## Skill Version(s):

1.2.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
