## Description:

Guides developers through creating and deploying Cargo-hosted web apps and edge workers, including configuration, secrets, custom domains, and promotion to production.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to scaffold, deploy, and manage public web apps and HTTP workers in a Cargo workspace, including their deployments and environment settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creating or promoting a deployment can make an app or worker publicly accessible.

Mitigation: Confirm the workspace, resource UUID, source directory, and intended visibility before creating or promoting a deployment.

Risk: API tokens or environment values may be exposed by overly broad access or public app bundles.

Mitigation: Use worker-scoped or least-privilege tokens when possible, store credentials as worker secrets, and keep tokens and .env.local files out of version control.

Risk: Hosted resources consume recurring credits, and removing a resource also removes its deployments.

Mitigation: Confirm cost and deletion impact before creating or removing resources; remove resources no longer needed.

## Reference(s):

- [Cargo Hosting skill release](https://clawhub.ai/cargo-ai/skills/cargo-hosting)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Hosting troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with CLI commands and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes deployment steps and JSON response examples.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
