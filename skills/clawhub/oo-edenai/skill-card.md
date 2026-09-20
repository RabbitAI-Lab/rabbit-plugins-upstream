## Description:

Eden AI (edenai.co). Use this skill for ANY Eden AI request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Eden AI through an OOMOL-connected account, inspect connector schemas, run validated JSON payloads, create non-streaming chat completions, and list available Eden AI models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can execute remote installer scripts on the user's machine.

Mitigation: Review the installer path before use and prefer a versioned, verifiable OOMOL CLI source or inspect the installer script before execution.

Risk: Chat completion requests may send prompt data through Eden AI and OOMOL and may consume account credits.

Mitigation: Avoid sending sensitive data unless approved for the connected account, confirm expected usage, and monitor billing or credit errors before retrying.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-edenai)
- [Eden AI homepage](https://www.edenai.co)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId when actions are run.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
