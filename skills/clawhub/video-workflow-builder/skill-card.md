## Description:

Builds custom video creation workflow skills for specific platforms, niches, and creator personas, covering topic selection, scripts, titles, and covers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[charriotzed](https://clawhub.ai/user/charriotzed)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, content teams, and agent users use this skill to generate a reusable video production workflow skill after providing only a target platform, content niche, and creator persona. The generated workflow guides research, positioning, topic selection, script writing, title generation, cover design, and delivery setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create other installable skills and write multiple files.

Mitigation: Inspect generated skills and their files before enabling or installing them.

Risk: Bundled scripts use external search, image, and LLM gateways.

Mitigation: Use dedicated limited API keys and avoid placing real credentials in tracked files.

Risk: Optional Douyin tooling can involve persistent storage and social-platform scraping workflows.

Mitigation: Avoid storing personal social-platform sessions unless that tooling is explicitly needed; remove or disable scraping and transcription scripts for basic workflow-builder use.

Risk: Security evidence rates the release as suspicious due to broad capabilities, even though it is not proven malicious.

Mitigation: Review the skill, its generated outputs, and bundled scripts before deployment.

## Reference(s):

- [Server-resolved source repository](https://github.com/CharriotZed/video-workflow-builder)
- [ClawHub skill page](https://clawhub.ai/charriotzed/skills/video-workflow-builder)
- [DailyHotApi dependency](https://github.com/imsyy/DailyHotApi)
- [Douyin platform methodology](artifact/references/platforms/douyin.md)
- [Bilibili platform methodology](artifact/references/platforms/bilibili.md)
- [Xiaohongshu platform methodology](artifact/references/platforms/xiaohongshu.md)
- [Shipinhao platform methodology](artifact/references/platforms/shipinhao.md)
- [Baijiahao platform methodology](artifact/references/platforms/baijiahao.md)
- [Topic selection methodology](artifact/references/methodology/topic-selection.md)
- [Script writing methodology](artifact/references/methodology/script-writing.md)
- [Title craft methodology](artifact/references/methodology/title-craft.md)
- [Cover design methodology](artifact/references/methodology/cover-design.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance plus generated skill files, Python scripts, configuration examples, and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create an installable skill directory and supporting files after user confirmation.]

## Skill Version(s):

0.1.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
