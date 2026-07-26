## Description: <br>
A mathematical modeling competition agent that helps analyze contest problems, construct models, implement Python or MATLAB solvers, visualize results, and draft LaTeX-formatted CUMCM papers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tronmen](https://clawhub.ai/user/tronmen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Students, educators, and external users use this skill for math-modeling competition workflows, including problem analysis, data preparation, model design, solver code, validation, sensitivity analysis, visualization, and contest-paper drafting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill strongly defaults to full CUMCM-style paper generation, which may be more output than needed for partial modeling or code-only requests. <br>
Mitigation: Users should state when they want a partial answer, a non-Chinese response, or a different paper or template style. <br>
Risk: Generated modeling assumptions, results, solver code, and paper text may be incorrect or unsuitable for a specific contest submission. <br>
Mitigation: Review the mathematical reasoning, rerun code, validate results against provided data, and check contest formatting requirements before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tronmen/skills/mathmodel-master-full) <br>
- [README](README.md) <br>
- [Agent definition](agents/mathmodel-master.md) <br>
- [Modeling workflow skill](skills/modeling/SKILL.md) <br>
- [Common algorithms reference](skills/mathmodel-toolkit/references/common-algorithms.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with LaTeX, Python or MATLAB code blocks, formulas, tables, and file-oriented instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce full CUMCM-style paper drafts, solver code, visualization guidance, and compilation instructions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
