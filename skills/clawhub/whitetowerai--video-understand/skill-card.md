## Description:

Use when a video project needs reusable media metadata, word-level transcription, objective speech analysis, or evidence-backed semantic understanding before optional editing skills run.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whitetowerai](https://clawhub.ai/user/whitetowerai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video workflow agents use this skill to build a reusable evidence layer for video projects, including media facts, word-level transcripts, speech analysis, and human-reviewed semantic understanding before downstream editing skills run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled render helpers can create final video outputs and mark a project render as verified.

Mitigation: Review the render plan and project status changes before running render_project.py, and run the skill only inside a dedicated video project workspace.

Risk: Local ffmpeg, ffprobe, Python, and transcription workflows process media files and write project artifacts.

Mitigation: Limit filesystem access to the intended project directory and keep source media, cache files, and generated review outputs in that workspace.

## Reference(s):

- [Project Schema V1](artifact/reference/project-schema.md)
- [Timeline Schema V1](artifact/reference/timeline-schema.md)
- [Understanding Schema V1](artifact/reference/understanding-schema.md)
- [Understanding Example](artifact/examples/understanding.example.json)
- [ClawHub Skill Page](https://clawhub.ai/whitetowerai/skills/video-understand)
- [ClawHub Publisher Profile](https://clawhub.ai/user/whitetowerai)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text, markdown, code]

**Output Format:** [Markdown guidance with shell commands and JSON schema-backed project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local video project evidence such as media metadata, transcripts, analysis JSON, semantic understanding JSON, review summaries, SRT captions, and contact sheets.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
