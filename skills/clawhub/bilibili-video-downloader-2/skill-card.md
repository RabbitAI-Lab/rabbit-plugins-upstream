## Description: <br>
Parses Bilibili video links through RedFox to return watermark-free direct download links for single or batch requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, video collectors, and operations analysts use this skill to turn supported Bilibili URLs into direct video download links and cover links. It supports single-link and batch workflows for saving authorized videos or reviewing content offline. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bilibili URLs are sent to redfox.hk for parsing. <br>
Mitigation: Use the skill only when you are comfortable sharing those URLs with RedFox and avoid submitting sensitive or private links. <br>
Risk: API keys may be exposed if passed on the command line or saved in plaintext configuration. <br>
Mitigation: Prefer the REDFOX_API_KEY environment variable, avoid --save-key on shared or synced machines, and do not place keys in prompts, logs, or files. <br>
Risk: Downloaded videos may be subject to copyright law or platform rules. <br>
Mitigation: Download only videos you are authorized to save and use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/bilibili-video-downloader-2) <br>
- [Server-resolved GitHub source](https://github.com/redfox-data/redfox-community/tree/main/skills/bilibili-video-downloader) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=github) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown tables by default, with JSON available through the script option.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY; returned video download links are temporary and should be used promptly.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
