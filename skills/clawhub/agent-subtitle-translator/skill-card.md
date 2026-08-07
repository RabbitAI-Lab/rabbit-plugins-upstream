## Description: <br>
Translates one SRT, VTT, or ASS subtitle file at a time with local timeline handling, strict ID validation, safe output composition, and an optional loopback-only visualizer. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lumen01](https://clawhub.ai/user/lumen01) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to translate a single subtitle file while preserving timing, supported ASS structure, and validation traceability. It is useful when an agent needs deterministic subtitle parsing, batched translation prompts, response validation, and final subtitle/report generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads the selected subtitle file and writes local work, output, and report files. <br>
Mitigation: Run it only on intended subtitle files, review generated paths before sharing outputs, and use overwrite flags only when replacement is intentional. <br>
Risk: The optional visualizer stores task history in the user's home directory, which can retain subtitle content on shared machines. <br>
Mitigation: Stop the visualizer after use and manually clear ~/.agent-subtitle-translator/visualizer when subtitle contents are sensitive. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lumen01/skills/agent-subtitle-translator) <br>
- [Server-resolved GitHub source](https://github.com/Lumen01/agent-subtitle-translator) <br>
- [Artifact README](README.md) <br>
- [Artifact skill instructions](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, files, guidance] <br>
**Output Format:** [Markdown progress updates plus generated subtitle and JSON report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes one selected subtitle file per run and reports validation, degradation, output path, format, encoding, entry count, and time range.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
