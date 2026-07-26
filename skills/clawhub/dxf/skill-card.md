## Description: <br>
Generate, regenerate, and validate 2D DXF drawings from Python ezdxf sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liubuq-sys](https://clawhub.ai/user/liubuq-sys) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to create or modify 2D DXF drawings from natural-language requirements or CAD geometry, generate checked .dxf artifacts, and report deterministic validation results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Python generator targets are executable code. <br>
Mitigation: Review or create gen_dxf()/gen_step() files yourself, avoid generator files from untrusted repositories, and use a sandbox for unfamiliar designs. <br>
Risk: DXF generation writes artifacts to target output paths. <br>
Mitigation: Check source and output paths before generation, and run the tool only on explicit Python source targets. <br>
Risk: Dependency behavior can change across environments. <br>
Mitigation: Consider pinning ezdxf and related CAD dependencies for repeatable generation and validation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/liubuq-sys/skills/dxf) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated .dxf files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports explicit output paths, validation checks that ran, assumptions, and viewer links when available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
