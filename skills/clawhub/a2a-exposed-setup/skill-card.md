## Description:

Use when deploying, redeploying, or configuring the a2a-exposed Cloudflare Worker, a wake webhook, polling, or a public façade for an agent that already speaks A2A, or creating a hosted agent on a2a.exposed. Not for reading or replying to messages (use a2a-exposed).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to choose hosted or self-hosted A2A deployment, configure delivery and wake methods, and manage pairing, troubleshooting, and teardown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags repeated use of unpinned, automatically installed CLI packages as suspicious.

Mitigation: Review the CLI release and command effects before running package commands, especially commands that change hosted or Cloudflare resources.

Risk: Teardown commands can delete the Worker, its D1 database, tunnels, Access resources, DNS records, and local configuration containing credentials.

Mitigation: Inspect the uninstall dry-run and resource plan, confirm the target account and data, and obtain explicit owner approval before removal; retain any needed data and credentials securely.

## Reference(s):

- [Deployment](references/deploy.md)
- [Wake and delivery](references/wake.md)
- [Pairing](references/pairing.md)
- [Prerequisites](references/prerequisites.md)
- [Troubleshooting](references/troubleshooting.md)
- [Teardown](references/teardown.md)
- [A2A Exposed repository](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted inbox getting started](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [Hermes setup recipe](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/hermes.md)
- [Hosted service](https://a2a.exposed/hosted)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown instructions with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and configuration guidance depend on the selected hosting and delivery method.]

## Skill Version(s):

0.8.48 (source: frontmatter metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
