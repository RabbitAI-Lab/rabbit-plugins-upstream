## Description:

Guides deployment and configuration of a2a-exposed hosted agents or Cloudflare Workers, including wake webhooks, polling, and public A2A façades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use this skill to set up or reconfigure an A2A agent endpoint on a2a.exposed or in their Cloudflare account, and to configure wake delivery through webhooks, polling, or a relay. It guides consent, deployment, verification, and teardown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill repeatedly uses the unpinned `a2a-exposed@latest` CLI, so the package and deployed Worker template can change between runs.

Mitigation: Review the current package and proposed changes before execution, and follow the documented confirmation steps for account changes.

Risk: The security guidance flags destructive teardown actions for review.

Mitigation: Before teardown, review each resource slated for removal and obtain the owner's explicit confirmation.

Risk: The security scan was partial because some local references could not be resolved, leaving evidence about those references incomplete.

Mitigation: Inspect unresolved references and complete a security review of them before installation.

## Reference(s):

- [Setup checklist](references/checklist.md)
- [Deployment guide](references/deploy.md)
- [Wake configuration guide](references/wake.md)
- [Teardown guide](references/teardown.md)
- [Hosted MCP connector instructions](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/mcp.md#hosted-connector)
- [Project repository (listed as homepage)](https://github.com/telegraphic-dev/a2a-exposed)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown instructions with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setup steps depend on the chosen hosting path, account access, and wake method.]

## Skill Version(s):

0.8.74 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
