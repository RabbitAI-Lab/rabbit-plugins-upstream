## Description:

从输入视频一气呵成生成中文解说成片或原声剧情短片。用户提供 .mp4 / .mov / .mkv / .webm，并要求剪辑、添加旁白、配音、总结或制作短剧/电视剧/电影/纪录片/科普解说时使用。在同一个自包含技能内完成视频理解、导演立意与选镜剪辑、解说撰稿与校验、TTS 配音及音画混音合成。触发词：视频解说、视频旁白、生成解说、视频 recap、video recap、voiceover、narration、recap。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要制作中文视频解说或原声剧情短片的创作者与剪辑人员，帮助他们从视频素材完成理解、故事与镜头规划、解说撰写、配音、字幕和成片交付。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags a local dashboard path-confinement concern and incomplete scan coverage.

Mitigation: Review the dashboard and its access to project directories, and avoid sensitive projects until the path-boundary concern and scan coverage are addressed.

Risk: Optional project information may be sent to external video-understanding or speech-generation providers.

Mitigation: Review the documented data flows and provider choices before use, and avoid sending sensitive project material unless those transfers are acceptable.

## Reference(s):

- [视频解说总入口 on ClawHub](https://clawhub.ai/worldwonderer/skills/video-recap)
- [Audio modes](references/audio-modes.md)
- [Creative editing playbook](references/creative-editing-playbook.md)
- [Research guide](references/research-guide.md)

## Skill Output:

**Output Type(s):** [Video files, Subtitles, JSON configuration, Markdown, Shell commands]

**Output Format:** [Rendered MP4 video, SRT/ASS subtitles, and optional JSON or Markdown project and review files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the selected editing and audio modes; generated from user-provided video and project inputs.]

## Skill Version(s):

1.0.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
