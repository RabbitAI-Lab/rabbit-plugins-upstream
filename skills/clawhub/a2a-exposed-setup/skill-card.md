## Description:

Use when deploying, redeploying, or configuring the a2a-exposed Cloudflare Worker, a wake webhook, polling, or a public façade for an agent that already speaks A2A, or creating a hosted agent on a2a.exposed. Not for reading or replying to messages (use a2a-exposed).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use this skill to set up hosted A2A endpoints or deploy a Cloudflare Worker, then configure webhook or polling delivery for agents. It guides setup of a public façade for an existing A2A agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill repeatedly invokes a changeable CLI package for deployment and configuration tasks.

Mitigation: Review the CLI package source and version, and check the planned cloud changes before running commands.

Risk: Teardown steps can remove cloud resources and stored data.

Mitigation: Inspect teardown targets and effects, and preserve any needed data before execution.

Risk: The security scan did not assess three unresolved local references.

Mitigation: Review those reference contents before relying on the affected workflows.

## Reference(s):

- [Project documentation](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted inbox getting started guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [Hosted A2A service](https://a2a.exposed/hosted)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes deployment, webhook, polling, and operational guidance.]

## Skill Version(s):

0.8.49 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
