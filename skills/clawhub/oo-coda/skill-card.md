## Description:

Coda (coda.io) enables an agent to read, create, and update Coda data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Coda connector schemas, run read actions, and prepare confirmed write actions for docs, pages, tables, columns, rows, users, and asynchronous mutations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes unverified remote installer commands for the oo CLI, which could execute arbitrary local code if the installer path is compromised or not independently trusted.

Mitigation: Review installer provenance before use and prefer an official, versioned, signed, or checksum-verified oo CLI installation path.

Risk: Write actions can create pages or upsert rows in Coda.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running any action tagged as write.

## Reference(s):

- [ClawHub Coda skill](https://clawhub.ai/oomol/skills/oo-coda)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Coda homepage](https://coda.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Coda connector schema inspection, JSON action payloads, command results, setup guidance, and confirmation prompts for write actions.]

## Skill Version(s):

1.0.3 (source: SKILL.md metadata and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
