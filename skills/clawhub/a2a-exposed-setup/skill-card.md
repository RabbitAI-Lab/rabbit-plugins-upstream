## Description:

Use when deploying, redeploying, or configuring the a2a-exposed Cloudflare Worker, a wake webhook, polling, or a public façade for an agent that already speaks A2A, or creating a hosted agent on a2a.exposed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to choose a hosted or self-hosted A2A endpoint and configure its deployment, pairing, and wake delivery. It guides setup through a real message and owner notification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the skill suspicious due to repeated unpinned command-line packages and teardown and other capabilities beyond its stated deployment purpose; the scan was partial because some local references could not be resolved.

Mitigation: Avoid installation until package commands are pinned to reviewed versions and the undeclared feedback, pairing, and destructive teardown capabilities are clarified; review the unresolved references.

## Reference(s):

- [Setup checklist](artifact/references/checklist.md)
- [Prerequisites](artifact/references/prerequisites.md)
- [Deployment guide](artifact/references/deploy.md)
- [Wake configuration](artifact/references/wake.md)
- [Pairing guide](artifact/references/pairing.md)
- [Teardown guide](artifact/references/teardown.md)
- [Troubleshooting](artifact/references/troubleshooting.md)
- [ClawHub release](https://clawhub.ai/telegraphic-dev/skills/a2a-exposed-setup)
- [Project documentation](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted setup](https://a2a.exposed/hosted)
- [Pricing](https://a2a.exposed/pricing)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with shell command examples and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setup choices and commands depend on the selected hosting and wake-delivery path.]

## Skill Version(s):

0.8.53 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
