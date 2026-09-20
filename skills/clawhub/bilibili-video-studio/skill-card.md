## Description:

B站视频全解析 turns a Bilibili video URL and a short user request into transcripts, summaries, viral-video breakdowns, shooting scripts, rewritten scripts, prompts, PPT extraction notes, or exam-study notes using Cue Omni Reader plus model-based post-processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and content-operations teams use this skill to parse Bilibili videos and produce reusable Markdown deliverables such as transcripts, summaries, video structure analysis, script drafts, prompt packs, slide notes, and study notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bilibili URLs and possibly temporary media links are sent to Cue's remote parsing service.

Mitigation: Use public or authorized videos only, and avoid private or rights-sensitive content.

Risk: Cue API keys can be exposed if stored in plaintext local configuration.

Mitigation: Prefer the CUE_API_KEY environment variable over plaintext ~/.cue/config.json storage.

Risk: Raw transcripts, reports, and keyframe images may be written into the workspace.

Mitigation: Review workspace outputs before sharing or committing them, and remove sensitive generated files when no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/bilibili-video-studio)
- [Cue Omni Reader online experience](https://cuecue.cn/hub/omni-reader)
- [Cue API key management](https://cuecue.cn/hub/api-key)
- [Cue subscription page](https://cuecue.cn/pay)
- [Bilibili video metadata API](https://api.bilibili.com/x/web-interface/view?bvid=BVxxxxxxxx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables, inline shell commands, and optional structured JSON prompt output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write raw transcripts, reports, keyframe images, and generated Markdown files into the workspace for larger workflows.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
