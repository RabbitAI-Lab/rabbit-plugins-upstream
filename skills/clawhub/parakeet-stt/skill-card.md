## Description: <br>
Local speech-to-text skill for transcribing audio files with NVIDIA Parakeet TDT 0.6B v3 through a local OpenAI-compatible API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carlulsoe](https://clawhub.ai/user/carlulsoe) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and users who need local transcription use this skill to configure and call a local Parakeet speech-to-text service for audio transcription, timestamps, and subtitle outputs without cloud APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Running the upstream service through Docker or Python can execute third-party dependencies on the local machine. <br>
Mitigation: Install only if comfortable running the upstream project and review its Docker or Python dependencies before use. <br>
Risk: Exposing the local transcription endpoint publicly could allow unintended access to audio processing. <br>
Mitigation: Keep PARAKEET_URL pointed at a trusted local server, avoid exposing the port publicly, and stop the Docker service when finished. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/carlulsoe/skills/parakeet-stt) <br>
- [Upstream Parakeet FastAPI OpenAI project](https://github.com/groxaxo/parakeet-tdt-0.6b-v3-fastapi-openai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell commands, Python snippets, API examples, and transcription response format guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses PARAKEET_URL to target the local service; supported response formats include text, JSON, verbose JSON, SRT, and VTT.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
