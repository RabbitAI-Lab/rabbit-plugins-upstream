## Description:

VATlayer enables agents to calculate VAT-inclusive and VAT-exclusive prices, retrieve VAT rates, list VAT rate types, and validate VAT numbers through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate VATlayer through the oo CLI for VAT rate lookup, VAT price calculation, reduced-rate type discovery, and VAT number validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include direct execution of remotely downloaded installer scripts.

Mitigation: Install the oo CLI through a verified official release, package manager, checksum, or signature process before running VATlayer actions.

Risk: VATlayer use depends on user-controlled account connection and billing setup.

Mitigation: Only start account connection, authentication, or billing steps after a matching command failure, and keep those setup actions under user control.

## Reference(s):

- [VATlayer homepage](https://vatlayer.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub VATlayer skill page](https://clawhub.ai/oomol/skills/oo-vatlayer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses from VATlayer actions are returned as JSON data with execution metadata.]

## Skill Version(s):

1.0.3 (source: server evidence release.version and SKILL.md metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
