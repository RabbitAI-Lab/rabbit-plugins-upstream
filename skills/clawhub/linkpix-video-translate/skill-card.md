## Description:

自动识别视频语音并翻译为多国语言，支持 AI 配音、字幕与对口型，帮助视频快速面向全球市场。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content localization teams use this skill to translate videos from Chinese or English into supported target languages with subtitle, voice, and lip-sync package options. Agents use it to prepare qhkit commands, check options and status, confirm paid generation parameters, and deliver the resulting translated video URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs agents to install or upgrade qhkit, Node, or related tooling at broad system scope.

Mitigation: Require user or administrator approval before host-level installs or upgrades, prefer trusted registries, and apply normal package integrity controls.

Risk: Video generation can consume credits and tasks cannot be cancelled after submission.

Mitigation: Before running a generate action, confirm key parameters and the estimated credit cost with the user; use read-only option, estimate, and status actions without extra confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-translate)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes task IDs, polling guidance, credit estimates where available, CLI error messages, and final media URLs when generation completes.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
