## Description:

Guides an agent through a single high-quality Pruna p-video-2 short-video generation request from text, image anchors, or audio, with prompt, mode, and generation settings checked before the API call.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to prepare and execute one Pruna p-video-2 prediction for polished B-roll, start/end frame animation, or a short motion shot with stronger lip-sync. It helps the agent collect required inputs, draft a faithful video prompt, choose supported settings, and redirect out-of-scope multi-scene, avatar-only, or video-editing requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill references unpinned npx installs for companion PrunaAI skill packages and the skills runner.

Mitigation: Review the packages before installation and pin them to known versions or commits in controlled environments.

Risk: Prompts, images, and audio may be sent to Pruna when using the documented API workflow.

Mitigation: Use a least-privileged environment and avoid sending sensitive or unauthorized media or prompts.

Risk: The skill exposes a safety-control option through the API request fields.

Mitigation: Keep safety controls enabled unless the user's policy and review process explicitly allow disabling them.

Risk: The workflow can trigger paid external API calls.

Mitigation: Confirm prompt, mode, resolution, duration, fps, and draft settings with the user before submitting a prediction.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-video-2)
- [Pruna file upload API endpoint](https://api.pruna.ai/v1/files)
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl command blocks and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include prompt text, Pruna API request fields, upload or prediction commands, and safety or routing guidance; generated media is produced by the external Pruna API.]

## Skill Version(s):

1.0.12 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
