## Description:

lexoffice (office.lexware.de) supports lexoffice requests involving reading, creating, and updating data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected lexoffice account through OOMOL for reading, creating, listing, and updating articles, contacts, vouchers, profile data, and organization metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that can execute downloaded shell or PowerShell code.

Mitigation: Review installation steps before use and install the oo CLI through a verified, version-pinned method with checksum or signature verification.

Risk: Create and update actions can change lexoffice business data.

Mitigation: Confirm exact payloads and expected effects with the user before running state-changing actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lexoffice)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [lexoffice homepage](https://office.lexware.de/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing lexoffice actions require user confirmation, and live action schemas should be inspected before request construction.]

## Skill Version(s):

1.0.3 (source: evidence release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
