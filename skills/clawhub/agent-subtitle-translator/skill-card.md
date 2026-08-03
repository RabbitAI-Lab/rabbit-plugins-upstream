## Description: <br>
Translate SRT, VTT, and ASS subtitle files with local parsing, strict batch validation, timeline preservation, and safe output composition. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lumen01](https://clawhub.ai/user/lumen01) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to translate one subtitle file at a time while preserving timing, supported ASS structure, hard line breaks, and validation-safe subtitle mappings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The mandatory visualizer is an unauthenticated local persistent service. <br>
Mitigation: Keep the visualizer bound to 127.0.0.1 and do not expose it on remote or public interfaces. <br>
Risk: Network override paths can point the visualizer or bridge away from the default local endpoint. <br>
Mitigation: Avoid setting SUBTITLE_VISUALIZER_URL or SUBTITLE_VISUALIZER_HOST to remote addresses unless the deployment has reviewed and accepted that exposure. <br>
Risk: Retained visualizer task history can include subtitle contents or model/session metadata. <br>
Mitigation: Periodically clear ~/.agent-subtitle-translator/visualizer when subtitle content or session metadata is sensitive. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lumen01/skills/agent-subtitle-translator) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact skill instructions](artifact/SKILL.md) <br>
- [README documentation link](https://github.com/Lumen01/agent-subtitle-translator/blob/main/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Text, Files, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands, model prompt batches, translated subtitle files, and JSON reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes one subtitle file per run; batch prompts contain stable IDs and text while excluding timelines and raw ASS override tags.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
