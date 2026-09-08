## Description:

用多模态大模型分析视频：内容摘要、分段时间线、镜头/运镜/转场/情绪、画面事实与屏幕文字OCR。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content teams use this skill to ask an agent to inspect video URLs or files, summarize content, build segmented timelines, extract screen text, and analyze visual facts, shots, motion, transitions, and emotion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-supplied video files or URLs are sent to the We-Media cloud API for processing.

Mitigation: Use the skill only for media whose privacy and retention requirements allow third-party processing; avoid confidential or regulated media unless those terms have been reviewed.

Risk: The API key may be stored in local config files or supplied through the environment.

Mitigation: Limit access to the local configuration, avoid sharing workspaces containing keys, and rotate or revoke the key if exposure is suspected.

Risk: Generated outputs and cached paid API responses can remain on disk.

Mitigation: Delete generated result files and the skill cache after sensitive runs, or run in a disposable workspace.

Risk: The skill can invoke paid endpoints after confirmation.

Mitigation: Review the printed cost estimate and require explicit user confirmation before rerunning with --yes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dunkong/skills/video-content-understanding)
- [Publisher profile](https://clawhub.ai/user/dunkong)
- [We-Media API site](https://api.we-media.cn)

## Skill Output:

**Output Type(s):** [text, markdown, json, files, shell commands, configuration guidance]

**Output Format:** [Markdown, JSON, Excel files, and terminal markers with generated file paths, consumption, and balance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid calls require an API key and explicit confirmation after a cost estimate; generated results are written to disk and paid POST responses may be cached for 24 hours.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter says v1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
