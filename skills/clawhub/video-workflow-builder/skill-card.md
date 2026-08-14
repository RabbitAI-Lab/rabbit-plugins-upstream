## Description:

Generates installable, account-specific video creation workflow skills for topic selection, scripts, titles, and covers after collecting platform, content vertical, and persona inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[charriotzed](https://clawhub.ai/user/charriotzed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operators use this skill to generate a tailored video production workflow skill for a specific platform, niche, and account persona. The generated workflow guides audience research, positioning, topic selection, title writing, cover design, scripting, validation, and local setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated skills and local files may contain incorrect, stale, or misleading workflow guidance.

Mitigation: Review and scan each generated skill before installing or enabling it.

Risk: The workflow uses API keys from .env files and may call external gateways.

Mitigation: Keep real secrets only in git-ignored .env files, do not commit credentials, and use limited-scope keys where possible.

Risk: Scraping and transcription tools can process third-party video or audio and can rely on external local downloader code.

Mitigation: Use these tools only for content you are allowed to process and do not point TIKTOK_DOWNLOADER_DIR at untrusted code.

Risk: The content archive can retain generated content and research outputs over time.

Mitigation: Choose the archive location deliberately and periodically review or delete sensitive content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/charriotzed/skills/video-workflow-builder)
- [README](README.md)
- [Quick Start Guide](快速上手.md)
- [DailyHotApi](https://github.com/imsyy/DailyHotApi)
- [Platform Reference: Douyin](references/platforms/douyin.md)
- [Platform Reference: Bilibili](references/platforms/bilibili.md)
- [Platform Reference: Xiaohongshu](references/platforms/xiaohongshu.md)
- [Platform Reference: Shipinhao](references/platforms/shipinhao.md)
- [Platform Reference: Baijiahao](references/platforms/baijiahao.md)
- [Methodology: Topic Selection](references/methodology/topic-selection.md)
- [Methodology: Script Writing](references/methodology/script-writing.md)
- [Methodology: Title Craft](references/methodology/title-craft.md)
- [Methodology: Cover Design](references/methodology/cover-design.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown skill files with Python scripts, configuration templates, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local skill directories, .env templates, content archive files, and generated cover assets; generated skills should be reviewed before use.]

## Skill Version(s):

0.1.1 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
