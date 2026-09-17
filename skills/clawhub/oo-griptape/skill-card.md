## Description:

Enables agents to operate Griptape Cloud through OOMOL's oo CLI for reading, creating, updating, and deleting Griptape data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage Griptape Cloud organizations, assistants, runs, and events through an OOMOL-connected account while inspecting live action schemas before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote shell installer commands for the oo CLI.

Mitigation: Review the install path before real-account use and prefer verified official documentation or a pinned, inspectable release.

Risk: Create, update, cancel, and delete actions can change Griptape Cloud state.

Mitigation: Inspect the live action schema, confirm the exact payload and effect with the user, and require explicit approval for destructive targets.

Risk: Operations may run against a connected OOMOL account with access to real Griptape data.

Mitigation: Run only the requested action, avoid proactive login or connection flows, and reconnect only after authentication or scope errors.

## Reference(s):

- [Griptape homepage](https://www.griptape.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing JSON payloads; write and destructive actions require explicit confirmation.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
