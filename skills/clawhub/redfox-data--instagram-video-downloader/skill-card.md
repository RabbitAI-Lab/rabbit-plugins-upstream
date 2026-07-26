## Description: <br>
Paste an Instagram video link and get a watermark-free video download URL for supported Reels or regular posts through the redfox.hk API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators, editors, content collectors, operators, and researchers use this skill to parse Instagram Reel or post URLs and obtain direct video download links for permitted saving, editing, backup, or analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted Instagram URLs and the RedFox API key are sent to redfox.hk. <br>
Mitigation: Install only if that disclosure is acceptable for the intended use, and confirm the key source, scope, validity period, and revocation path before use. <br>
Risk: API keys can be exposed through command-line arguments, plaintext config files, logs, prompts, or shared machines. <br>
Mitigation: Prefer the REDFOX_API_KEY environment variable, avoid --save-key on shared or synced machines, and do not hardcode or print the key. <br>
Risk: Downloaded or reused Instagram content may be subject to permissions, platform rules, or applicable law. <br>
Mitigation: Download or reuse content only when you have permission and comply with the relevant rules. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/instagram-video-downloader) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [redfox.hk Instagram video download API endpoint](https://redfox.hk/story/api/parseWork/videoDownload/instagram) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown-style text with full download and cover URLs; optional JSON from the downloader script.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [One Instagram video URL per request; requires REDFOX_API_KEY and sends the submitted URL to redfox.hk.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
