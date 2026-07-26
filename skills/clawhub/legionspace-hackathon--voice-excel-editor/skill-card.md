## Description: <br>
Voice Excel Editor turns an uploaded Excel workbook and Chinese voice instruction into structured worksheet edits, applies them to a copied workbook, and returns execution feedback and logs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to convert spoken Chinese Excel editing requests into structured worksheet operations, apply supported edits to a copied workbook, and receive the modified file with an execution log. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio instructions are sent to the external SenseAudio service. <br>
Mitigation: Confirm user consent before uploading audio and avoid using the skill with sensitive recordings unless the external service is approved. <br>
Risk: The skill can install Python dependencies at runtime and create modified copies of Excel workbooks. <br>
Mitigation: Run it in an isolated environment, review the generated operation plan before execution, and verify the modified workbook before relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/voice-excel-editor) <br>
- [Excel Operation Schema](references/operation_schema.md) <br>
- [Voice Excel Planning Prompt](references/planning_prompt.md) <br>
- [SenseAudio API endpoint](https://api.senseaudio.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, files, shell commands, guidance] <br>
**Output Format:** [Markdown response with file references, JSON operation and log artifacts, and a modified Excel workbook] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SENSEAUDIO_API_KEY; writes modified workbooks as separate output files rather than overwriting the original.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
