## Description: <br>
Turn a source image or multi-color mask image into a 3D-printable bas-relief STL by mapping colors or grayscale values to heights. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ajmwagar](https://clawhub.ai/user/ajmwagar) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, makers, and agent workflows use this skill to convert generated or supplied flat-color and grayscale images into printable bas-relief STL files. It is suited for deterministic local conversion where color or brightness maps directly to model height. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional preview path can execute unintended Python code from a specially crafted input filename. <br>
Mitigation: Avoid using --preview-svg with filenames from untrusted sources or unusual characters until heredoc interpolation is fixed. <br>
Risk: First use downloads Pillow into a cached local virtual environment. <br>
Mitigation: Review dependency installation behavior before use in restricted or production environments. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ajmwagar/skills/image-to-relief-stl) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [image_to_relief.py](artifact/scripts/image_to_relief.py) <br>
- [image_to_relief.sh](artifact/scripts/image_to_relief.sh) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration] <br>
**Output Format:** [ASCII STL file with optional SVG preview] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 for conversion; optional preview requires potrace and mkbitmap; first use installs Pillow into a cached local virtual environment.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
