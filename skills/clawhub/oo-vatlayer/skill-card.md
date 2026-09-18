## Description:

Enables an agent to operate VATlayer through an OOMOL-connected account for VAT rate lookup, VAT number validation, and VAT-inclusive or VAT-exclusive price calculation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query VATlayer through the oo CLI for VAT rates, VAT number validation, and VAT-compliant price calculations without handling raw VATlayer credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can run arbitrary local code if executed without integrity verification.

Mitigation: Review and install the oo CLI through an official, integrity-verified method before using VATlayer actions.

## Reference(s):

- [VATlayer homepage](https://vatlayer.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-vatlayer)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live VATlayer connector schemas before running actions; raw VATlayer credentials are not handled by the agent.]

## Skill Version(s):

1.0.3 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
