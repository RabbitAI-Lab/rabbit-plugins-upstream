## Description: <br>
Quantum experiment numerical curve fitting and parameter extraction for S21 peak detection, pi-pulse calibration, Rabi and Ramsey analysis, T1/T2 fitting, DRAG optimization, benchmarking, and related QubitScopeClient workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yaqiangsun](https://clawhub.ai/user/yaqiangsun) <br>

### License/Terms of Use: <br>
GPL-3.0 <br>


## Use Case: <br>
Developers and quantum engineers use this skill to prepare QubitScopeClient requests, understand supported experiment data shapes, and interpret curve-fitting outputs for quantum calibration and analysis tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Quantum experiment data may be proprietary or sensitive if sent through QubitScopeClient. <br>
Mitigation: Review the underlying qubitclient package or service and data-handling requirements before using proprietary datasets. <br>
Risk: Curve-fitting results can be invalid or low confidence for unsuitable input data. <br>
Mitigation: Check returned status, confidence scores, and R2 values, and validate fits against source measurements before acting on extracted parameters. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/yaqiangsun/QubitClient/tree/main/skills/qubitclient-scope) <br>
- [ClawHub skill page](https://clawhub.ai/yaqiangsun/skills/qubitclient-scope) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Configuration] <br>
**Output Format:** [Markdown with Python and JSON code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Describes task-specific input schemas and result objects containing fit parameters, confidence scores, fitted data, and status values.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
