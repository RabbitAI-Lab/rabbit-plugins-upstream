## Description:

Generate publication-ready scientific figures with the official SciDraw AI web app and public API. Use for paper figures, graphical abstracts, mechanism diagrams, research workflows, and model architectures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[toplocalai](https://clawhub.ai/user/toplocalai)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, academic authors, and developers use this skill to plan and generate scientific figure images such as paper figures, graphical abstracts, mechanism diagrams, research workflows, and model architectures with SciDraw AI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and supplied source details to SciDraw AI during generation.

Mitigation: Use it only with content that may be shared with SciDraw AI, and summarize limitations after inspecting the returned figure.

Risk: Confirmed API generation consumes SciDraw AI account credits.

Mitigation: State the requested resolution and image count, then get user confirmation before starting a credit-consuming generation.

Risk: The SciDraw AI API key could be exposed if pasted into chat, prompts, committed files, or public packages.

Mitigation: Store the key only in the local environment as SCIDRAW_API_KEY and never include credentials in outputs, logs, prompts, or files.

Risk: Changing the API base URL can send requests to a different service.

Mitigation: Keep the default SciDraw AI API endpoint unless the user intentionally trusts another endpoint.

Risk: Generated image downloads write to local output paths and could overwrite unimportant files.

Mitigation: Choose output paths where overwriting a generated image would not matter.

## Reference(s):

- [SciDraw AI Drawing](https://sci-draw.com/ai-drawing)
- [SciDraw AI API Documentation](https://sci-draw.com/docs/api)
- [SciDraw AI OpenAPI Specification](https://sci-draw.com/api/openapi.yaml)
- [ClawHub Skill Page](https://clawhub.ai/toplocalai/skills/scidraw-ai-scientific-illustration)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands; the helper script can print plain text or JSON status and saves generated image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 1-4 generated images at 2K or 4K, configured aspect ratios, and local output paths.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
