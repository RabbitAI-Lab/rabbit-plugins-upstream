## Description:

Use this skill to operate Poper through an OOMOL-connected account with the oo CLI for reading popup and response data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect live Poper connector schemas and list popups or collected popup responses through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Poper account data is accessed through OOMOL as an intermediary.

Mitigation: Use this skill only when the user is comfortable with an OOMOL-connected Poper account and oo CLI sign-in.

Risk: Connector payload requirements can change over time.

Mitigation: Fetch the live Poper connector schema before constructing each action payload.

Risk: Future added connector actions may write, remove, or overwrite Poper data.

Mitigation: Confirm exact payloads and effects before write actions, and require explicit user approval before destructive actions.

## Reference(s):

- [ClawHub Poper skill page](https://clawhub.ai/oomol/skills/oo-poper)
- [Poper homepage](https://www.poper.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed and authenticated oo CLI with Poper connected in OOMOL.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
