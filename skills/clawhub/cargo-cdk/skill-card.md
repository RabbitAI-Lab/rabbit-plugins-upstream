## Description: <br>
Cargo Cdk helps agents define, type, preview, and deploy Cargo workspaces as TypeScript workspace-as-code using cargo-ai cdk. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cargo-ai](https://clawhub.ai/user/cargo-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when they want to manage a Cargo workspace reproducibly from code: scaffold projects, define connectors, models, tools, agents, MCP servers, apps, and workers, then plan and deploy the graph with Cargo CDK. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Deploy, destroy, and deploy --prune can change or remove live Cargo workspace resources. <br>
Mitigation: Review cargo-ai cdk plan output before deploys, use --prune deliberately, and gate destructive operations behind human review or protected CI workflows. <br>
Risk: Using the wrong selected workspace or token could reconcile code into the wrong Cargo environment. <br>
Mitigation: Verify the selected workspace before deployment and keep separate state files or branches for separate environments. <br>
Risk: API tokens and connector secrets are required for some deployments. <br>
Mitigation: Store tokens and secret() environment variables in a secure secret store or CI secret configuration, and avoid committing secret values. <br>
Risk: Losing cargo.state.json can orphan resources such as deployed plays and agents that do not have stable slugs. <br>
Mitigation: Commit cargo.state.json after deploys and use cargo-ai cdk import to recover bindings for existing live resources when needed. <br>


## Reference(s): <br>
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills) <br>
- [Authoring resources guide](guides/authoring-resources.md) <br>
- [Deploy and state guide](guides/deploy-and-state.md) <br>
- [Typed config guide](guides/typed-config.md) <br>
- [Command reference](references/commands.md) <br>
- [Resource reference](references/resources.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Full workspace example](references/examples/full-workspace.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with TypeScript and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Cargo CDK project structure, configuration advice, and commands to plan, deploy, import, or destroy workspace resources.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
