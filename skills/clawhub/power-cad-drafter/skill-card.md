## Description: <br>
Auto-generate electrical CAD drawings from survey data and auto-audit against power codes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[powerzzjohn](https://clawhub.ai/user/powerzzjohn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Electrical designers and project engineers use this skill to turn survey data, sketches, or design briefs into draft DXF construction drawings for 10kV-and-below power distribution projects and to generate code-check audit reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated CAD drawings and audit reports may be incomplete or incorrect if survey inputs, inferred parameters, or local code assumptions are wrong. <br>
Mitigation: Treat outputs as draft engineering assistance and require qualified professional review before construction or compliance decisions. <br>
Risk: The scripts write CAD and audit files to user-supplied or default output paths, which could overwrite existing work. <br>
Mitigation: Use explicit project output directories and check for existing files before running the scripts. <br>
Risk: The skill depends on an external company design-code document being present in the workspace. <br>
Mitigation: Confirm the required code document is available and current before relying on audit results. <br>


## Reference(s): <br>
- [Drawing Symbols Reference](references/drawing_symbols.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python script usage; generated artifacts include DXF, JSON, Markdown, CSV, and ZIP files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces four DXF drawing sheets, inferred design parameters, an audit report with pass/fail and corrective actions, and an equipment list.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
