## Description: <br>
Use when a video project needs reusable media metadata, word-level transcription, objective speech analysis, or evidence-backed semantic understanding before optional editing skills run. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[whitetowerai](https://clawhub.ai/user/whitetowerai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and video-production agents use this skill to build a shared evidence layer before downstream editing skills run. It initializes a video project, extracts media metadata and transcripts, produces objective speech analysis, and records factual semantic understanding in source time. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags under-disclosed rendering and export capability beyond the stated analysis workflow. <br>
Mitigation: Review any invocation of bundled render scripts before execution, especially when they can create final videos or change project status. <br>
Risk: The skill reads and writes local video project files and creates cache or model files during media processing. <br>
Mitigation: Run it in a dedicated project workspace and inspect generated evidence, transcript, review, and final-output files before relying on them. <br>


## Reference(s): <br>
- [Project Schema V1](artifact/reference/project-schema.md) <br>
- [Timeline Schema V1](artifact/reference/timeline-schema.md) <br>
- [Understanding Schema V1](artifact/reference/understanding-schema.md) <br>
- [Understanding Example](artifact/examples/understanding.example.json) <br>
- [ClawHub Skill Page](https://clawhub.ai/whitetowerai/skills/video-understand) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON project artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local video-project evidence files, review artifacts, transcripts, analysis JSON, and validation guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
