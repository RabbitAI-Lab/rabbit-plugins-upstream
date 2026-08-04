## Description: <br>
Xiaohongshu Video Downloader parses single or batch Xiaohongshu video links and returns watermark-free video download and cover URLs through redfox.hk. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users such as creators, editors, content collectors, and operations researchers use this skill to obtain downloadable Xiaohongshu video and cover links for editing, backup, or analysis when they have the right to do so. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Xiaohongshu links and the REDFOX_API_KEY are sent to redfox.hk for parsing. <br>
Mitigation: Use the skill only if that data sharing is acceptable; prefer the REDFOX_API_KEY environment variable and avoid saving plaintext keys on shared or synced machines. <br>
Risk: Downloaded or reused videos may be subject to platform terms, local law, or rights restrictions. <br>
Mitigation: Download or reuse videos only when you have the right to do so and can comply with applicable platform terms and local law. <br>


## Reference(s): <br>
- [Server-resolved source provenance](https://github.com/redfox-data/redfox-community/tree/main/skills/xiaohongshu-video-downloader) <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/xiaohongshu-video-downloader) <br>
- [Core Workflow](references/core_workflow.md) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=github) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or terminal text with video download URLs, cover URLs, status summaries, and optional JSON from the downloader script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY; returned video download links may expire after a short period.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
