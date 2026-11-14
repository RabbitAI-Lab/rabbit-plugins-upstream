## Description:

Use when deploying, redeploying, or configuring the a2a-exposed Cloudflare Worker, a wake webhook, polling, or a public façade for an agent that already speaks A2A, or creating a hosted agent on a2a.exposed. Not for reading or replying to messages (use a2a-exposed).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to set up a hosted or self-hosted A2A endpoint, configure how it receives wake events, and verify that it can handle a real message. It guides setup decisions and consent before service or Cloudflare account changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup commands use a changeable CLI package version, so command behavior can change between runs.

Mitigation: Review the package version and commands before execution; use a reviewed pinned release when reproducibility is needed.

Risk: Setup and troubleshooting may send test requests to external destinations.

Mitigation: Confirm each test destination and the data it will receive, and use only approved endpoints.

Risk: Teardown commands can remove cloud resources, DNS and access configuration, and local credentials or project data.

Mitigation: Review the teardown plan, target account, and resources first; obtain explicit owner confirmation and preserve any needed data before removal.

Risk: The security analysis is partial, so its lack of listed findings does not establish that every behavior was assessed.

Mitigation: Review the relevant setup and teardown commands and documentation before use.

## Reference(s):

- [Setup checklist](references/checklist.md)
- [Deployment guide](references/deploy.md)
- [Wake setup guide](references/wake.md)
- [Teardown guide](references/teardown.md)
- [Project homepage](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted service](https://a2a.exposed/hosted)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setup guidance and commands depend on the selected hosting and wake-delivery options.]

## Skill Version(s):

0.8.56 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
