## Description:

Generates local, single-file HTML study workbenches that schedule lessons by school start date, show daily knowledge points, explanations, exercises, review tasks, accumulation prompts, and exam countdowns, and can be adapted to other grades, subjects, and textbook editions with JSON content packs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ranchryan](https://clawhub.ai/user/ranchryan)

### License/Terms of Use:

MIT-0

## Use Case:

External users, parents, educators, and developers use this skill to create browser-based daily study dashboards for students. They can use the default eighth-grade Chinese, math, and English content or provide a content-pack JSON file to generate a workbench for another grade, subject, or textbook edition.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad education prompts may invoke the skill when the user did not intend to create a study dashboard.

Mitigation: Confirm that the requested output is a student study workbench before generating or customizing files.

Risk: Untrusted content packs or optional textbook links can be rendered into the generated workbench.

Mitigation: Use content packs and optional book links only from trusted sources, and review JSON content before injection.

Risk: Progress is stored in the user's browser and may be lost if browser storage is cleared.

Mitigation: Use the built-in JSON or CSV export features for periodic backups before clearing browser data or moving devices.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/ranchryan/study-workbench)
- [ClawHub skill page](https://clawhub.ai/ranchryan/skills/study-workbench)
- [Project homepage](https://oierb0rbss1.feishuapp.com/app/app_17c14rw9hc0)
- [Content Pack Schema](references/content-pack-schema.md)
- [Content Pack Injection Script](references/inject_pack.js)
- [Sample Content Pack](references/sample-pack-8up-cme.json)
- [Study Workbench Engine Template](assets/study-workbench-engine.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with HTML files, JSON content packs, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a local browser workbench with localStorage persistence and optional content-pack injection for customization.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
