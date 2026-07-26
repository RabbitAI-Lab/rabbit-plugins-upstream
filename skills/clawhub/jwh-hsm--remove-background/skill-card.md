## Description: <br>
Remove single-color light backgrounds from images and output transparent PNG files using a luminance threshold. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jwh-hsm](https://clawhub.ai/user/jwh-hsm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creators can use this skill to convert local images with uniform light backgrounds into transparent PNG assets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill automatically opens the generated image in the system viewer after writing it. <br>
Mitigation: Review before installing if automatic local application launch is not desired, or remove/disable the auto-open block before use. <br>
Risk: Threshold-based background removal works best on uniform light backgrounds and may remove intended bright pixels. <br>
Mitigation: Run on trusted local inputs, inspect the generated PNG, and adjust the threshold when the background is not pure white. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jwh-hsm/remove-background) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Guidance] <br>
**Output Format:** [Transparent PNG file plus command-line status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses input path, output PNG path, and an optional brightness threshold.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
