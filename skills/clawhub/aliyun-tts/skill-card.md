## Description: <br>
Alibaba Cloud Text-to-Speech synthesis service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[guang384](https://clawhub.ai/user/guang384) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to synthesize text into Alibaba Cloud TTS audio and provide voice replies from generated audio files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends synthesized text to Alibaba Cloud and requires Aliyun credentials. <br>
Mitigation: Use a restricted Aliyun key and avoid sending sensitive or regulated text. <br>
Risk: Server security guidance notes an unencrypted token request that should be reviewed before production use. <br>
Mitigation: Patch or verify the token request uses HTTPS before deploying in production. <br>
Risk: The skill writes generated audio to caller-selected paths. <br>
Mitigation: Choose output paths deliberately and review generated files before sharing or attaching them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/guang384/skills/aliyun-tts) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Files, Guidance] <br>
**Output Format:** [CLI command output and generated audio file path] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes audio to a user-specified output path; default format is MP3 at 16000 Hz.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
