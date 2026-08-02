## Description: <br>
Use when someone needs word-level timestamps from audio for lyric alignment, cut-safe line boundaries, or caption source timing before burn-in with video-editing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and media workflow agents use this skill to collect required audio inputs, configure Replicate access, and run WhisperX workflows that produce word-level transcript timing for lyric alignment, captioning, and video-editing cuts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio may be sent to Replicate/Pruna-backed workflows. <br>
Mitigation: Confirm the provider terms fit the use case and avoid submitting sensitive audio unless that handling is approved. <br>
Risk: REPLICATE_API_TOKEN could be exposed through logs, shared files, or copied commands. <br>
Mitigation: Keep the token private and provide it through environment variables or a secrets manager. <br>
Risk: Recommended companion skills can change the workflow's risk profile. <br>
Mitigation: Install and inspect companion skills only when they are trusted for the task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/whisperx) <br>
- [Replicate model: victor-upmeet/whisperx](https://replicate.com/victor-upmeet/whisperx) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with bash snippets and structured input guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides Replicate token setup and audio input collection; expected workflow artifacts include transcript JSON and SRT timing files.] <br>

## Skill Version(s): <br>
1.0.8 (source: server evidence release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
