## Description: <br>
YouTube 提文案 extracts transcript text from a YouTube link or video ID, prioritizes Chinese subtitles, can translate non-Chinese captions into Chinese, and returns transcript results in a table with optional Markdown or Excel export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, content creators, learners, researchers, operations teams, and marketing teams use this skill to turn YouTube videos into searchable transcript text for notes, content repurposing, translation, and competitive analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: YouTube links and transcript content are sent to RedFox, and non-Chinese captions may be sent to Google Translate. <br>
Mitigation: Use the skill only for content appropriate for those services, use --no-translate for original-language output, and review organizational data-sharing rules before extracting sensitive videos. <br>
Risk: The skill saves transcript files locally by default. <br>
Mitigation: Use --no-save when local transcript files are not desired, or set --output-dir to an approved location. <br>
Risk: Transcript extraction depends on available YouTube subtitle or auto-caption tracks. <br>
Mitigation: Confirm that the source video has suitable captions and review generated transcripts before using them for publication or analysis. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/youtube-digest) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFoxHub](https://redfox.hk) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown table and terminal text, with optional JSON, Markdown archive, or Excel file output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default output is clean transcript text without timestamps; timestamped transcript, original-language output, no-save mode, and Excel export are optional.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
