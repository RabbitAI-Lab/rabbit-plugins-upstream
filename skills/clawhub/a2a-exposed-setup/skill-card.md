## Description:

Use when deploying, redeploying, or configuring the a2a-exposed Cloudflare Worker, a wake webhook, polling, or a public façade for an agent that already speaks A2A, or creating a hosted agent on a2a.exposed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to set up a hosted or self-hosted A2A endpoint and configure webhook or polling delivery. It guides deployment, credentials, pairing, and teardown decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can change cloud resources and create polling costs.

Mitigation: Approve the exact account, resources, handling mode, and polling costs before setup.

Risk: Owner credentials and message handling need protection.

Mitigation: Protect owner credentials, enable owner notifications, and prefer the token-file tunnel launch on shared machines.

Risk: Teardown can delete data.

Mitigation: Preview teardown before deleting data.

Risk: Externally fetched latest-release code can change beyond the instructions reviewed here.

Mitigation: Review the currently fetched release when its behavior matters; the security review covers the bundled instructions only.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/telegraphic-dev/skills/a2a-exposed-setup)
- [Project documentation](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted inbox getting started](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [Deploy guide](references/deploy.md)
- [Prerequisites](references/prerequisites.md)
- [Wake guide](references/wake.md)
- [Pairing guide](references/pairing.md)
- [Teardown guide](references/teardown.md)
- [Troubleshooting guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.8.33 (source: server release metadata, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
