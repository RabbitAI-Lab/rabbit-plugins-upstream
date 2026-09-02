## Description:

基于已注册实验的真实产物撰写中英实验报告；use when producing a lab report, design record, reproducibility package, or formal HTML/PDF output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yxy050208](https://clawhub.ai/user/yxy050208)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, students, and lab-report authors use this skill to produce bilingual Multisim lab reports, design records, reproducibility packages, or formal HTML/PDF outputs from registered experiment artifacts. The skill emphasizes traceable evidence, measured summaries, verification results, and approved export tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent could include measurements, PASS/FAIL results, file paths, or artifacts that are not supported by registered Multisim evidence.

Mitigation: Use only registered experiment artifacts, tool-returned local file references, and verification evidence; mark unsupported metrics as unverified.

Risk: The agent could export reports or artifacts outside the approved Multisim export controls.

Mitigation: Use formal export tools only when requested and do not bypass the approved export root.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yxy050208/skills/multisim-write-lab-report)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Bilingual Markdown-style lab report content, with formal HTML/PDF export when requested through approved tools.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SHA-256 references for reproducibility artifacts and PASS/FAIL statements tied to verification evidence.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
