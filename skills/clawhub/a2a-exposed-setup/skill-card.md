## Description:

Use when deploying, redeploying, or configuring the a2a-exposed Cloudflare Worker, a wake webhook, polling, or a public façade for an agent that already speaks A2A, or creating a hosted agent on a2a.exposed. Not for reading or replying to messages (use a2a-exposed).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to create a hosted A2A agent or deploy and configure a self-hosted A2A endpoint with wake delivery. It guides setup choices and checks that the owner receives a real message.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports repeated use of unpinned downloaded command-line packages, including in credentialed environments.

Mitigation: Review the package release and setup instructions before running commands, and avoid exposing unnecessary credentials in the execution environment.

Risk: The security review reports teardown actions whose destructive effects may not be clear to an installer.

Mitigation: Read the teardown guide and confirm the affected resources before running removal or forwarding-change commands.

Risk: The security review was partial because some referenced paths were unresolved.

Mitigation: Review the relevant setup and teardown references before installation; the scan does not cover every referenced path.

## Reference(s):

- [Setup checklist](references/checklist.md)
- [Deployment guide](references/deploy.md)
- [Wake setup and delivery](references/wake.md)
- [Prerequisites](references/prerequisites.md)
- [Troubleshooting](references/troubleshooting.md)
- [Pairing](references/pairing.md)
- [Teardown](references/teardown.md)
- [Hosted A2A service](https://a2a.exposed/hosted)
- [A2A getting started: hosted inbox and clients](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [HTTP and native A2A relay](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/http-relay.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown guidance with shell commands, configuration examples, and setup checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.8.63 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
