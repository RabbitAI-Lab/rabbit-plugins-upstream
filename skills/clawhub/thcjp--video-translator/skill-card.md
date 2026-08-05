## Description: <br>
Video Translator helps an agent translate user-provided videos, generate subtitles, and prepare dubbed audio synchronized to the source media. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, localization teams, developers, and automated workflows use this skill to translate user-provided video files or URLs into target-language subtitles and dubbed audio. The artifact states it is not intended for copyrighted media processing or live simultaneous interpretation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Video files may contain sensitive media or personal data and may be sent to external services depending on the agent workflow. <br>
Mitigation: Use only selected videos you are comfortable processing, avoid sensitive media unless the external service path is known, and confirm the target service before uploading or translating. <br>
Risk: The skill may prompt media-processing commands or API calls as part of its stated purpose. <br>
Mitigation: Run commands only for explicitly requested video-processing tasks, review generated commands before execution, and keep processing constrained to the intended input files. <br>
Risk: API credentials used for video translation services could be exposed through configuration or logs. <br>
Mitigation: Provide credentials through environment variables or the agent platform's secret handling and avoid storing keys in skill files, logs, or version control. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/video-translator) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with JSON result examples and optional shell command or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide subtitle outputs such as SRT/VTT files, dubbed audio, synchronized media tracks, and status/error reports.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
