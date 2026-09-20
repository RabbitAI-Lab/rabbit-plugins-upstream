## Description:

This skill lets agents operate xAI through an OOMOL-connected account for non-streaming chat completions and model lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call xAI through the OOMOL oo CLI, including creating non-streaming chat completions and retrieving model metadata. It is suited for workflows where xAI access is intentionally routed through an OOMOL-connected account instead of direct API token handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup includes running a remote installer script directly in the shell.

Mitigation: Review the official install guide and installer contents before running commands, and verify any available checksums or signatures.

Risk: xAI requests are routed through the OOMOL connector and depend on OOMOL account, connection, and billing state.

Mitigation: Install only when the user trusts OOMOL for the task, and limit use to the listed xAI actions unless the user intentionally wants OOMOL involved.

Risk: Connector actions depend on live schemas that may change over time.

Mitigation: Inspect the action schema with `oo connector schema` before constructing payloads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-x-ai)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [xAI homepage](https://x.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL oo CLI actions for non-streaming chat completions, model listing, and model metadata lookup.]

## Skill Version(s):

1.0.5 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
