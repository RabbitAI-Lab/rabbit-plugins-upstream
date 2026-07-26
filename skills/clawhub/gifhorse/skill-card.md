## Description: <br>
Search video dialogue and create reaction GIFs with timed subtitles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coyote-git](https://clawhub.ai/user/coyote-git) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use GifHorse to search dialogue in local video libraries, preview timed clips, create subtitled reaction GIFs, and optionally send completed GIFs through iMessage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs and uses an external GifHorse command-line repository. <br>
Mitigation: Install only after trusting the linked repository and review the install command before running it. <br>
Risk: The workflow processes local video folders and stores searchable transcription data. <br>
Mitigation: Choose video folders deliberately and keep the transcription database in a user-controlled location such as GIFHORSE_DB. <br>
Risk: Subtitle download and optional iMessage sending can contact external services or send media to recipients. <br>
Mitigation: Use local .srt files to avoid subtitle downloads when needed, and verify GIF content and recipient before using --send or --send-to. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/coyote-git/skills/gifhorse) <br>
- [GifHorse GitHub Repository](https://github.com/Coyote-git/gifhorse) <br>
- [GifHorse Usage Guide](https://github.com/Coyote-git/gifhorse/blob/main/USAGE_GUIDE.md) <br>
- [GifHorse Roadmap](https://github.com/Coyote-git/gifhorse/blob/main/ROADMAP.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides use of the gifhorse and ffmpeg command-line tools, including transcription, dialogue search, GIF generation, file output, and optional iMessage sending.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
