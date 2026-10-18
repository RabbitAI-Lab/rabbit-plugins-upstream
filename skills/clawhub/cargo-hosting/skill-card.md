## Description:

Guides developers through hosting Cargo web apps and edge workers, deploying and promoting builds, managing worker secrets, and configuring public sites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scaffold, deploy, and manage Cargo-hosted web apps and HTTP workers, including build promotion, environment configuration, and troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deploying an unintended local directory can expose source files or sensitive configuration.

Mitigation: Review the source directory and exclude sensitive files before deployment.

Risk: API tokens or app environment values may be exposed if handled as public configuration.

Mitigation: Protect API tokens and local env files; use worker-scoped secrets rather than public app variables or workspace-wide tokens where possible.

Risk: Promoting or removing the wrong resource changes live hosting, and removal can delete its deployments.

Mitigation: Confirm the active workspace and verify resource and deployment UUIDs before promotion or removal.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/cargo-hosting)
- [Project homepage (listed in skill metadata)](https://github.com/getcargohq/cargo-skills)
- [App examples](references/examples/apps.md)
- [Worker examples](references/examples/workers.md)
- [Deployment examples](references/examples/deployments.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides deployment and promotion steps; live resources change only after promotion.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
