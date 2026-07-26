## Description: <br>
Generates complete songs from a user's voice sample, lyrics or theme, and style settings by coordinating voice cloning, lyric generation, music generation, and audio mixing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhaobod1](https://clawhub.ai/user/zhaobod1) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External creators, developers, and audio-production teams use this skill to prepare voice-cloned song generation workflows from consented voice samples, user lyrics or generated lyrics, and configurable music styles. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow handles sensitive voice samples and voice models that could be misused for unauthorized voice cloning. <br>
Mitigation: Use only voices the operator owns or has explicit permission to clone, document that consent, and require clear retention and deletion controls for uploaded samples and trained voice models. <br>
Risk: The deployment examples expose local services and include default JWT and MinIO secrets. <br>
Mitigation: Run the stack in an isolated environment, bind services to private interfaces, and replace all default JWT and MinIO credentials before any shared or production use. <br>
Risk: The workflow depends on external service containers and Python dependencies for audio and model processing. <br>
Mitigation: Inspect Docker images and dependency files before installation, avoid unreviewed custom requirements, and scan the environment before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhaobod1/skills/huo15-ai-music-composer) <br>
- [Quick Start](QUICK_START.md) <br>
- [Technical Specification](docs/technical-spec.md) <br>
- [API Reference](docs/api-reference.md) <br>
- [Extension Guide](docs/extension-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, Python and JSON snippets, API examples, and file-oriented workflow instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The described workflow can produce generated audio files, MIDI files, karaoke assets, job status JSON, and quality reports when backed by the required services.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
