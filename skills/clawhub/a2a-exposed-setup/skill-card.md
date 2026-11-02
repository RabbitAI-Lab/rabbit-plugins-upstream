## Description:

Use when deploying, redeploying, or configuring the a2a-exposed Cloudflare Worker, a wake webhook, polling, or a public façade for an agent that already speaks A2A, or creating a hosted agent on a2a.exposed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to set up, configure, troubleshoot, and remove a hosted or self-hosted A2A endpoint, including its wake, polling, pairing, and Cloudflare resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Testing and service-install examples could expose secret access keys.

Mitigation: Review those examples before installing; use a separate test setup with dummy credentials for public webhook inspectors, and keep tunnel tokens out of command arguments.

Risk: The externally downloaded implementations were not verified by the bundled-file inspection.

Mitigation: Pin reviewed CLI versions, particularly for scheduled runs, and follow the documented approval plan for Cloudflare changes and destructive teardown.

## Reference(s):

- [Prerequisites](references/prerequisites.md)
- [Deploy](references/deploy.md)
- [Wake and polling](references/wake.md)
- [Peer pairing](references/pairing.md)
- [Troubleshooting](references/troubleshooting.md)
- [Teardown](references/teardown.md)
- [Project homepage](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted A2A option](https://a2a.exposed/hosted)
- [Getting started and supported clients](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#clients)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes step-by-step setup, operational, troubleshooting, and teardown guidance.]

## Skill Version(s):

0.8.30 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
