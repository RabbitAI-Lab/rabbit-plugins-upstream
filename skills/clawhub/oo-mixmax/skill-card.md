## Description:

Use this skill to read, create, and update Mixmax data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Mixmax action schemas, list or search sequences and recipients, and add recipients to Mixmax sequences through the OOMOL oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes a remote installer command that may be unsafe if run without review.

Mitigation: Review the oo CLI installation path and prefer a pinned package or verified installer before installing.

Risk: The add_sequence_recipients action changes Mixmax state.

Mitigation: Confirm the exact recipient-add payload and expected effect with the user before running write actions.

## Reference(s):

- [Mixmax homepage](https://www.mixmax.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mixmax)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and return connector data with an execution id in meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
