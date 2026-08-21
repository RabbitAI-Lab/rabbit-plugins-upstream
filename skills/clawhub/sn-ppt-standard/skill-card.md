## Description:

sn-ppt-standard is a standard and fast presentation-generation pipeline that coordinates research, image generation or search, slide HTML creation, and PPTX/PDF export through a staged CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and presentation-building agents use this skill to create polished slide decks from user prompts, uploaded materials, web research, local images, generated visuals, and charts. It supports a fast draft mode for immediate iteration and a standard mode with style previews and a user-selected PPTX or PDF output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deck content and images can be sent to configured model services.

Mitigation: Review confidentiality requirements before use and prefer explicit, narrowly scoped credentials in an isolated project environment.

Risk: The local workbench bridge can automatically use local Hermes or OpenClaw-style credentials.

Mitigation: Review bridge settings before installation on shared developer machines and avoid broad shared credentials.

Risk: The skill can create and overwrite deck files during staged generation and export.

Mitigation: Run it in the intended deck directory and review generated outputs before distributing presentations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-ppt-standard)
- [HTML generation constraints](artifact/references/html_constraints.md)
- [Style catalog](artifact/references/style_catalog.md)
- [Export package metadata](artifact/scripts/export_pptx/package.json)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Markdown, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands plus generated HTML, images, PPTX, or PDF files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces intermediate JSON artifacts and local slide assets; final export depends on the selected PPTX or PDF format.]

## Skill Version(s):

2026.8.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
