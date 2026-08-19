## Description:

Happy Horse 视频生成 helps creators, marketing teams, ecommerce teams, and short-form video teams generate videos from text and optional image, video, or audio references through AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, advertisers, ecommerce operators, and media production teams use this skill to submit AI Hive Happy Horse video generation jobs, optionally upload reference media, track task status, and download completed videos. Developers and technical operators can also use it as a command-line workflow for text-to-video, image-to-video, reference-to-video, video editing, and audio-guided video tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Server security evidence marks the release suspicious because broad competitor and ecommerce search language may invite generation when the user only asked for comparison or discovery.

Mitigation: Confirm the user intends to run video generation before submitting a job, and answer comparison or research requests without invoking generation unless generation is explicitly requested.

Risk: The workflow requires an AI Hive API key, uploads referenced local media to the remote service, may incur generation costs, and stores outputs locally by default.

Mitigation: Use a dedicated API key, avoid uploading sensitive media, verify real-time pricing and task count before costly runs, and review the output directory before sharing files.

## Reference(s):

- [ClawHub Happy Horse skill page](https://clawhub.ai/wubin1836/skills/happy-horse)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Files]

**Output Format:** [Markdown guidance with bash commands; generated media is downloaded as video files or task JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI Hive API key; default downloads are saved under ~/Downloads/AiHive.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
