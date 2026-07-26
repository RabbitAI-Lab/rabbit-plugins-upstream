## Description: <br>
Bilibili All In One helps agents monitor Bilibili trends, download and analyze videos, process subtitles and danmaku, inspect playback data, and assist with authenticated publishing workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to direct an agent through Bilibili content operations: trend monitoring, video download and format extraction, statistics tracking, subtitle and danmaku handling, playback inspection, and account-authenticated publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated features require Bilibili session cookies that can provide full account access. <br>
Mitigation: Prefer a test account, provide cookies only for features that need login, and delete or rotate cookies after use on shared or synced machines. <br>
Risk: Optional credential persistence can store Bilibili cookies in .credentials.json. <br>
Mitigation: Keep persistence off unless necessary, never commit .credentials.json, and verify local file permissions before reuse. <br>
Risk: High-frequency monitoring or batch downloading may trigger Bilibili rate limits or anti-abuse controls. <br>
Mitigation: Use conservative intervals and batch sizes, and review requests before execution when account state or publishing actions are involved. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/bilibili-all-in-one) <br>
- [SkillHub Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON response examples and inline shell or Python commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured success/error responses and setup guidance for Bilibili cookies, ffmpeg, and optional dependencies.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
