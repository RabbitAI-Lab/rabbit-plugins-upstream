## Description:

Guides developers in defining Cargo workspace resources in TypeScript and managing their deployment with the Cargo project CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build version-controlled Cargo workspaces, review planned changes, and deploy resources across environments or from CI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deployments or destruction can change live workspace resources.

Mitigation: Confirm the selected workspace, review the project plan, and test CRM, email, and DNS workflows in staging before deployment.

Risk: Credentials or unreviewed cookbook code could be exposed or executed.

Mitigation: Scope API tokens and secret environment variables, pin CLI and npx versions where possible, and inspect fetched cookbooks before installing or deploying them.

## Reference(s):

- [Cargo skills documentation](https://github.com/getcargohq/cargo-skills)
- [Cargo GTM skill cookbooks](https://github.com/getcargohq/gtm-skills)
- [Deployment and state guide](guides/deploy-and-state.md)
- [Resource authoring guide](guides/authoring-resources.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with TypeScript, configuration, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide changes to live Cargo workspace resources.]

## Skill Version(s):

3.1.0 (source: skill frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
