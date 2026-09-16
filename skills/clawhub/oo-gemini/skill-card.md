## Description:

Guides agents to operate Gemini through an OOMOL-connected account using the oo CLI for text, speech, image, embedding, token-counting, model-listing, and Veo video actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call Gemini capabilities through an OOMOL-managed connector, including content generation, embeddings, token counting, image generation, model listing, and Veo video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may encourage direct execution of remote installer scripts without independent verification.

Mitigation: Review the OOMOL install guide, download installers before execution, and verify publisher, signature, or checksum where available.

Risk: Gemini access depends on an OOMOL-connected account and server-side credential handling.

Mitigation: Use the skill only when the user trusts OOMOL as the Gemini connector and has intentionally connected the required Gemini account.

Risk: Actions that generate content, images, speech, or video can produce externally visible or costly outputs depending on the connected account.

Mitigation: Inspect the live action schema first and confirm payloads for any write-tagged or cost-sensitive generation workflow.

## Reference(s):

- [ClawHub Gemini skill page](https://clawhub.ai/oomol/skills/oo-gemini)
- [Gemini API documentation](https://ai.google.dev/gemini-api)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses may include JSON data, execution IDs, generated media transit URLs, or setup guidance.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
