## Description: <br>
Video Finder helps users search, filter, and download adult videos with yt-dlp, stored preferences, proxy configuration, progress monitoring, and feedback-based preference updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiaoka520](https://clawhub.ai/user/xiaoka520) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users can use this skill to search for adult videos, compare filtered results, and download a selected video after confirmation. The skill also maintains local preferences, proxy settings, download tracking, and history files to personalize later searches. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores sensitive adult-content preferences, viewing history, download tracking, and proxy credentials in local files. <br>
Mitigation: Use it only on a private machine or account, avoid saving proxy credentials unless necessary, and review or delete preferences.json, proxy.json, history.md, and tracking/downloads.json after use. <br>
Risk: Broad trigger phrases can start search or download workflows from vague requests. <br>
Mitigation: Review the skill before installing and require explicit user confirmation before any download action. <br>
Risk: Background downloads may continue after the initial interaction and can expose sensitive local activity. <br>
Mitigation: Monitor active downloads and clear generated tracking files when finished. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xiaoka520/skills/video-finder) <br>
- [Server-resolved GitHub provenance](https://github.com/xiaoka520/video-finder) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with inline shell commands and local JSON or Markdown state files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update preferences.json, proxy.json, history.md, and tracking/downloads.json in the skill workspace.] <br>

## Skill Version(s): <br>
0.1.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
