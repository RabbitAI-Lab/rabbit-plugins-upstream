## Description: <br>
Bilibili-all-in-one helps agents monitor Bilibili trends, download videos or audio, track video metrics, process subtitles, retrieve playback and danmaku information, and manage video publishing workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content operators, creators, and developers use this skill to automate Bilibili monitoring, media retrieval, subtitle workflows, video analytics, and upload or publishing tasks through an agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use password-equivalent Bilibili session cookies for uploads and other account actions. <br>
Mitigation: Use a secondary Bilibili account when possible, provide cookies only through environment variables, and review upload or publish actions before execution. <br>
Risk: Credential persistence can save Bilibili session material to a local .credentials.json file. <br>
Mitigation: Avoid enabling BILIBILI_PERSIST or persist=True unless local storage is required, keep .credentials.json out of shared or synced folders, and verify file permissions. <br>
Risk: Automated uploads or high-frequency requests can affect a Bilibili account session or trigger platform controls. <br>
Mitigation: Keep request rates conservative and review publishing actions, account credentials, and target content before running the workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/bilibili-all-in-one) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide an agent to call Bilibili APIs, run Python commands, configure credentials, download media files, or publish account content.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
