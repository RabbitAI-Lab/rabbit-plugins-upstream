## Description:

Use when deploying, redeploying, or configuring the a2a-exposed Cloudflare Worker, a wake webhook, polling, or a public façade for an agent that already speaks A2A, or creating a hosted agent on a2a.exposed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT

## Use Case:

Developers who need to expose an A2A-compatible agent use this skill to create and configure a hosted endpoint or Cloudflare Worker, set up wake delivery, and verify that messages reach the owner.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance downloads unpinned command-line tools and includes actions that can change or delete cloud resources.

Mitigation: Review tool downloads and commands before running them; explicitly approve credential handling, elevated access, and each cloud-resource change or deletion.

Risk: Security scan coverage was partial because some referenced local paths were unavailable.

Mitigation: Review and scan the complete skill and its referenced materials before deployment.

## Reference(s):

- [Setup checklist](artifact/references/checklist.md)
- [Prerequisites](artifact/references/prerequisites.md)
- [Deployment guide](artifact/references/deploy.md)
- [Wake setup guide](artifact/references/wake.md)
- [Teardown guide](artifact/references/teardown.md)
- [Project home](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted connector guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/mcp.md#hosted-connector)
- [Hosted service](https://a2a.exposed/hosted)
- [Pricing](https://a2a.exposed/pricing)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.8.73 (source: frontmatter; release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
