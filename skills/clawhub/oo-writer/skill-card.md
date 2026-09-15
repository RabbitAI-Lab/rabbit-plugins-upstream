## Description:

Writer (writer.com). Use this skill for ANY Writer request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Writer through an OOMOL-connected account, including listing available Writer models and creating non-streaming chat completions from plain-text messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote shell installer commands for the oo CLI.

Mitigation: Prefer a verified, versioned release or package manager, and avoid running remote installer scripts unless the OOMOL installer delivery path is trusted.

Risk: Writer prompts and connector action payloads may pass through OOMOL's connector service.

Mitigation: Review data sensitivity before using the connector and avoid sending content that should not be processed by the connected service.

Risk: The skill can create Writer chat completions through a write-tagged action.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [Writer homepage](https://writer.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-writer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId when actions are run.]

## Skill Version(s):

1.0.3 (source: evidence.release.version and skill metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
