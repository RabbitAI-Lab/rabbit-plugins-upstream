## Description:

Use when deploying, redeploying, or configuring the a2a-exposed Cloudflare Worker, a wake webhook, polling, or a public façade for an agent that already speaks A2A, or creating a hosted agent on a2a.exposed. Not for reading or replying to messages (use a2a-exposed).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to choose a hosted or self-managed A2A endpoint, configure its Cloudflare Worker or wake delivery, and troubleshoot or remove that deployment. It guides setup through the CLI and hosted service, with explicit human authorization for account changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions use unpinned npx package commands.

Mitigation: Review the package and release version before running commands, especially in unattended jobs.

Risk: Teardown can remove the Worker, D1 database, tunnel, Access objects, DNS records, and local configuration containing credentials.

Mitigation: Inspect the teardown plan and target Cloudflare account, explain the resources and data affected, and obtain explicit human approval before removal.

Risk: The scanner's assessment is incomplete because coverage was partial and several references could not be resolved.

Mitigation: Review the unresolved references and assess the skill again before relying on it.

## Reference(s):

- [Prerequisites](references/prerequisites.md)
- [Deployment and Cloudflare consent](references/deploy.md)
- [Wake and delivery configuration](references/wake.md)
- [Troubleshooting](references/troubleshooting.md)
- [Teardown](references/teardown.md)
- [Project homepage](https://github.com/telegraphic-dev/a2a-exposed)
- [Getting started](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [Hosted service](https://a2a.exposed/hosted)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setup steps, configuration values, and troubleshooting guidance]

## Skill Version(s):

0.8.45 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
