## Description: <br>
Turns a podcast episode link, RSS feed, or direct audio URL into a timestamped transcript and a production-ready Chinese two-host script package with outline, script, and show notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haohuawu](https://clawhub.ai/user/haohuawu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, editors, and developers use this skill to convert public podcast episodes or audio files into transcripts, Chinese two-host production scripts, and publishable show notes. It is suited for resumable episode processing where scripted gates check outline, script, and notes formats. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill fetches podcast metadata, RSS feeds, audio, transcripts, and images from user-provided or resolved URLs. <br>
Mitigation: Use public, trusted podcast sources and avoid private or sensitive URLs unless local downloads and transcript outputs are acceptable. <br>
Risk: The first-run install path can install faster-whisper and download ASR model data into the local environment. <br>
Mitigation: Review the environment policy before running the install option, especially in managed or locked-down systems. <br>
Risk: Episode artifacts, including raw audio and transcript text, are stored locally in a temporary working directory. <br>
Mitigation: Review and clean the episode directory after processing sensitive or licensed material. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/haohuawu/skills/podcast-to-script) <br>
- [Script format spec](references/script-spec.md) <br>
- [Shownotes format spec](references/notes-spec.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, guidance] <br>
**Output Format:** [Markdown files, plain-text transcripts, timestamp files, local audio/image files, and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces an episode directory containing raw audio, script.txt, optional script.srt/script.vtt, images, outline.md, script.md, and notes.md; output is staged and resumable.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
