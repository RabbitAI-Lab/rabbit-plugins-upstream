## Description: <br>
Automates a six-step local workflow that downloads Douyin or Bilibili short videos, extracts audio and vocals, transcribes speech, corrects text, and restores punctuation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangminrui2022](https://clawhub.ai/user/wangminrui2022) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, content operators, and OpenClaw users use this skill to turn a short-video URL or local media folder into extracted audio, clean vocals, transcripts, corrected text, and punctuated final text. It supports full end-to-end processing or resume from a specific workflow step. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow downloads and processes third-party short-video content. <br>
Mitigation: Use only content you have rights to process, and verify privacy obligations before downloading or transcribing media. <br>
Risk: The skill runs local Python helpers and depends on companion skills or helper scripts. <br>
Mitigation: Install it only for an intended local download/transcription pipeline, and review missing or mismatched helper-script references before relying on dependable operation. <br>
Risk: The workflow writes downloaded media, audio, transcripts, and final text to local output directories. <br>
Mitigation: Use explicit input URLs and output directories, then inspect generated files before reuse or publication. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wangminrui2022/skills/short-video-content-replicator) <br>
- [Publisher profile](https://clawhub.ai/user/wangminrui2022) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated local media and text files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates videos, mp3, vocals, transcripts, corrected, and final output directories; supports start-from step1 through step6.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
