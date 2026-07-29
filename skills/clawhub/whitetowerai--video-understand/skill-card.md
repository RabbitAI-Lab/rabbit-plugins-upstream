## Description: <br>
Use when a video project needs reusable media metadata, word-level transcription, objective speech analysis, or evidence-backed semantic understanding before optional editing skills run. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[whitetowerai](https://clawhub.ai/user/whitetowerai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and video workflow agents use this skill to initialize a video project, collect media metadata, transcribe speech, generate objective analysis, and prepare human-reviewed semantic evidence before downstream editing skills run. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled rendering and render-plan tools can generate final media and update project state. <br>
Mitigation: Review project plans and generated artifacts before running rendering tools, especially for untrusted projects. <br>
Risk: The skill requires local shell and file-write access for video project processing. <br>
Mitigation: Run it only in a project workspace where local media files and generated outputs are expected. <br>


## Reference(s): <br>
- [video-understand ClawHub Page](https://clawhub.ai/whitetowerai/skills/video-understand) <br>
- [Project Schema V1](reference/project-schema.md) <br>
- [Timeline Schema V1](reference/timeline-schema.md) <br>
- [Understanding Schema V1](reference/understanding-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON project artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local video-understanding project files, transcript data, semantic evidence, validation reports, and review artifacts.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
