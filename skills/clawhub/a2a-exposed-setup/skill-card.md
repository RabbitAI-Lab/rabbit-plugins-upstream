## Description:

Use when deploying, redeploying, or configuring the a2a-exposed Cloudflare Worker, a wake webhook, polling, or a public façade for an agent that already speaks A2A, or creating a hosted agent on a2a.exposed. Not for reading or replying to messages (use a2a-exposed).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to choose a hosted or self-hosted deployment, configure an A2A endpoint and its wake or polling delivery, and manage pairing and teardown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that CLI commands rely on package versions that can change.

Mitigation: Review the commands and package version before installing or deploying.

Risk: The security review reports capabilities beyond setup, including destructive teardown and diagnostic reporting.

Mitigation: Review teardown and reporting steps before running them, and confirm the intended action with the owner.

## Reference(s):

- [Project homepage](https://github.com/telegraphic-dev/a2a-exposed)
- [ClawHub release page](https://clawhub.ai/telegraphic-dev/skills/a2a-exposed-setup)
- [Hosted getting started](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [Prerequisites](references/prerequisites.md)
- [Deployment](references/deploy.md)
- [Wake and polling](references/wake.md)
- [Pairing](references/pairing.md)
- [Troubleshooting](references/troubleshooting.md)
- [Teardown](references/teardown.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Operational guidance]

**Output Format:** [Markdown with inline shell commands and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deployment-specific steps; secret values should be supplied through protected storage.]

## Skill Version(s):

0.8.51 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
