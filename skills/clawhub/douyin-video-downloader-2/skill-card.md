## Description: <br>
输入抖音号，自动拉取账号近期作品，解析无水印下载链接，并可批量下载视频或图文资源到本地。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, content creators, operations teams, MCNs, brands, and learners use this skill to fetch Douyin account works, review engagement data, parse download links, filter by date or page, and optionally save media locally for permitted backup, review, or editing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends Douyin IDs, work URLs, and the RedFox API key to redfox.hk. <br>
Mitigation: Use only a key you are authorized to use, keep it out of prompts, logs, and source files, and confirm you are comfortable sharing the requested account and work URLs with redfox.hk. <br>
Risk: Batch downloads can create many local media files. <br>
Mitigation: Confirm the output directory before running downloads, especially for multi-account requests. <br>
Risk: Downloaded media may be subject to platform, copyright, privacy, or contractual restrictions. <br>
Mitigation: Download and reuse only media you are allowed to store or process. <br>


## Reference(s): <br>
- [Server-resolved source import](https://github.com/redfox-data/redfox-community/tree/main/skills/douyin-video-downloader) <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/douyin-video-downloader-2) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=github) <br>
- [RedFoxHub](https://redfox.hk?source=github) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, files, shell commands, guidance] <br>
**Output Format:** [Markdown tables or JSON summaries, with optional downloaded media files in a local output directory.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a REDFOX_API_KEY and sends Douyin account IDs and work URLs to redfox.hk for listing and download-link parsing.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
