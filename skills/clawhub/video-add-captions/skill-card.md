## Description: <br>
Add word-timed captions to an Open Recut program by mapping the canonical transcript through timeline.json, reviewing maintained caption styles on source-backed pixels, rendering a local transparent HyperFrames PNG sequence, and registering it as an overlay contribution for the shared delivery render. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[whitetowerai](https://clawhub.ai/user/whitetowerai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and video workflow operators use this skill to add validated, word-timed captions to an Open Recut project. It supports style review, SRT generation, caption planning, and transparent overlay frame production for a shared delivery render. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs local media and rendering commands and modifies project caption, review, and overlay files. <br>
Mitigation: Use it only in trusted video project workspaces, inspect planned outputs, and review generated caption evidence before approving render contributions. <br>
Risk: The workflow depends on external rendering tooling, including npx hyperframes and Chrome handling. <br>
Mitigation: Verify the toolchain and package completeness in the execution environment before relying on the workflow for production work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/whitetowerai/skills/video-add-captions) <br>
- [Caption rules and data shape](artifact/reference/caption-rules.md) <br>
- [Caption style themes](artifact/reference/caption-style-themes.md) <br>
- [Caption feedback mapping](artifact/reference/caption-feedback-mapping.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands plus generated JSON, SRT, HTML review pages, and PNG overlay frames] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces project-local caption plans, review evidence, style approval receipts, and transparent caption overlay frames.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
