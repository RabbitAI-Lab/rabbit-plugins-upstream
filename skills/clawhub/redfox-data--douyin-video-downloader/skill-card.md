## Description: <br>
Fetches Douyin account works by Douyin ID, resolves downloadable media links, and can export results or save videos and images locally. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators, operators, brands, and learners use this skill to retrieve Douyin account work lists, review engagement metadata, filter by date, and optionally save authorized videos or images for backup, review, or offline study. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bulk downloads and no-watermark links can enable unauthorized copying or reuse of third-party content. <br>
Mitigation: Use the skill only for content the user owns, is authorized to archive, or otherwise has rights to download and store; verify platform-policy and rights constraints before reuse. <br>
Risk: Account IDs, video metadata, and media links are sent to redfox.hk during fetching and parsing. <br>
Mitigation: Inform users before use, avoid sensitive or unauthorized targets, and verify the RedFox API key source, scope, validity period, and revocation options. <br>
Risk: Batch downloads can save large or unintended media files to the local filesystem. <br>
Mitigation: Use an explicit output directory, review requested accounts and date filters before downloading, and keep the built-in rate limit or increase it when needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/douyin-video-downloader) <br>
- [RedFoxHub API key setup](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFoxHub](https://redfox.hk?source=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, files, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown tables or JSON summaries, with optional downloaded media files in a local output directory.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY; supports account IDs, pagination, date filters, rate limiting, and optional batch download.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
