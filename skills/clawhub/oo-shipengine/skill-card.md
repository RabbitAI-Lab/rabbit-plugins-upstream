## Description:

Helps agents operate ShipEngine through an OOMOL-connected account by inspecting live action schemas and running ShipEngine connector actions for rates, carriers, and address parsing or validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to calculate or estimate shipping rates, retrieve rate details, list connected carriers, parse addresses, and validate mailing addresses through a connected ShipEngine account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ShipEngine requests may include sensitive addresses and shipment details routed through OOMOL.

Mitigation: Use the skill only when that routing is acceptable, and confirm payload contents before rate calculation, address parsing, or address validation.

Risk: The setup guidance includes remote installer commands for the oo CLI.

Mitigation: Prefer a signed, pinned, and verifiable installation method instead of running the remote installer commands as written.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-shipengine)
- [ShipEngine Homepage](https://www.shipengine.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI commands against the user's connected ShipEngine account after live schema inspection.]

## Skill Version(s):

1.0.4 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
