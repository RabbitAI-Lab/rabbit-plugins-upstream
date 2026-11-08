## Description:

Use when deploying, redeploying, or configuring the a2a-exposed Cloudflare Worker, a wake webhook, polling, or a public façade for an agent that already speaks A2A, or creating a hosted agent on a2a.exposed. Not for reading or replying to messages (use a2a-exposed).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to choose hosted or self-hosted delivery and configure an A2A endpoint, wake path, and related Cloudflare resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deployment and teardown can create or remove Cloudflare resources and local configuration or credentials.

Mitigation: Confirm the selected account and exact resources before changes; review the teardown plan and use its dry-run option before removal.

Risk: The documented npx commands use unpinned package versions, including while Cloudflare credentials or tokens may be available.

Mitigation: Review the package version before running commands and keep credentials in protected environment or secret storage, never in chat or command-line arguments.

Risk: The security scan reports partial coverage, so it does not establish that the skill is safe.

Mitigation: Review the deployment, hosted setup, and teardown steps before use, especially where credentials or infrastructure changes are involved.

## Reference(s):

- [Project homepage](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted service](https://a2a.exposed/hosted)
- [Hosted setup guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [Deployment instructions](references/deploy.md)
- [Wake configuration](references/wake.md)
- [Teardown instructions](references/teardown.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setup, verification, and teardown guidance for hosted or self-hosted A2A endpoints.]

## Skill Version(s):

0.8.46 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
