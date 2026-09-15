## Description:

Agenty lets agents operate Agenty through an OOMOL-connected account to read, create, update, and delete data without calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Agenty action schemas and run Agenty connector actions through the OOMOL `oo` CLI for agents, lists, jobs, web capture, PDF conversion, downloads, and structured extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup asks users to execute mutable remote installer scripts directly.

Mitigation: Prefer an official signed or checksum-verified OOMOL CLI installation method before running Agenty connector actions.

Risk: Write and destructive Agenty actions can create, update, stop, or delete agents, lists, rows, jobs, and configurations.

Mitigation: Confirm the exact target, payload, and expected effect with the user before approving any action tagged write or destructive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-agenty)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Agenty homepage](https://agenty.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown with inline shell commands, JSON payloads, connector responses, and downloadable file references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Agenty connector schemas before constructing action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
