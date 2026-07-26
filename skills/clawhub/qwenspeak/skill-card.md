## Description: <br>
Text-to-speech generation via Qwen3-TTS over SSH, including preset voices, voice cloning, and voice design. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to generate speech audio, manage QwenSpeak TTS jobs, and work with preset, designed, or consented cloned voices through a trusted SSH-accessible QwenSpeak server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Text, YAML job files, uploaded reference audio, and downloaded audio pass through the configured SSH server. <br>
Mitigation: Use only a QWENSPEAK_HOST and QWENSPEAK_PORT that point to a server you operate or explicitly trust. <br>
Risk: Voice cloning can misuse biometric voice data or enable impersonation when reference audio lacks consent. <br>
Mitigation: Clone only voices with explicit permission, ask when provenance is unclear, and refuse impersonation, fraud, harassment, or deceptive synthetic-media requests. <br>
Risk: The optional server installer runs with elevated privileges. <br>
Mitigation: Pin the installer to a released tag, review it before execution, and avoid piping a mutable branch directly into a root shell. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/qwenspeak) <br>
- [Publisher profile](https://clawhub.ai/user/psyb0t) <br>
- [docker-qwenspeak](https://github.com/psyb0t/docker-qwenspeak) <br>
- [setup.md](references/setup.md) <br>
- [docker-lockbox](https://github.com/psyb0t/docker-lockbox) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with YAML examples and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces job instructions and wrapper commands for remote TTS generation; generated audio is retrieved through the configured SSH server.] <br>

## Skill Version(s): <br>
1.5.2 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
