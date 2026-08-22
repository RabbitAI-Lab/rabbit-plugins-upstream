## Description:

Modelagem parametrica e preparacao de pecas FDM para Bambu Lab A1 Combo, com STL/3MF, AMS Lite e validacao.

This skill is ready for commercial/non-commercial use.

## Publisher:

[serramos-hub](https://clawhub.ai/user/serramos-hub)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create parametric 3D-printable parts for Bambu Lab A1 Combo workflows. It guides requirements gathering, model construction, STL validation, material and tolerance choices, AMS Lite planning, and Bambu Studio handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated geometry or slicing guidance may be unsuitable for functional, structural, electrical, heat, food-contact, medical, or protective-use parts.

Mitigation: Review generated geometry and Bambu Studio slicing output before printing; prototype and measure critical fits before relying on a part.

Risk: The bundled STL audit is a limited local geometry check and does not certify printability, material suitability, or machine safety.

Mitigation: Use the STL audit and visual or slicer preview as checks, then confirm dimensions, orientation, supports, material, nozzle, plate, and profile in Bambu Studio.

Risk: Requests for weapons or components primarily intended to injure create unsafe downstream use.

Mitigation: Decline weapon modeling and keep safety warnings visible for sensitive applications.

## Reference(s):

- [Bambu Lab A1 Combo reference](artifact/references/bambu-a1.md)
- [Bambu Lab A1 Combo Quick Start](https://cdn1.bambulab.com/documentation/quick-start-b5f1a684f77/A1%20Combo%20Quick%20Start_V0%28EN%29.pdf)
- [Bambu Studio](https://github.com/bambulab/BambuStudio)
- [Bambu Studio Command Line Usage](https://github.com/bambulab/BambuStudio/wiki/Command-Line-Usage)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with CAD/modeling source snippets, inline shell commands, validation notes, and slicing/setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create parametric model sources, STL files, STEP files when supported, optional 3MF project files, and concise project notes.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
