## Description: <br>
bilibili content collection for search, creator spaces, video details, comments, and danmaku using agent-browser and public Bilibili interfaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[excalibursssooo](https://clawhub.ai/user/excalibursssooo) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and analysts use this skill to collect public Bilibili video, creator, comment, and danmaku data, then save structured JSON and human-readable harvest reports for downstream review or analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional Bilibili cookies and the agent-browser session can expose authenticated account context. <br>
Mitigation: Avoid adding SESSDATA or bili_jct unless authenticated results are needed, store cookie files outside shared locations, and never commit or share cookie files. <br>
Risk: Saved harvest outputs can contain comments, user identifiers, and other collected public data. <br>
Mitigation: Treat harvest directories as sensitive working data and periodically delete outputs that are no longer needed. <br>
Risk: Bilibili scraping paths can trigger captcha, rate limits, or temporary access errors. <br>
Mitigation: Use the skill's built-in agent-browser workflow and rate limits, prefer creator-space harvesting when possible, and pause or retry later when risk-control errors occur. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/excalibursssooo/skills/bilibili-search) <br>
- [README.md](README.md) <br>
- [docs/pitfalls.md](docs/pitfalls.md) <br>
- [Bilibili public API host](https://api.bilibili.com) <br>
- [Bilibili creator space](https://space.bilibili.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON files, guidance] <br>
**Output Format:** [Markdown guidance with bash commands, JSON harvest files, and generated REPORT.md files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Harvest outputs may include collected comments, user identifiers, video metadata, and optional danmaku records.] <br>

## Skill Version(s): <br>
0.1.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
