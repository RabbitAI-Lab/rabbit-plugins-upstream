## Description:

Video Workflow Builder helps an agent create customized, installable video creation workflow skills for a user's platform, content niche, and persona, covering topic selection, scripts, titles, covers, and handoff guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[charriotzed](https://clawhub.ai/user/charriotzed)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, operators, and developers use this skill to have an agent generate a tailored video production workflow skill after a short platform, niche, and persona interview. The generated workflow supports research, positioning, topic selection, script writing, title crafting, cover generation, validation, and installation handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports broader scraping, credentialed transcription, direct-fetch, and WAF-bypass patterns bundled with the skill.

Mitigation: Review the skill before installation and only enable scraping or transcription utilities when those capabilities are intentionally needed and permitted.

Risk: The skill asks agents to generate files, run scripts, use API keys, and create persistent local content databases.

Mitigation: Inspect generated files and scripts before execution, keep real credentials only in git-ignored .env files, and confirm where local content databases will be written.

Risk: Bundled Douyin scraping and transcription utilities may require account cookies, Alibaba credentials, external downloader paths, and paid API calls.

Mitigation: Avoid configuring account cookies, Alibaba credentials, or external downloader paths unless the user understands the privacy, platform, account, and cost implications.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/charriotzed/skills/video-workflow-creator)
- [Server-resolved GitHub provenance](https://github.com/CharriotZed/video-workflow-builder)
- [DailyHotApi dependency](https://github.com/imsyy/DailyHotApi)
- [Title generation methodology exemplar](references/exemplars/title-gen-v3.md)
- [Bilibili finance video workflow exemplar](references/exemplars/bilibili-finance-video-skill.md)
- [Topic selection methodology](references/methodology/topic-selection.md)
- [Script writing methodology](references/methodology/script-writing.md)
- [Title craft methodology](references/methodology/title-craft.md)
- [Cover design methodology](references/methodology/cover-design.md)
- [Douyin competitor and monitoring methodology](references/methodology/douyin-competitor-and-monitoring.md)
- [Douyin platform notes](references/platforms/douyin.md)
- [Bilibili platform notes](references/platforms/bilibili.md)
- [Xiaohongshu platform notes](references/platforms/xiaohongshu.md)
- [Shipinhao platform notes](references/platforms/shipinhao.md)
- [Baijiahao platform notes](references/platforms/baijiahao.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with generated skill files, configuration examples, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate installable skill directories, scripts, .env.example files, local database helpers, image-generation prompts, and validation commands.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
