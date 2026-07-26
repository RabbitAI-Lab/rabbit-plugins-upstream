## Description: <br>
Bilibili All In One Free helps agents monitor Bilibili trends, fetch video metadata and danmaku, compare engagement data, and download public videos in 360p-1080p MP4 without account cookies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent users can use this skill to inspect Bilibili public trends, video information, engagement statistics, danmaku, playlists, and standard-resolution downloads for content discovery or offline review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Network and download actions may contact external services and save media files locally. <br>
Mitigation: Review download destinations, use known Bilibili video identifiers or URLs, and scan the skill before deployment. <br>
Risk: The artifact includes a generic API_KEY example even though the free Bilibili workflow says account cookies are not required. <br>
Mitigation: Do not provide Bilibili cookies, account credentials, or unrelated API keys unless a reviewed implementation explicitly requires them. <br>
Risk: Callback URLs could expose results to an unintended endpoint if callback handling is added or enabled. <br>
Mitigation: Use only trusted callback URLs and verify destination ownership before sending results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/bilibili-all-in-one-free) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration, JSON, Files] <br>
**Output Format:** [Markdown guidance with Python and shell command examples; runtime responses are JSON and downloaded media files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require Python dependencies and ffmpeg for some video stream merging workflows.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
