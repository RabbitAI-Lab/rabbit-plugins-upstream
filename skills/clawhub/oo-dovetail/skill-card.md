## Description:

Dovetail (dovetail.com). Use this skill for Dovetail requests involving reading, creating, and updating data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and teams use this skill to operate Dovetail through an OOMOL-connected account. It helps agents inspect action schemas, list projects and data records, export records, inspect token metadata, and create or update data after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes one-line remote installer commands that execute downloaded scripts in a shell.

Mitigation: Prefer an official verified release or package manager, and review checksums or signatures before installing the oo CLI.

Risk: Write actions can create or update Dovetail records.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running any action tagged as write.

## Reference(s):

- [Dovetail homepage](https://dovetail.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Dovetail skill](https://clawhub.ai/oomol/skills/oo-dovetail)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
