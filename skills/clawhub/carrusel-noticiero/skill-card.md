## Description:

Creates a Spanish 8-slide Instagram news carousel from a sourced AI or technology news item, including rendered 1080x1350 PNG slides and animated-cover assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[formula100k](https://clawhub.ai/user/formula100k)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and social-media operators use this skill to turn a verified AI or technology news source into Formula 100K-style Spanish carousel assets for Instagram. It is intended for newsjacking workflows that need concise slide copy, HTML theme templates, local PNG rendering, and animated-cover handoff files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated news copy or visuals may be inaccurate or misleading if the source is not verified.

Mitigation: Require a confirmed news source, avoid inventing facts, and review generated copy and assets before posting.

Risk: The workflow creates local output files and renders local HTML with Chromium.

Mitigation: Run it in an expected workspace, review the generated deliverables folder, and keep Chromium and dependencies under normal local execution controls.

Risk: The workflow may load Google Fonts, use Apify for social-post sources, and spend Higgsfield credits for cover image or video generation.

Mitigation: Confirm external-service use and paid generation before running those steps, and reuse generated cover assets when re-rendering.

Risk: The final carousel is prepared for publishing but is not automatically published by the skill.

Mitigation: Manually inspect the files before upload and publish only through the user's chosen channel.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/formula100k/skills/carrusel-noticiero)
- [Animated cover reference](artifact/reference.md)
- [Scrapbook theme reference](artifact/themes/scrapbook.md)
- [Theme template reference](artifact/themes/_template.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTML templates, shell commands, and generated local media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces an organized local deliverables folder containing PNG carousel slides, editable HTML sources, cover resources, and animated-cover handoff assets.]

## Skill Version(s):

1.0.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
