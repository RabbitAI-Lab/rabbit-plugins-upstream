## Description:

HelloLeads (helloleads.io) helps agents read, create, and update HelloLeads data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate HelloLeads web form workflows through an OOMOL-connected account, including fetching form definitions and submitting supported lead data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands executed directly in a shell.

Mitigation: Prefer an official, pinned, verifiable installer, or download and inspect the installer script before execution.

Risk: Write actions can submit lead data to HelloLeads.

Mitigation: Confirm the exact payload and intended effect with the user before running any action tagged as write.

## Reference(s):

- [HelloLeads homepage](https://www.helloleads.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [HelloLeads skill on ClawHub](https://clawhub.ai/oomol/skills/oo-helloleads)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include live schema inspection guidance and connector command results.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
