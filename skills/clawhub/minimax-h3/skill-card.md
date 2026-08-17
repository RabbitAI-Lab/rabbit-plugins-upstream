## Description:

Generates MiniMax H3 videos through AI Hive from text prompts and optional image, video, or audio references, with task submission, progress checks, and result download support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketing teams, e-commerce teams, and production teams use this skill to generate MiniMax H3 videos for ads, product videos, social content, short dramas, and comic-style video workflows. Developers and operators can run the included CLI to upload reference media, submit AI Hive video jobs, query task status, and download completed outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The activation scope is broader than MiniMax H3 video generation and may appear during general AI-tool comparison or marketplace research.

Mitigation: Use the skill only after the user explicitly chooses MiniMax H3 generation or asks to run the AI Hive video workflow.

Risk: Prompts and selected media files are sent to AI Hive for generation.

Mitigation: Confirm the user is comfortable sending the specific prompt and media to AI Hive before upload or task submission, and avoid sensitive content unless policy allows it.

Risk: Video generation and batch runs may incur service costs.

Mitigation: Check live model pricing and confirm quantity, routing mode, and expected cost before high-volume or expensive generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/minimax-h3)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with shell commands; CLI output includes JSON task data and downloaded video files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is saved to a local output directory; API credentials may be read from CLI arguments, environment variables, or a local config file.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
