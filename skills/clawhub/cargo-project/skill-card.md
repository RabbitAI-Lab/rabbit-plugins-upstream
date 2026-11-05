## Description:

Defines Cargo workspaces in TypeScript and helps plan, deploy, and review their resources as code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to build repeatable, version-controlled Cargo workspace configurations and review planned changes before deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deployments can change live resources and incur scheduled or recurring costs.

Mitigation: Review plans, schedules, costs, and pending executions before deployment; use --no-auto-deploy to begin with plans only when connecting GitHub.

Risk: Contact data may be shared with enrichment providers, and uploaded files may be indexed or visible more broadly than intended.

Mitigation: Confirm data sharing is appropriate and set file indexing and visibility deliberately.

Risk: Workspace secrets and service permissions can grant access beyond what a project needs.

Mitigation: Limit permissions and workspace secrets to the minimum needed.

Risk: Rollback restores deployment state but does not reverse completed external actions.

Mitigation: Review pending executions and consider external effects before applying changes.

Risk: Unpinned packages or downloaded cookbooks can change or introduce unexpected behavior.

Mitigation: Pin package versions and review downloaded cookbooks before use.

## Reference(s):

- [Cargo Project on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-project)
- [Cargo Skills repository (listed as the skill homepage)](https://github.com/getcargohq/cargo-skills)
- [Deploy and state guide](guides/deploy-and-state.md)
- [Command reference](references/commands.md)
- [Resource reference](references/resources.md)
- [Cookbook menu](references/cookbooks.md)

## Skill Output:

**Output Type(s):** [Code, Configuration, Shell commands, Guidance]

**Output Format:** [TypeScript, JSON, shell commands, and Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Contents depend on the requested workspace task.]

## Skill Version(s):

4.4.1 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
