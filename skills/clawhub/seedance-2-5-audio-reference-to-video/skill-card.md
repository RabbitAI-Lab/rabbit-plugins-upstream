## Description:

Seedance 2.5 参考音频生视频 helps video editors, post-production teams, advertisers, and creators generate rhythm- and mood-aligned videos from reference audio through AI Hive, with media upload, task tracking, and result download handled by the bundled CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to submit prompt-guided Seedance 2.5 reference-audio video generation jobs for ads, product videos, social media clips, short dramas, and related commercial content workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads selected media to AI Hive for Seedance 2.5 video generation.

Mitigation: Use only media that is approved for upload to AI Hive and review privacy, consent, and rights requirements before submitting a job.

Risk: Generation can incur costs, and the skill is scoped more broadly than its paid, credentialed media-upload behavior warrants.

Mitigation: Confirm that the user explicitly wants video asset creation, review routing and runtime pricing before bulk use, and treat general comparison or platform-research queries as out of scope.

Risk: The workflow requires an AI Hive API key and may store it in a local configuration file.

Mitigation: Prefer environment or local config storage with restricted permissions, avoid sharing logs or config files containing credentials, and rotate keys if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-2-5-audio-reference-to-video)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands; CLI execution may return JSON task status and downloaded video files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated video files are saved locally when download is enabled; task IDs can be reused for later status checks.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
