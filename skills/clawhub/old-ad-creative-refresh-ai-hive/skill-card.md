## Description:

旧广告智能改版｜AI-HIVE helps brand and marketing teams turn authorized legacy ad assets into refreshed platform-specific video plans, edit commands, AI-HIVE generation tasks, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External brand, ecommerce, advertising, and marketing teams use this skill to inspect authorized old TVC, feed, and product-video assets, preserve valid brand evidence, and produce refreshed ad plans, scripts, commands, and AI-HIVE video-generation tasks for new channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags the skill as suspicious because it includes broader AI-HIVE API capabilities and billable remote generation or upload paths.

Mitigation: Review every upload and generation command before execution, confirm routing and pricing snapshots before submitting tasks, and start with a small sample before batch work.

Risk: The skill can upload media to AI-HIVE and use it as image, video, or audio reference material.

Mitigation: Upload only media the user owns or is licensed to use, and avoid using the skill implicitly for generic video editing.

Risk: The workflow relies on an AI-HIVE API key that can be stored locally.

Mitigation: Use environment or local config storage intentionally, keep API keys out of logs and version control, and rotate keys if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/old-ad-creative-refresh-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local JSON briefs, ffmpeg commands, AI-HIVE upload or generation commands, task records, and downloaded media paths when the user runs the bundled scripts.]

## Skill Version(s):

1.0.0 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
