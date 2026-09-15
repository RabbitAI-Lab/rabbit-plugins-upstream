## Description:

Plain lets agents read, create, and update Plain customer data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Plain customer records, including customer lookup, search, and create-or-update workflows through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions can run an unverified internet installer on the user's machine.

Mitigation: Prefer a verified official installer, pinned release, checksum, or signature check before installing the oo CLI.

Risk: Write actions can change Plain customer data.

Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged as write.

## Reference(s):

- [Plain homepage](https://www.plain.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and requires confirmation for write actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
