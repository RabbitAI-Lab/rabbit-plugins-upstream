## Description:

Guides developers in building, running, deploying, and securing long-running Node.js HTTP functions on Neon branches, including streaming endpoints and scheduled or storage-triggered handlers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to build and deploy Neon Functions for APIs, streaming agents, webhooks, MCP servers, and scheduled or storage-triggered work, with guidance for connecting to branch Postgres and hardening public routes.

### Deployment Geography for Use:

aws-us-east-1, aws-us-east-2, aws-eu-central-1, and aws-ap-southeast-1

## Known Risks and Mitigations:

Risk: ClawScan marks the skill suspicious and reports partial analysis, including purpose mismatches and examples involving tokens, bucket access, data counting, and third-party privacy.

Mitigation: Review those examples and the scanner's Review status against the intended use before relying on the guidance; treat the assessment as incomplete.

Risk: The skill includes an unpinned install command.

Mitigation: Verify the package source and pin the version before running the command.

## Reference(s):

- [Neon Functions overview](https://neon.com/docs/compute/functions/overview.md)
- [Deploy Neon Functions](https://neon.com/docs/compute/functions/deploy.md)
- [Neon Functions authentication](https://neon.com/docs/compute/functions/authentication.md)
- [Neon Function Triggers](https://neon.com/docs/cli/triggers.md)
- [Production hardening guidance](https://neon.com/docs/ai/skills/neon-functions/references/production-hardening.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Technical guidance]

**Output Format:** [Markdown with TypeScript examples, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setup, deployment, authentication, streaming, trigger, and production guidance.]

## Skill Version(s):

1.0.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
