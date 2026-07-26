## Description: <br>
Create RFQ-ready 2D DXF files and optional SVG previews from strict, validated JSON design specs derived from natural-language part requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ajmwagar](https://clawhub.ai/user/ajmwagar) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, fabrication engineers, and external coding agents use this skill to turn sheet or plate part requests into validated JSON specs and deterministic DXF/SVG outputs for RFQs, previews, and manufacturing review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated CAD geometry may contain incorrect dimensions or design intent for a quote or fabrication workflow. <br>
Mitigation: Review generated dimensions, units, layers, and geometry before using the files for RFQs or fabrication. <br>
Risk: The local renderer can create or overwrite DXF/SVG files in the selected output directory. <br>
Mitigation: Run the tool in a dedicated output directory and inspect generated filenames before keeping or sharing the files. <br>
Risk: The v0 schema does not cover kerf compensation, bend lines, STEP/STL output, or full geometric self-intersection checks. <br>
Mitigation: Treat outputs as 2D RFQ drafts and apply shop-specific CAD/CAM validation for production use. <br>


## Reference(s): <br>
- [Create Dxf on ClawHub](https://clawhub.ai/ajmwagar/skills/create-dxf) <br>
- [Spec Schema](artifact/references/spec_schema.md) <br>
- [Test Prompts](artifact/references/test_prompts.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, configuration, shell commands, files] <br>
**Output Format:** [Markdown guidance with JSON specs and bash commands; generated DXF and SVG files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a strict JSON design spec; generated dimensions and geometry should be reviewed before quoting or fabrication.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
