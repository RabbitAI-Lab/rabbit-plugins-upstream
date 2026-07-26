## Description: <br>
Translate one subtitle file at a time with deterministic local parsing, timeline preservation, strict batch mapping, and safe output composition. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lumen01](https://clawhub.ai/user/lumen01) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agent operators use this skill to translate SRT, WebVTT/VTT, and ASS subtitle files while preserving timing and supported subtitle structure. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Subtitle text is sent to the agent's selected translation model, which may be inappropriate for confidential media. <br>
Mitigation: Use the skill only with subtitle content approved for that model path, and avoid confidential subtitle files unless the model handling is acceptable. <br>
Risk: Shared installations and optional symlinks can expose the skill to multiple agent runtimes or overwrite an existing local setup. <br>
Mitigation: Review installation destinations and symlinks before installing or sharing the skill across runtimes. <br>
Risk: Invalid translation responses can break subtitle mapping, hard line breaks, or ASS style markers. <br>
Mitigation: Validate every batch response, retry structural errors, and stop when required IDs, wrappers, BR markers, or fixed-structure markers still mismatch. <br>
Risk: Some ASS karaoke timing or unresolved inline style markers may be degraded to static text. <br>
Mitigation: Report karaoke degradations and inline-style fallback IDs from the final report so users understand any formatting loss. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lumen01/skills/agent-subtitle-translator) <br>
- [README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated subtitle/report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes one subtitle file per run; generated batches contain stable IDs and subtitle text, not timelines or raw ASS override tags.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
