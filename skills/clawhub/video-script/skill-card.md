## Description:

根据视频分析与现有成片证据，策划剪辑、撰写并校验带时间戳的中文解说，也支持宣发文案修订。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

视频创作者和剪辑团队根据已有画面、对白及成片证据制定故事与声音方案，生成带时间戳的中文解说，并修订标题、花字等宣发文案。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow writes planning, narration and review files in the project work_dir.

Mitigation: Use a dedicated work_dir and review generated files before incorporating them into a production edit.

Risk: MiMo review can send narration, transcript excerpts and planning context to an external service; end-to-end orchestration runs it by default before TTS.

Mitigation: For sensitive material, do not run review.py and disable orchestrated review with --no-review-narration or REVIEW_NARRATION=0; strict review settings override these switches.

## Reference(s):

- [ClawHub video-script release](https://clawhub.ai/worldwonderer/skills/video-script)
- [Creative editing playbook](references/creative-editing-playbook.md)
- [Research guide](references/research-guide.md)
- [Promotional copy guide](references/promotional-copy.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [JSON plans and timecoded narration; Markdown proposals and review reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Planning files, optional clip plans and validated narration are written under work_dir; promotional-only tasks may return copy proposals.]

## Skill Version(s):

1.0.6 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
