## Description:

Polar lets an agent search and read Polar customers, orders, organizations, products, and subscriptions through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent inspect Polar commerce data through an OOMOL-connected account without handling raw Polar credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions can pipe a remote installer script into a local shell.

Mitigation: Do not let an agent run the installer blindly; use an official versioned install path and verify checksums or signatures before installation.

Risk: The connected OOMOL account may expose Polar customer, order, organization, product, and subscription data to read actions.

Mitigation: Review the granted Polar scopes and connected account before use, and run only the read action needed for the user's request.

## Reference(s):

- [ClawHub Polar Skill Page](https://clawhub.ai/oomol/skills/oo-polar)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Polar Homepage](https://polar.sh)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Polar get and list actions are executed through the oo CLI after checking each action schema.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
