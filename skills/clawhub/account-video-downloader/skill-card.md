## Description: <br>
Fetches recent account works from Douyin, Kuaishou, Bilibili, and YouTube, resolves resource download links, and can batch-download videos or image resources locally. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, operators, analysts, and developers use this skill to retrieve account video listings, review engagement data, obtain resource links, filter by date or page, and optionally download authorized works for backup, review, or offline use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bulk watermark-free downloading of third-party videos can be used outside authorization or platform terms. <br>
Mitigation: Use the skill only for content you own, are authorized to download, or may lawfully process; confirm rights before downloading or reusing content. <br>
Risk: Target account IDs, video URLs, and REDFOX_API_KEY are sent to redfox.hk. <br>
Mitigation: Install only if that data sharing is acceptable, keep REDFOX_API_KEY in environment variables, and rotate or revoke the key if exposed. <br>
Risk: Generated direct download links may expose content access if shared in chats or logs. <br>
Mitigation: Avoid posting full resource links in shared spaces; redact sensitive links and limit retention of generated outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/account-video-downloader) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact English README](artifact/README.en.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown tables or JSON, with CLI commands and local file path notes when downloads are requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY; may create local files under the selected output directory when download is enabled.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
