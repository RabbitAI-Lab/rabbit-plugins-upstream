## Description:

Enables agents to operate Doubao Speech through an OOMOL-connected account for speech-to-text and text-to-speech workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run Doubao Speech recognition and synthesis tasks through OOMOL-managed connector credentials. The skill guides agents to inspect live action schemas before building payloads and to confirm state-changing speech job submissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may pipe a remote installer directly into a shell.

Mitigation: Review OOMOL's official CLI installation method first and prefer a package manager, pinned release, or downloaded installer that can be inspected and verified.

Risk: Doubao Speech credentials are brokered through an OOMOL-connected account.

Mitigation: Connect Doubao Speech only when the user trusts OOMOL to broker connector credentials, and avoid placing raw credentials in prompts, files, or logs.

Risk: The submit_stt and submit_tts actions create asynchronous speech tasks and may affect account state or billing.

Mitigation: Inspect the live connector schema and confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-doubao-speech)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Doubao Speech homepage](https://www.volcengine.com/product/doubao-voice)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action payload construction.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
