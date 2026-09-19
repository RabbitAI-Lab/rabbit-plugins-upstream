## Description:

Provides agent guidance for using OpenAI through an OOMOL-connected account and the oo CLI, including schema inspection and actions for responses, embeddings, media, moderation, batches, models, and token counting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to perform OpenAI tasks through an OOMOL-connected account while inspecting live action schemas before constructing requests. It supports read workflows and state-changing OpenAI actions such as responses, embeddings, generated media, batch jobs, and audio processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OpenAI work is routed through a third-party OOMOL-connected account.

Mitigation: Install only when this routing is intended, and avoid sending sensitive or proprietary content unless the account, connection, and data handling are approved.

Risk: The artifact recommends remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Prefer an official package, pinned release, or verified installer, and inspect installer contents before execution.

Risk: Write actions can create or change OpenAI resources such as responses, embeddings, media, batch jobs, and audio outputs.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running any write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-openai)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OpenAI API](https://openai.com/api/)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a signed-in OOMOL account with an OpenAI connection; write actions require payload review and user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
