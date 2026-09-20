## Description:

Operates Cloudflare Email Routing through the OOMOL oo CLI for listing destination addresses and routing rules and creating, updating, or deleting routing rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators managing Cloudflare Email Routing use this skill to inspect destination addresses and routing rules, then create, replace, or delete routing rules through an OOMOL-connected Cloudflare account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup uses remote installer commands that could execute arbitrary local code if the installer or delivery path is compromised.

Mitigation: Review the OOMOL CLI installer through a safer documented method before installation and install only when the publisher and download path are trusted.

Risk: Update and delete actions can overwrite or remove Cloudflare Email Routing rules.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

Risk: The skill relies on an OOMOL-connected Cloudflare account for Email Routing operations.

Mitigation: Use it only when the user trusts OOMOL with the connected Cloudflare Email Routing scope and account access.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-cloudflare-email-routing)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Cloudflare Email Routing](https://www.cloudflare.com/developer-platform/products/email-routing/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
