## Description:

Cloudflare Email Routing helps agents read and manage Cloudflare email routing rules and destination addresses through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to list Cloudflare Email Routing rules and destination addresses, create or update routing rules with schema-validated JSON payloads, and delete rules after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer one-liners that can execute local code with the user's privileges.

Mitigation: Review the installer endpoint and prefer trusted installation steps before running the remote installer commands.

Risk: Write and destructive actions can change or delete Cloudflare Email Routing state.

Mitigation: Confirm the exact payload, target zone or account, and expected effect with the user before running write or delete actions.

## Reference(s):

- [Cloudflare Email Routing](https://www.cloudflare.com/developer-platform/products/email-routing/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cloudflare-email-routing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server evidence release.version and skill metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
