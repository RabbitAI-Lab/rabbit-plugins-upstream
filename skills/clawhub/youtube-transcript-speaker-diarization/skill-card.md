## Description: <br>
Generate speaker-aware YouTube transcripts through diarize for attributed speakers in TXT, JSON, SRT, or VTT format. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[patelnav](https://clawhub.ai/user/patelnav) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to submit YouTube URLs to diarize, poll transcript jobs, and retrieve speaker-aware transcripts for readable answers, structured processing, or subtitle workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the YouTube URL and transcript job data to diarize.io or to a configured compatible base URL. <br>
Mitigation: Use it only when that external processing is approved; avoid private, confidential, or regulated video links unless approved. <br>
Risk: The skill depends on a local API key resolved from documented environment or OpenClaw configuration paths. <br>
Mitigation: Keep the API key in the documented credential locations and avoid sharing configuration files or command output that exposes it. <br>


## Reference(s): <br>
- [diarize documentation](https://diarize.io/docs) <br>
- [diarize API key settings](https://diarize.io/settings/api-keys) <br>
- [ClawHub skill listing](https://clawhub.ai/patelnav/skills/youtube-transcript-speaker-diarization) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Plain text, JSON, SRT, or VTT transcript content with Markdown command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bash, curl, jq, and a diarize API key; the default run flow polls for transcript completion.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
