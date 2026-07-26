## Description: <br>
本地视频转文字 - 使用 OpenAI Whisper 进行语音识别，完全免费、离线运行、保护隐私 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaa2531349](https://clawhub.ai/user/aaa2531349) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and creators use this skill to transcribe local audio and video files into text, subtitles, and optional summary JSON. It is suited for meeting recordings, interviews, lectures, podcasts, and short-form media workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: First use may download and install unpinned Python packages and Whisper models, including from a third-party package mirror. <br>
Mitigation: Review before installing, prefer a virtual environment, install dependencies yourself where possible, and verify the package source before execution. <br>
Risk: Transcripts and summary files are saved beside the source media or in the selected output directory. <br>
Mitigation: Avoid running the skill on sensitive recordings in shared or synced folders unless saving transcript artifacts there is acceptable. <br>
Risk: The release makes strong offline and privacy claims while dependency and model installation may require network access on first use. <br>
Mitigation: Treat offline operation as applying after dependencies and models are installed, and document any network access required during setup. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaa2531349/video-transcribe) <br>
- [OpenAI Whisper](https://github.com/openai/whisper) <br>
- [Tsinghua PyPI mirror used by install command](https://pypi.tuna.tsinghua.edu.cn/simple) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Local transcript and subtitle files with console status output and optional summary JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces TXT, SRT, VTT, TSV, JSON, and optional summary JSON files in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata and SKILL.md changelog, released 2026-03-18) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
