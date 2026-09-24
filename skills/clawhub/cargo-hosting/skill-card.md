## Description:

Helps agents use Cargo CLI hosting to scaffold, create, deploy, promote, configure, and troubleshoot hosted web apps, edge workers, deployments, secrets, custom domains, and search-indexable public sites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to publish Cargo-hosted static apps and serverless HTTP workers, then manage deployments, environment variables, secrets, logs, custom domains, and troubleshooting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through creating, promoting, or removing public Cargo-hosted apps and workers.

Mitigation: Confirm the target workspace and review deployment, promotion, and removal commands before execution.

Risk: CARGO_API_TOKEN and worker secrets may be exposed or over-scoped if handled as normal app configuration.

Mitigation: Treat CARGO_API_TOKEN as a secret, prefer worker-scoped secrets over workspace-wide tokens, and avoid placing credentials in public app environment variables.

Risk: Hosted resources can consume monthly credits while they remain active.

Mitigation: Review resource ownership and billing impact before creating resources, and remove apps or workers that should no longer be served.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cargo-ai/skills/cargo-hosting)
- [Cargo Skills Homepage](https://github.com/getcargohq/cargo-skills)
- [App examples](references/examples/apps.md)
- [Deployment examples](references/examples/deployments.md)
- [Worker examples](references/examples/workers.md)
- [Hosting response shapes](references/response-shapes.md)
- [Hosting troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell commands, JSON examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Cargo CLI commands and API calls that create, modify, promote, or remove hosted resources.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
