## Description: <br>
Use when a video project needs reusable media metadata, word-level transcription, objective speech analysis, or evidence-backed semantic understanding before optional editing skills run. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[whitetowerai](https://clawhub.ai/user/whitetowerai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and video workflow agents use this skill to build a reusable evidence layer for source media, including media facts, word-level transcript data, objective speech metrics, semantic understanding, and review artifacts before downstream editing skills run. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package can run local media-processing commands and write within a project directory. <br>
Mitigation: Use it in a dedicated project folder and review commands before execution. <br>
Risk: Included rendering code can create final media and modify project state. <br>
Mitigation: Do not let an agent run render_project.py or generated render plans unless you intend to create or overwrite final delivery files. <br>
Risk: The security verdict is suspicious because the main understanding workflow is local and coherent, but rendering behavior is under-documented. <br>
Mitigation: Limit normal use to the documented video-understanding workflow and review the included rendering path separately before deployment. <br>


## Reference(s): <br>
- [Project Schema V1](reference/project-schema.md) <br>
- [Timeline Schema V1](reference/timeline-schema.md) <br>
- [Understanding Schema V1](reference/understanding-schema.md) <br>
- [Understanding Example](examples/understanding.example.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Media review artifacts] <br>
**Output Format:** [Markdown guidance with shell commands plus JSON, SRT, JPEG, and project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates project-local work, review, input, final, and cache directories; durable machine outputs are kept under work/understand.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
