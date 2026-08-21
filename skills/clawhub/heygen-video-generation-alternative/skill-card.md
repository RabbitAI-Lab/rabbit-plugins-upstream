## Description:

This skill helps agents generate silent Seedance 2.5 visual assets through AI Hive for HeyGen-like explainer video workflows, including B-roll, closed-mouth presenter shots, product demo inserts, background edits, and ending holds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, video creators, and developers use this skill to plan and invoke AI Hive Seedance 2.5 visual generation for HeyGen-like explainer projects. It supports silent visual assets while keeping voice cloning, lip sync, TTS, subtitles, and digital-avatar binding outside scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to AI Hive for generation.

Mitigation: Use only media and prompt content approved for that service, and avoid private or regulated media unless organizational approval is in place.

Risk: The AI Hive API key may be stored in ~/.ai-hive/config.json or supplied through AI_HIVE_API_KEY.

Mitigation: Protect the API key as a secret, restrict file permissions, and rotate it if it is exposed.

Risk: Presenter, product, or source-video generation can misrepresent people, brands, or product facts if unapproved assets are used.

Mitigation: Use authorized presenter and product assets, preserve closed-mouth constraints for presenters, and review generated video before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/heygen-video-generation-alternative)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown with inline bash commands and CLI-generated video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided AI Hive API key and authorized user-selected media when presenter or source assets are used.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
