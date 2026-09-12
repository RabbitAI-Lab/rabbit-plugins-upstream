## Description:

Supports Minimax H3 text-to-video and image-to-video fight design by turning combat ideas into story beats, action chains, spatial routes, and action storyboards while its own documentation states that it should not output ready-to-run model prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangminrui2022](https://clawhub.ai/user/wangminrui2022)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to draft fictional or staged fight choreography, action continuity, camera beats, and reference-library routing for animated, live-action, wuxia, xianxia, and ability-driven combat scenes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security review flags detailed martial-arts and weapon choreography that could be mistaken for real-world fighting advice.

Mitigation: Use outputs only for fictional or staged choreography; do not rely on them as training or tactical instructions.

Risk: The server security review notes under-disclosed prompt-generation templates despite the skill documentation saying it should not produce prompts.

Mitigation: Review outputs before use and remove model or platform wrappers, generation parameters, negative prompts, subtitle or audio directives, and ready-to-generate prompt text from reusable references.

Risk: Reference ingestion can store private or third-party material in the reusable library.

Mitigation: Ingest only material you have rights to use; review proposed file destinations and approve writes only after removing sensitive or copyrighted content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangminrui2022/skills/ftk-sercet-minimax-h3)
- [Workflow and operating constraints](artifact/SKILL.md)
- [English README](artifact/README.en.md)
- [Changelog](artifact/changelog.md)
- [Scene route metadata](artifact/reference/scenes/00-路由元.json)
- [Action storyboard route metadata](artifact/reference/action-storyboard-design/00-路由元.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown or structured text with optional tables and bash or Python command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update local reference files and routing metadata after user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
