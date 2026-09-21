## Description:

抖音短视频全解析 helps agents turn Douyin video links into transcripts, summaries, viral-structure breakdowns, shooting scripts, script drafts, and prompt reconstructions using Cue Omni Reader results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and content teams use this skill to analyze Douyin videos and convert them into reusable transcripts, summaries, breakdown reports, production scripts, generated script drafts, and prompt templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin links are sent to Cue's remote service for parsing.

Mitigation: Use the skill only when the user is comfortable sending the target links to that service.

Risk: The security scan flags API-key handling because the skill text asks the user to paste a full Cue API key in chat and may write it to a local config file.

Mitigation: Configure the key through an environment variable or another secure local mechanism, do not paste it into chat, and rotate any key that has already been shared.

Risk: Generated breakdowns can include inferred visual details, and the artifact notes that video-frame recognition can misidentify people or works.

Mitigation: Treat speech transcripts and explicit parsed text as the primary source, and label inferred or visual-recognition details before using them in public or commercial outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/douyin-video-studio)
- [Cue Omni Reader](https://cuecue.cn/hub/omni-reader)
- [Cue API key management](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with tables, inline shell commands, and optional structured JSON prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write generated reports to workspace files; requires a Douyin video link and a user-configured Cue API key.]

## Skill Version(s):

1.1.1 (source: server release metadata; artifact frontmatter and auto changelog mention 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
