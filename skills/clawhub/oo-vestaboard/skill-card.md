## Description:

Vestaboard (vestaboard.com). Use this skill for Vestaboard requests that read, create, or update data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Vestaboard schemas, read the current message and transition settings, send messages, and update transition behavior through an OOMOL-connected Vestaboard account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions include unverified remote installer commands.

Mitigation: Review the oo CLI installation path first and prefer official, version-pinned, checksum- or signature-verified installation instructions before running installer scripts.

Risk: Write actions can change the message or transition settings on a connected Vestaboard.

Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write.

## Reference(s):

- [Vestaboard skill page](https://clawhub.ai/oomol/skills/oo-vestaboard)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Vestaboard homepage](https://www.vestaboard.com)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May inspect live connector schemas before producing or running an oo CLI command.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
