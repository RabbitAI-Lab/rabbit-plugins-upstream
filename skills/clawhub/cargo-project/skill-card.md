## Description:

Manage Cargo workspaces as TypeScript projects by declaring connectors, models, agents, tools, apps, and other resources, then planning and deploying them with `cargo-ai project`.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform engineers use this skill to define a Cargo workspace as code, review planned changes, deploy from local development or CI, and manage deploy state across environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary flags mutable unpinned package installs while the skill guides workspace-changing deployments with credentials.

Mitigation: Pin reviewed CLI and skill versions, avoid unpinned `npx` in CI, and expose Cargo or connector secrets only to the minimum deployment step with scoped tokens.

Risk: Deployment, destroy, prune, and state commands can change or remove live Cargo workspace resources.

Mitigation: Review `cargo-ai project plan` output before applying changes, require explicit approval for destructive commands, and confirm the selected workspace before deploy or destroy.

Risk: Lost or incorrect deploy state can orphan deployed resources or reconcile code against the wrong workspace.

Mitigation: Commit the `cargo.state.json` pointer, keep one state per repo and environment, and use state bind or import workflows to recover links rather than creating replacement state silently.

## Reference(s):

- [Cargo Project Skill Release](https://clawhub.ai/cargo-ai/skills/cargo-project)
- [Cargo Skills Homepage](https://github.com/getcargohq/cargo-skills)
- [Authoring resources](artifact/guides/authoring-resources.md)
- [Deploy & state](artifact/guides/deploy-and-state.md)
- [Typed config](artifact/guides/typed-config.md)
- [Command reference](artifact/references/commands.md)
- [Resource reference](artifact/references/resources.md)
- [Troubleshooting](artifact/references/troubleshooting.md)
- [Cookbooks](artifact/references/cookbooks.md)
- [Full workspace example](artifact/references/examples/full-workspace.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with TypeScript examples, JSON snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project scaffolding guidance, deployment plans, CI command sequences, and Cargo CDK configuration advice for agent execution.]

## Skill Version(s):

3.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
