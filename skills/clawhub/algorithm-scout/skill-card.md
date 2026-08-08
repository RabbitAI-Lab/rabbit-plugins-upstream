## Description: <br>
独创的智能优化算法推荐系统，根据问题特征精准推荐 WOA/GWO/SOA/GOA/MFO/BAS/CVX/波束形成等算法 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mama1234421](https://clawhub.ai/user/mama1234421) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to select optimization, convex optimization, and beamforming algorithms based on problem characteristics. It provides recommendation rationale, parameter suggestions, and pointers to local algorithm locations when available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill recommends algorithms from static reference material, so guidance may not fit every optimization problem or constraint set. <br>
Mitigation: Review the recommendation against the problem formulation, objective, constraints, dimensionality, and validation results before relying on it. <br>
Risk: The skill points to local algorithm paths that may not exist in the user's environment. <br>
Mitigation: Confirm referenced local paths and implementations are present before using path guidance. <br>


## Reference(s): <br>
- [Optimization algorithm library](references/algorithm_library.md) <br>
- [ClawHub skill page](https://clawhub.ai/mama1234421/skills/algorithm-scout) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown] <br>
**Output Format:** [Markdown guidance with algorithm recommendations, rationale, parameter suggestions, and local path references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; produces advisory recommendations rather than executable solver output.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
