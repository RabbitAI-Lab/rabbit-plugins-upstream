## Description:

Uses LinkPix through qhkit to identify and remove burned-in video subtitles, repair the affected image area, and produce clean video material.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, translators, and agents preparing video assets use this skill to remove hard subtitles before reuse or downstream translation. It guides qhkit setup, task submission, status polling, and delivery of the processed video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may involve installing qhkit and uploading selected videos to a paid third-party video processing service.

Mitigation: Review the skill before installing, confirm the user is comfortable with the provider upload, and obtain explicit confirmation before spending provider credits.

Risk: API keys or stored credentials could be exposed if pasted into chat or handled insecurely.

Mitigation: Do not ask users to paste API keys into chat; have them set QHKIT_TOKEN or configure qhkit locally, then verify only masked configuration output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-subtitle-remove)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, status polling guidance, processed video URLs, and provider credit information when available.]

## Skill Version(s):

0.1.3 (source: server release evidence, released 2026-08-25)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
