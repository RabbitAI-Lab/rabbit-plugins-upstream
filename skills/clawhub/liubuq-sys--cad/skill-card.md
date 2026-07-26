## Description: <br>
Create, modify, inspect, and validate STEP-first parametric CAD parts and assemblies. Use for natural-language CAD specs, reference images, 2D technical drawings, STEP/STP generation or direct inspection, Python CAD source, source-level joints, selector references, geometry facts, measurements, mating deltas, snapshots, and secondary STL/3MF/native GLB outputs from CAD geometry. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liubuq-sys](https://clawhub.ai/user/liubuq-sys) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to turn CAD requirements, reference images, drawings, or existing STEP/STP files into validated STEP-first parametric parts and assemblies. It also guides inspection, measurement, snapshot review, and secondary STL, 3MF, or native GLB export workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Python CAD generator files processed by the skill can run unrestricted local code. <br>
Mitigation: Use CAD files and generator scripts that were authored or reviewed by a trusted party, and run third-party CAD work in an isolated workspace. <br>
Risk: Generated CAD may be dimensionally wrong or unsuitable for fit-critical, safety-critical, or compliance-bound use if requirements are incomplete. <br>
Mitigation: Review the CAD brief, run the prescribed inspection and measurement checks, and use snapshot review before relying on generated artifacts. <br>


## Reference(s): <br>
- [CAD brief](references/cad-brief.md) <br>
- [build123d modeling patterns](references/build123d-modeling.md) <br>
- [STEP generation](references/step-generation.md) <br>
- [Inspection and validation](references/inspection-and-validation.md) <br>
- [Snapshot review](references/snapshot-review.md) <br>
- [Positioning logic, joints, and mating](references/positioning.md) <br>
- [CAD parameters](references/parameters.md) <br>
- [Supported exports](references/supported-exports.md) <br>
- [Repair loop](references/repair-loop.md) <br>
- [ClawHub skill page](https://clawhub.ai/liubuq-sys/skills/cad) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CAD source code, shell commands, validation summaries, file paths, and snapshot or viewer handoff details when applicable] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces STEP-first CAD workflows; STL, 3MF, and native GLB are secondary outputs derived from validated CAD geometry.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
