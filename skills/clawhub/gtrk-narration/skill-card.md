## Description:

将具有自身叙事时序的本地长素材提炼为解说稿与视频成片编排。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gitruck](https://clawhub.ai/user/gitruck)

### License/Terms of Use:

MIT-0

## Use Case:

内容创作者可用它把旅行、影视、游戏、探店或做饭等具有自身时序的本地素材，整理成解说稿与视频剪辑工程。它按素材时序安排画面，并支持 TTS 配音或用户口播。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Early transcription can send local audio to an external provider without clearly informing the user first.

Mitigation: Before processing private or client recordings, disclose the external audio processing provider and its privacy terms and obtain approval; otherwise skip cloud transcription or use a supplied transcript.

Risk: Some workflow steps may incur charges.

Mitigation: Confirm the displayed charges before starting paid steps.

## Reference(s):

- [Gitruck CLI homepage](https://github.com/Gitruck/cli)
- [gtrk-narration on ClawHub](https://clawhub.ai/gitruck/skills/gtrk-narration)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell command examples and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workflow plans for editing local footage into narration videos; cloud transcription and paid media steps require user review.]

## Skill Version(s):

1.3.9 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
