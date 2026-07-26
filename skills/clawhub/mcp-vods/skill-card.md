## Description: <br>
用于追剧/追番的技能，为AI提供搜索影视播放地址的能力，并支持在小米电视上直接播放。当用户想搜索影视、动漫、短剧、综艺等节目信息或更新进度时使用此技能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[al-one](https://clawhub.ai/user/al-one) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to search for movies, anime, short dramas, variety shows, and update status across multiple sources. With optional local TV configuration, the skill can also help cast selected media URLs to Xiaomi TVs or Android TV/TvBox devices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs upstream packages through npx and uvx to perform media search and casting actions. <br>
Mitigation: Install and run it only when you trust the upstream mcporter and mcp-vods packages, and review proposed commands before execution. <br>
Risk: Casting can send a media URL to a configured TV or IP address. <br>
Mitigation: Use casting only with TVs you own or are allowed to control, and confirm both the media URL and target address before playback. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/al-one/skills/mcp-vods) <br>
- [Skill homepage](https://github.com/aahl/mcp-vods) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires npx and uvx; TV casting requires optional local TV IP or list configuration.] <br>

## Skill Version(s): <br>
1.0.2 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
