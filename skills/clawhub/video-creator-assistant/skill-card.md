## Description:

All-in-one video creation assistant from script to publish, covering topic planning, script writing, storyboard design, copy polishing, voiceover scripts, subtitles, cover guidance, platform adaptation, trend tracking, and content analysis guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and content teams use this skill to plan, draft, adapt, and optimize short-form and mid/long-form video content for platforms including Douyin, Xiaohongshu, Bilibili, and WeChat Channels. It can produce structured scripts, storyboards, titles, cover copy, voiceover notes, subtitle text, hashtag guidance, and performance-improvement suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a persistent local learning module that can record usage, preferences, errors, and notes.

Mitigation: Review whether local memory is acceptable before installation; make learning opt-in, scope stored fields to video-creation needs, and provide inspect and delete controls for learned_patterns.json.

Risk: The artifact describes automatic improvement behavior that may update stored patterns or skill guidance over time.

Mitigation: Review generated changes before deployment and disable or restrict the learning script when self-modifying behavior is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/video-creator-assistant)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured tables and occasional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include timecoded video script tables, platform adaptation notes, topic recommendations, cover/title options, and local learning commands.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
