## Description: <br>
Guides agents through installing and configuring OctoASR so OpenClaw can transcribe audio locally on Apple Silicon Macs and inject transcripts into chat context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lovejing0306](https://clawhub.ai/user/lovejing0306) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw operators use this skill to set up offline speech-to-text for audio messages on Apple Silicon Macs, including installation, service checks, model selection, and OpenClaw audio-tool configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing the skill workflow requires adding the Mininglamp-AI Homebrew tap and running a local transcription service. <br>
Mitigation: Install only after reviewing the tap and package source, and run OctoASR with normal local service controls such as status checks and logs. <br>
Risk: The optional OpenAI fallback means audio may be processed by a cloud provider when local transcription fails. <br>
Mitigation: Use the recommended local-only OpenClaw configuration for private audio, and enable cloud fallback only after confirming data-handling requirements. <br>


## Reference(s): <br>
- [OctoASR ClawHub Skill](https://clawhub.ai/lovejing0306/skills/octoasr) <br>
- [OctoASR Project](https://github.com/Mininglamp-AI/octoasr) <br>
- [OpenClaw Project](https://github.com/openclaw/openclaw) <br>
- [Homebrew](https://brew.sh) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with shell commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes local-only setup guidance and an optional cloud-fallback configuration example.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
