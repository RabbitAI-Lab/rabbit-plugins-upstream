## Description:

Operate Sensibo devices through an OOMOL-connected account, including listing devices, retrieving device details and AC states, and setting AC state with the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Sensibo devices connected through OOMOL: list devices, inspect device details and AC state, and update AC state after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands executed directly in a shell.

Mitigation: Do not run the installer commands as-is; use an official, versioned installation method with checksum or signature verification.

Risk: The set_ac_state action changes Sensibo AC state.

Mitigation: Approve the action only after reviewing the exact target device and full payload with the user.

Risk: The skill depends on OOMOL-mediated access to Sensibo.

Mitigation: Use it only where OOMOL account access, Sensibo connection status, and billing requirements are acceptable for the task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sensibo)
- [Sensibo homepage](https://home.sensibo.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an OOMOL-connected Sensibo account; write actions require explicit confirmation of the target device and payload.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
