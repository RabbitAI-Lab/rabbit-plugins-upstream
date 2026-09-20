## Description:

Operate Mux through the OOMOL oo CLI for reading, creating, updating, and deleting Mux assets, uploads, playback IDs, and metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Mux action schemas and manage video assets, direct uploads, playback IDs, and metadata through an OOMOL-connected Mux account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write and destructive Mux actions can change, overwrite, or delete assets and related data.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write actions, and require explicit approval before destructive actions.

Risk: Running remote installer commands for the oo CLI can expose the environment to supply-chain risk.

Mitigation: Use trusted official installation instructions for the oo CLI and review installer commands before execution.

## Reference(s):

- [Mux homepage](https://www.mux.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when the oo CLI is run with --json.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
