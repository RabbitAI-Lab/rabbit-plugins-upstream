## Description: <br>
Transforms an existing voice recording or TTS audio file into a Protoss-style psionic voice effect using local SoX and FFmpeg processing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vemec](https://clawhub.ai/user/vemec) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Use as a post-processing step for user-provided recordings or TTS output when an agent needs a deep, resonant StarCraft-inspired Protoss voice effect. The skill does not generate speech; it processes selected local audio files and writes a processed output file. <br>

### Deployment Geography for Use: <br>
User-selected local execution environment; the evidence does not identify a geography-specific deployment restriction. <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs local ffmpeg and sox commands against audio files selected by the user. <br>
Mitigation: Install only when comfortable with local audio processing, keep backups of important recordings, and review the selected input path before execution. <br>
Risk: Unusual filenames, including names beginning with a dash, can be risky when passed to command-line media tools. <br>
Mitigation: Use simple filenames for input audio or rename files before processing. <br>
Risk: Raw or intermediate audio may be removed when treated as temporary workflow output. <br>
Mitigation: Ask the agent to preserve raw or intermediate files when they are needed for audit, remixing, or recovery. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vemec/skills/protoss-voice) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/vemec) <br>


## Skill Output: <br>
**Output Type(s):** [audio, shell commands, guidance] <br>
**Output Format:** [Processed local audio file with a _psionic suffix, plus terminal status messages and usage guidance.] <br>
**Output Parameters:** [Input audio file path; output path is auto-derived by appending _psionic before the extension.] <br>
**Other Properties Related to Output:** [Requires local ffmpeg and sox binaries. Temporary WAV intermediates are created in the output directory and removed after processing. No server-resolved GitHub provenance is available for this version.] <br>

## Skill Version(s): <br>
1.1.1 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
