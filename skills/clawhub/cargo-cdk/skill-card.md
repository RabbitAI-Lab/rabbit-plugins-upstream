## Description:

Manage a Cargo workspace as code by defining connectors, models, plays, tools, agents, MCP servers, segments, context, folders, files, workers, and apps in TypeScript, then reconciling them with cargo-ai cdk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and RevOps engineers use this skill to scaffold, author, review, and deploy reproducible Cargo workspaces as TypeScript-managed infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide changes to live Cargo workspace resources.

Mitigation: Review cargo-ai cdk plan before deploys and confirm the active workspace with cargo-ai whoami.

Risk: Destructive or broad commands can remove resources or apply production-impacting changes.

Mitigation: Treat destroy --all, deploy --prune, and CI --yes as deliberate, reviewed actions.

Risk: Secrets and API tokens may be exposed if handled directly in code or committed files.

Mitigation: Store tokens only as secrets and use environment-backed secret handling for deploy-time credentials.

Risk: Losing cargo.state.json can break the link between code and deployed resources.

Mitigation: Keep cargo.state.json committed and review state changes as part of deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo-cdk)
- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [Cargo cookbooks](https://github.com/getcargohq/cargo-cookbooks)
- [Command reference](artifact/references/commands.md)
- [Resource reference](artifact/references/resources.md)
- [Troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with TypeScript examples, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include deployment review steps for live Cargo workspace changes.]

## Skill Version(s):

1.2.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
