## Description:

Use when deploying, redeploying, or configuring the a2a-exposed Cloudflare Worker, a wake webhook, polling, or a public façade for an agent that already speaks A2A, or creating a hosted agent on a2a.exposed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to set up a hosted a2a.exposed agent or configure a Cloudflare Worker, then choose and configure a wake path such as a webhook, relay, or polling. It guides setup and verification of a real message reaching the owner.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious for repeatedly using an unpinned, automatically installed CLI and for including feedback submission and destructive teardown beyond the stated setup purpose. The scan was partial and does not establish intentional harm or compromise.

Mitigation: Review the command and package version before running it; use a reviewed, pinned release where available. Get explicit approval for feedback submission and resource changes or teardown.

Risk: Setup can handle owner tokens, webhook keys, signing secrets, and upstream credentials.

Mitigation: Keep credentials in protected environment or secret storage, never paste them into chat or command arguments, and protect local config files with restrictive permissions.

## Reference(s):

- [Project homepage](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted a2a.exposed service](https://a2a.exposed/hosted)
- [Setup checklist](artifact/references/checklist.md)
- [Prerequisites](artifact/references/prerequisites.md)
- [Deployment guide](artifact/references/deploy.md)
- [Wake and delivery guide](artifact/references/wake.md)
- [Troubleshooting guide](artifact/references/troubleshooting.md)
- [Teardown guide](artifact/references/teardown.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Step-by-step setup and verification guidance; commands may create or change hosted services or Cloudflare resources.]

## Skill Version(s):

0.8.60 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
