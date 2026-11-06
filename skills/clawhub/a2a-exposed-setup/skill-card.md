## Description:

Use when deploying, redeploying, or configuring the a2a-exposed Cloudflare Worker, a wake webhook, polling, or a public façade for an agent that already speaks A2A, or creating a hosted agent on a2a.exposed. Not for reading or replying to messages (use a2a-exposed).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to set up a hosted or self-managed A2A endpoint and configure webhook or polling delivery for an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some testing and service-install examples may expose secret access keys.

Mitigation: Review credential-handling examples; test only with a receiver you control or disposable credentials, and keep tunnel tokens out of command arguments.

Risk: Account changes, saved Worker secrets, or background jobs can persist beyond a local command or unset environment variable.

Mitigation: Confirm the target account, deletion plan, and job permissions; inspect saved Worker secrets and use an isolated configuration for tests.

## Reference(s):

- [Prerequisites](references/prerequisites.md)
- [Deploy and Cloudflare consent](references/deploy.md)
- [Wake delivery and polling](references/wake.md)
- [Pairing](references/pairing.md)
- [Troubleshooting](references/troubleshooting.md)
- [Teardown](references/teardown.md)
- [Project homepage](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted inbox getting started](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [Client compatibility](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#clients)
- [Hosted service](https://a2a.exposed/hosted)
- [Hosted service pricing](https://a2a.exposed/pricing)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Step-by-step setup guidance, including consent checks and credential-handling instructions.]

## Skill Version(s):

0.8.38 (source: metadata.version, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
