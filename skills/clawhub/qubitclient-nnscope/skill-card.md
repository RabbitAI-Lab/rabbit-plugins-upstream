## Description: <br>
NNScope provides neural network-based quantum spectrum analysis for S21 peak detection, multi-peak detection, spectrum peak region analysis, 2D curve segmentation, S21-vs-flux segmentation, power-shift segmentation, curve fitting, batch processing, and matplotlib/plotly visualization workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yaqiangsun](https://clawhub.ai/user/yaqiangsun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and quantum engineering teams use this skill to call QubitClient NNScope APIs for peak detection, curve segmentation, parameter extraction, confidence scoring, batch analysis, and visualization of 1D and 2D quantum spectrum data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow depends on the qubitclient package and spectrum data supplied by the user. <br>
Mitigation: Install and use qubitclient only from a trusted source, and confirm that the data handling is appropriate for the spectra being analyzed. <br>
Risk: Neural network-based peak detection and curve fitting can produce uncertain or incorrect results on unfamiliar spectrum data. <br>
Mitigation: Review confidence scores, inspect visualizations, and validate extracted parameters against domain checks before relying on the analysis. <br>


## Reference(s): <br>
- [Source repository](https://github.com/yaqiangsun/QubitClient/tree/main/skills/qubitclient-nnscope) <br>
- [ClawHub skill page](https://clawhub.ai/yaqiangsun/skills/qubitclient-nnscope) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Configuration] <br>
**Output Format:** [Markdown with Python code blocks and JSON-style response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes task names, input schemas, result fields, confidence thresholds, curve-fitting options, and visualization examples.] <br>

## Skill Version(s): <br>
0.1.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
