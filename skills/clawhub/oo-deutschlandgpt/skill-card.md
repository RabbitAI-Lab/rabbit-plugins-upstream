## Description:

DeutschlandGPT lets agents use an OOMOL-connected DeutschlandGPT account to create chat completions, generate embeddings, and list enabled models through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to route DeutschlandGPT requests through an OOMOL-connected account, including text chat completions, embedding generation, and model discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts or text inputs to a DeutschlandGPT/OOMOL-connected service for generation or embedding.

Mitigation: Use the skill only when that external processing is intended, and avoid sending sensitive text unless appropriate for the connected service.

Risk: The setup guidance includes a pipe-to-shell installer command for the oo CLI.

Mitigation: Prefer the install guide, manual review, or verification of the installer before executing it.

Risk: The scanner verdict is suspicious because the skill under-describes external generation and data-processing actions.

Mitigation: Review the action schema and payload before use, especially for chat completion and embedding requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-deutschlandgpt)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [DeutschlandGPT homepage](https://www.deutschlandgpt.de/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses may include JSON data and an execution id under meta.executionId.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
