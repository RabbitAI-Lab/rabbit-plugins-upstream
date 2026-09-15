## Description:

Operate Mux video assets, direct uploads, and playback IDs through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect schemas and run Mux connector actions for video asset, direct upload, playback ID, and metadata workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded code.

Mitigation: Verify the installer source and review the install script before running the command.

Risk: The skill runs Mux actions through OOMOL-mediated access.

Mitigation: Use the skill only when the user accepts OOMOL-mediated Mux access and has connected the intended Mux account.

Risk: Some actions can change or permanently delete Mux assets.

Mitigation: Confirm the exact payload and effect before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [Mux homepage](https://www.mux.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mux)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
