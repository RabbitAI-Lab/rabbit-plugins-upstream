## Description: <br>
Vox helps an agent use the installed Vox CLI to transcribe exactly one user-specified URL or local audio/video file, with explicit boundaries for authentication, installation, file access, and output handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[casatwy](https://clawhub.ai/user/casatwy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users invoke this skill when they want an agent to use the Vox CLI for a single authorized transcription request, CLI status check, authentication flow, troubleshooting step, or skill installation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Transcribing a local file or URL may send media content to Vox. <br>
Mitigation: Confirm that the current user explicitly authorized exactly one submitted URL or one exact local media file path before invoking the CLI. <br>
Risk: Authentication uses a Vox API key. <br>
Mitigation: Use the CLI's status and login flow, let the hidden prompt read the key, and never print or store API keys, cookies, signed URLs, secret query parameters, or private payloads. <br>
Risk: Installing or upgrading the Vox CLI changes local tooling. <br>
Mitigation: Ask before installing or upgrading, require CLI version 0.1.0 or newer, and verify that the expected auth, transcribe, and skill commands are present. <br>
Risk: Output writes could overwrite files or expose transcript content. <br>
Mitigation: Write to a destination only when explicitly requested, preserve the CLI's no-clobber behavior, and otherwise keep transcript or result bytes on stdout. <br>


## Reference(s): <br>
- [ClawHub Vox skill page](https://clawhub.ai/casatwy/skills/vox) <br>
- [Vox API key page](https://vox.reka.cc/me/api-keys) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands and transcript output handling] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Preserves SRT, VTT, JSON, JSONL, and explicitly requested raw text exactly; writes output files only when the user explicitly requests a destination.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release evidence and manifest.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
