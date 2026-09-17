## Description:

Gemini helps agents use an OOMOL-connected Gemini account through the oo CLI to generate text, speech audio, images, embeddings, token counts, and videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Gemini action schemas, run Gemini connector actions, and handle first-time OOMOL account, connection, and billing setup when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path asks users to run internet-downloaded installer scripts for the oo CLI.

Mitigation: Review the installer path before installing, and prefer a signed or package-manager installation or verify the installer before running it.

Risk: Gemini generation actions may consume connected-account credits.

Mitigation: Inspect the live action schema and confirm credit-impacting generation or video requests before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gemini)
- [Gemini API documentation](https://ai.google.dev/gemini-api)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Gemini-generated text, audio, image, video, embedding, model-list, token-count, or operation-status data through the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
