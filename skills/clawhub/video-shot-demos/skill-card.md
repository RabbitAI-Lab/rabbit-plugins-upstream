## Description:

Generates storyboard-style video demo shots as standalone HTML pages with a shared cinematic player base, varied visual styles, character assets, narration timeline alignment, screenshot quality checks, and an index overview workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[unclecheng-li](https://clawhub.ai/user/unclecheng-li)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and video production teams use this skill to turn scripts, outlines, and shot plans into polished HTML demo scenes for technical tests, product launches, courses, and narrative videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Helper scripts handle paths unsafely enough that crafted inputs could run local commands or write outside the chosen output folder.

Mitigation: Install only after review, use trusted plan.json files, trusted project directories, and trusted BROWSER_PATH values, and keep generated outputs in a disposable directory.

Risk: The screenshot workflow may use shell command construction in shot.js.

Mitigation: Prefer SHOT_ENGINE=cdp until shot.js is fixed.

Risk: Rendered pages may load Google Fonts during recording or preview.

Mitigation: Review external font loading before use in privacy-sensitive or offline environments.

Risk: Artifact behavior references a hard-coded local Windows archive path.

Mitigation: Ignore or remove the local archive reference unless explicitly inspecting that path.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/unclecheng-li/skills/video-shot-demos)
- [Mechanics](references/mechanics.md)
- [Style Cards](references/style-cards.md)
- [Character Reactions](references/character-reactions.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated HTML/CSS/JavaScript file workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces standalone HTML shot pages, project indexes, screenshot artifacts, and lint or timeline quality-check outputs.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
