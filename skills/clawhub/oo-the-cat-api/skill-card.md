## Description:

The Cat API skill lets an agent search and read cat breed and image data through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect live The Cat API connector schemas and retrieve or search cat breed and image data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes running an unverified internet installer directly in a shell.

Mitigation: Review or replace the pipe-to-shell setup with a safer install method, such as a pinned package or verified installer, before running it on a machine with sensitive data.

Risk: The skill depends on OOMOL's oo CLI and an OOMOL-connected The Cat API account.

Mitigation: Install only where use of OOMOL account-mediated connector access is acceptable, and confirm account connection, billing, and authentication state before relying on the skill.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-the-cat-api)
- [The Cat API Homepage](https://thecatapi.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data payload and meta.executionId.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
