## Description:

Convert Chinese WeChat public-account articles and supplied images into publish-ready vertical WeChat Channels videos with article analysis, fact-safe scripting, 9:16 layout direction, Edge TTS narration, subtitle synchronization, rendering guidance, visible covers, and delivery QA.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tobewin](https://clawhub.ai/user/tobewin)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Content, marketing, and product teams can use this skill to turn Chinese WeChat public-account articles and supplied images into traceable, publish-ready vertical videos for WeChat Channels, including narration, subtitles, covers, publish copy, and QA artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voiceover text may be sent to Edge TTS during narration generation.

Mitigation: Review sensitive drafts before network TTS generation and use only article text that is appropriate to process with that service.

Risk: The workflow creates project and release files and runs local Python and FFmpeg tooling.

Mitigation: Run the skill in a dedicated project workspace, inspect generated files, and review QA outputs before publishing.

Risk: Medical or product videos can become misleading if claims, indications, or disclaimers are expanded beyond the source article.

Mitigation: Use the evidence map and content brief to trace claims to source text, preserve required disclaimers, and complete the final medical fact check.

Risk: Unlicensed or unverified images can create rights or accuracy issues in the finished video.

Mitigation: Use only supplied or licensed visual assets, copy them into the project source bundle, and visually verify each asset before storyboard generation.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/ToBeWin/wechat-article-video-skill)
- [README](README.md)
- [Content And Compliance](references/content-and-compliance.md)
- [Vertical Layout System](references/layout-system.md)
- [Storyboard And Timeline Schema](references/storyboard-schema.md)
- [Delivery QA](references/qa.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Media]

**Output Format:** [Markdown guidance with JSON project files, shell commands, MP4/JPG/MP3/SRT media artifacts, and QA reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Targets 1080x1920, 30 fps WeChat Channels videos with synchronized narration, burned-in subtitles, a frame-0 cover, contact sheet, and delivery QA report.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
