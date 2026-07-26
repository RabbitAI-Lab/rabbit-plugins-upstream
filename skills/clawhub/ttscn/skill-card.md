## Description: <br>
TtsCN helps agents generate Chinese text-to-speech audio through eight cloud and local-provider backends, with provider comparison guidance, command examples, JSON-friendly CLI output, and optional voice cloning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agents365-ai](https://clawhub.ai/user/agents365-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, content creators, and agent operators use this skill to choose a Chinese TTS backend and synthesize narration, voiceover, audiobook, podcast, or other speech audio from text or text files. Agents can also inspect provider capabilities, run dry runs, emit structured JSON results, and manage supported voice-cloning workflows when the user has the required rights and credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Synthesis text and clone reference audio may be sent to the selected TTS provider. <br>
Mitigation: Use only providers whose data handling is acceptable for the content, and avoid submitting sensitive text or audio unless the provider terms and account configuration permit it. <br>
Risk: Voice cloning can misuse a person's voice or violate provider terms. <br>
Mitigation: Clone only voices owned by the user or explicitly authorized by the rights holder, and keep evidence of consent for cloned voices. <br>
Risk: MiniMax voice cloning can incur charges and temporary clones may expire if not used. <br>
Mitigation: Require explicit user confirmation before paid clone creation and explain the provider's retention window before proceeding. <br>
Risk: Generated audio can overwrite an existing output file. <br>
Mitigation: Choose output paths deliberately, prefer new filenames for important work, and confirm before writing to a path that may already contain useful audio. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/agents365-ai/skills/ttscn) <br>
- [Provider comparison guide](docs/providers.md) <br>
- [Provider comparison page](docs/providers.html) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text, JSON, files] <br>
**Output Format:** [Markdown guidance with bash examples, terminal text or JSON CLI envelopes, and generated WAV or MP3 audio files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and ffmpeg; non-default providers may require API keys, provider packages, and user-selected output paths.] <br>

## Skill Version(s): <br>
1.3.2 (source: server release metadata, SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
