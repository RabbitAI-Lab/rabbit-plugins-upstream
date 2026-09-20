## Description:

抖音短视频全解析 turns a Douyin video link plus a short request into transcripts, summaries, viral-video breakdowns, storyboard scripts, rewritten or original short-video scripts, and generation prompts using Cue Omni Reader parsing plus model post-processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent users use this skill to convert Douyin video links into usable transcripts, content summaries, viral-structure analyses, scripts, and prompts. It is intended for short-video content workflows where the user provides the source link and reviews the generated outputs before reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin links and parsed video content are sent to Cue's remote service for parsing.

Mitigation: Use the skill only for content that can be shared with that service, and avoid private, sensitive, confidential, or clearly infringing videos.

Risk: A Cue API key is required and could be exposed if stored in plaintext configuration.

Mitigation: Prefer the CUE_API_KEY environment variable or another secret-managed runtime path instead of committing or sharing config files.

Risk: Visual recognition and inferred storyboard details can be wrong, especially for edited film or drama clips.

Mitigation: Treat speech transcripts and timestamps as primary evidence, label inferred or visual-identification content, and have a human review outputs before reuse.

Risk: Generated analyses or scripts may create copyright, platform-policy, or advertising-claim risk if reused without review.

Mitigation: Reuse structures and ideas only where authorized, review commercial claims manually, and avoid using the skill to bypass copyright or platform restrictions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/douyin-video-studio)
- [Cue Omni Reader online experience](https://cuecue.cn/hub/omni-reader)
- [Cue API key management](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with optional tables, JSON prompt structures, inline code blocks, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include timestamps, section headings, inferred shot details, scoring tables, and user-facing risk notes.]

## Skill Version(s):

1.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
