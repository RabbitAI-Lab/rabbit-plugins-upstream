## Description:

Converts a prepared Instagram Stories script into finished 9:16 PNG story images by selecting brand photos, building native Instagram-style prompts, and generating assets with Banana/Gemini or Higgsfield.

This skill is ready for commercial/non-commercial use.

## Publisher:

[formula100k](https://clawhub.ai/user/formula100k)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, social-media operators, and brand teams use this skill to turn approved story scripts into Instagram-ready image assets with the user's own visual style and photos. It supports workflows that need prompt construction, photo matching, image generation, preview, and regeneration guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personal or client images may be selected from the configured photo folder and sent to external image-generation services.

Mitigation: Use a curated folder with only approved brand photos, avoid third-party or client images without permission, and confirm the chosen generation service before running.

Risk: The workflow saves presets, converted files, generated PNGs, and run metadata to local folders.

Mitigation: Review the configured photo, preset, and output paths before execution and check generated files after each run.

Risk: Generated slides can contain distorted faces, incorrect text, or invented visual details if the source photo or capture is missing.

Mitigation: Preview every slide, regenerate low-quality outputs, and require the user to provide missing screenshots or photos instead of inventing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/formula100k/skills/historias-a-imagenes-nanobanana)
- [Formula100k publisher profile](https://clawhub.ai/user/formula100k)
- [Parser del Guion](references/parser-guion.md)
- [Instagram Stories Native Design System](references/instagram-design-system.md)
- [Prompt Builder](references/prompt-builder.md)
- [Foto Matcher](references/foto-matcher.md)
- [Motor Selection](references/motor-selection.md)

## Skill Output:

**Output Type(s):** [Files, Markdown, JSON, Guidance]

**Output Format:** [PNG image files with JSON run metadata and a Markdown preview of generated slides.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Designed for 1080x1920 or higher 9:16 Instagram Stories outputs; may include A/B image variants when both generation motors are requested.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
