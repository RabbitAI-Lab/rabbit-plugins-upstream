## Description:

将已剪辑的口播工程拆成按 beat 组织的视觉派单，分配真人出镜、动态图、AI 情景动画或影视素材，并生成供 gtrk 校验的清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gitruck](https://clawhub.ai/user/gitruck)

### License/Terms of Use:

MIT-0

## Use Case:

Video editors and creators use the skill to turn a finished talking-head edit and transcript into a beat-level visual plan and dispatch queues for motion graphics, dramatic reenactment, and film B-roll.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can continue from a visual plan into downstream actions that change the video project.

Mitigation: Work on a project copy. If only a visual plan is wanted, explicitly limit the task to dispatch and prohibit downstream actions or timeline changes.

Risk: Cloud steps depend on the Gitruck CLI.

Mitigation: Review the Gitruck CLI dependency before enabling cloud steps.

## Reference(s):

- [Field schema](references/field-schema.md)
- [Example visual split (JSON)](references/example-visual-split.json)
- [Example visual split (Markdown)](references/example-visual-split.md)
- [Gitruck CLI](https://github.com/Gitruck/cli)
- [ClawHub release page](https://clawhub.ai/gitruck/skills/gtrk-splitter)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Shell commands, Guidance]

**Output Format:** [Beat-level visual split JSON and dispatch queues, with Markdown guidance and gtrk CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Utterance-ID spans and lane assignments; the CLI projects timeline values during dispatch.]

## Skill Version(s):

1.3.9 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
