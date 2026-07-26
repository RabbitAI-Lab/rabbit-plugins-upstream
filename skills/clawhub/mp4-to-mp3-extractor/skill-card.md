## Description: <br>
MP4 to MP3 Extractor batch-converts .mp4 videos in a selected directory into .mp3 audio files while preserving the source folder structure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangminrui2022](https://clawhub.ai/user/wangminrui2022) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to ask an agent to extract audio from local MP4 video collections into MP3 files, including batch processing for course videos, downloaded videos, and media folders. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may change the Python environment by creating or reusing a virtual environment and installing or upgrading packages at runtime. <br>
Mitigation: Review the scripts before deployment, pin dependencies, and move package installation to an explicit setup step controlled by the user or administrator. <br>
Risk: The skill may automatically download and install FFmpeg with limited user control. <br>
Mitigation: Preinstall FFmpeg from an approved source or require explicit user approval before allowing automated FFmpeg installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wangminrui2022/skills/mp4-to-mp3-extractor) <br>
- [OpenClaw project](https://github.com/openclaw/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Guidance] <br>
**Output Format:** [MP3 audio files with command-line status and log text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Preserves relative folder structure and defaults the output directory to [source directory]_audio when no destination is provided.] <br>

## Skill Version(s): <br>
1.1.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
