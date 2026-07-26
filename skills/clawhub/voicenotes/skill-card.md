## Description: <br>
Sync and access voice notes from Voicenotes.com, including recordings, transcripts, AI summaries, markdown sync, and transcript search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shawnhansen](https://clawhub.ai/user/shawnhansen) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to retrieve Voicenotes recordings, transcripts, and summaries, then sync them into local markdown files for personal knowledge management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A Voicenotes access token is required and can expose account note data if mishandled. <br>
Mitigation: Keep VOICENOTES_TOKEN out of logs, screenshots, shell history, dotfiles, and repositories. <br>
Risk: Synced markdown files can contain private transcripts, summaries, tags, and note metadata. <br>
Mitigation: Sync into a private directory and exclude generated notes from public version control and shared backups. <br>


## Reference(s): <br>
- [Voicenotes](https://voicenotes.com) <br>
- [Voicenotes token settings](https://voicenotes.com/app?obsidian=true#settings) <br>
- [Voicenotes Obsidian sync API](https://api.voicenotes.com/api/integrations/obsidian-sync) <br>
- [ClawHub skill page](https://clawhub.ai/shawnhansen/skills/voicenotes) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Markdown, Configuration guidance] <br>
**Output Format:** [Markdown guidance with bash commands; scripts return JSON and write markdown files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires VOICENOTES_TOKEN; markdown sync also requires jq and writes local note files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
