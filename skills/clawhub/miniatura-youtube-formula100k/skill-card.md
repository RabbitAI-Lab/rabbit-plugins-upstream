## Description:

Creates YouTube thumbnail concepts and generation workflows in the FORMULA 100K style, including competitor analysis, reference-style cloning, and delivery guidance for generated variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[formula100k](https://clawhub.ai/user/formula100k)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and marketing teams use this skill to plan, generate, compare, and refine YouTube thumbnail variants from selfies, reference thumbnails, or a video topic. It helps produce image-generation prompts, generated thumbnail files, and CTR-focused recommendations for iteration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can upload selfies and reference images to external image-generation services.

Mitigation: Use only images the user is authorized to process, obtain explicit consent before uploads, and confirm the user is comfortable with Higgsfield or Gemini receiving the images.

Risk: Generated outputs and uploaded source images may be stored locally without clear retention rules.

Mitigation: Define where files are saved, share those paths with the user, and delete source or generated images when they are no longer needed.

Risk: The artifact includes guidance to retry when safety filters block generation.

Mitigation: Stop when a safety filter blocks a request, revise the user-facing goal to a compliant alternative, and avoid repeated attempts to bypass the filter.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/formula100k/skills/miniatura-youtube-formula100k)
- [MODO CLONAR ESTILO - Higgsfield](references/clonar-estilo-higgsfield.md)
- [Metodologia de Miniaturas - FORMULA 100K](references/metodologia-miniaturas.md)
- [9 Estilos de Miniatura + Prompts Base para NanoBanana](references/estilos-plantillas.md)
- [Configuracion NanoBanana para Miniaturas YouTube](references/banana-thumbnail-config.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with prompts, file paths, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or reference generated thumbnail image files and local delivery paths.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
