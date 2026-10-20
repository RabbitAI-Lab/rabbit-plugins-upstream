## Description:

Guides developers through creating, deploying, and managing Cargo-hosted web apps and serverless HTTP workers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to scaffold and publish Cargo web apps and HTTP workers, configure their environments, inspect deployments, and promote builds to live URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing or promoting a deployment can make an unintended app or worker live.

Mitigation: Confirm the active workspace and target UUID, inspect deployment status, and review each promotion before making it live.

Risk: Local environment files and API tokens contain sensitive material; app environment variables are public.

Mitigation: Protect .env.local and CARGO_API_TOKEN, keep credentials out of app variables, and prefer worker-scoped secrets where possible.

Risk: Removing an app or worker also removes its deployments.

Mitigation: Verify the app or worker UUID before removal and confirm that its deployments are no longer needed.

## Reference(s):

- [Cargo hosting skill on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-hosting)
- [Cargo skills homepage (listed in metadata)](https://github.com/getcargohq/cargo-skills)
- [App examples](references/examples/apps.md)
- [Worker examples](references/examples/workers.md)
- [Deployment examples](references/examples/deployments.md)
- [Hosting troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with CLI and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance includes deployment status checks before promotion.]

## Skill Version(s):

1.2.1 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
