## Description:

Cloudflare Email Routing (cloudflare.com). Use this skill for reading, creating, updating, and deleting Cloudflare Email Routing data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Cloudflare Email Routing rules and destination addresses through an OOMOL-connected account. It supports listing routing state, creating and updating rules with schema-validated JSON payloads, and deleting rules after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote shell installer commands for the oo CLI.

Mitigation: Use a verified, versioned oo CLI installation method and review installer contents before execution.

Risk: Write and destructive actions can modify or delete Cloudflare Email Routing rules.

Mitigation: Confirm the exact payload, target zone or account, and expected effect with the user before executing state-changing actions.

## Reference(s):

- [Cloudflare Email Routing homepage](https://www.cloudflare.com/developer-platform/products/email-routing/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cloudflare-email-routing)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server-resolved release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
