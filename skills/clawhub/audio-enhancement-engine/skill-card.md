## Description: <br>
Local audio enhancement and repair skill that routes common audio files or folders through VoiceFixer, AudioSR, or Resemble-Enhance workflows for denoising, speech repair, high-fidelity super-resolution, and WAV output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangminrui2022](https://clawhub.ai/user/wangminrui2022) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to enhance, denoise, repair, or upsample individual audio files and audio folders with local command-line workflows. It is intended for speech, meeting recordings, podcasts, older recordings, music, and other supported audio formats. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may download models, binaries, and third-party packages during use. <br>
Mitigation: Run it only in an isolated environment after reviewing dependency sources and network access expectations. <br>
Risk: The skill may create or modify a Python virtual environment and install or force-reinstall many packages. <br>
Mitigation: Use a dedicated virtual environment or container, and avoid running it in a shared production Python environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wangminrui2022/skills/audio-enhancement-engine) <br>
- [AudioSR project](https://github.com/haoheliu/versatile_audio_super_resolution.git) <br>
- [VoiceFixer project](https://github.com/haoheliu/voicefixer.git) <br>
- [Resemble Enhance PyPI package](https://pypi.org/project/resemble-enhance/) <br>
- [Resemble Enhance Hugging Face Space](https://huggingface.co/spaces/ResembleAI/resemble-enhance) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and WAV audio file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports single-file and directory batch processing; output audio is written as WAV files.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
