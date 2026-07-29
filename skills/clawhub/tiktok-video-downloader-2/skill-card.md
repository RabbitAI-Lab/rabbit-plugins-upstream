## Description: <br>
Parses single or batched TikTok video links through RedFox and returns watermark-free download resources, including video links, cover images, audio links, descriptions, and expiry reminders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators, editors, collectors, and operations researchers use this skill to retrieve downloadable TikTok video resources for saving, editing, backup, or analysis. It accepts TikTok web or short links, validates that inputs are TikTok links, and can process multiple links in one request. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: TikTok links and the RedFox API key are sent to redfox.hk for processing. <br>
Mitigation: Install only if that third-party sharing is acceptable, prefer the REDFOX_API_KEY environment variable, and keep the key revocable. <br>
Risk: Private or sensitive TikTok links may be disclosed to a third-party parsing service. <br>
Mitigation: Avoid submitting private or sensitive links, and use the skill only with links appropriate for third-party processing. <br>
Risk: Large batches can produce substantial, unbounded output. <br>
Mitigation: Use small batches and review returned links promptly because generated download URLs are time-limited. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/redfox-data/redfox-community/tree/main/skills/tiktok-video-downloader) <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/tiktok-video-downloader-2) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=github) <br>
- [Core workflow](references/core_workflow.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown-style terminal output with optional JSON API response output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include video download URLs, cover image URLs, audio URLs, content descriptions, duration metadata, per-link status, and batch success or failure counts.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
