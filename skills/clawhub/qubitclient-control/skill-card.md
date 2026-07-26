## Description: <br>
Qubitclient Control helps agents draft Python-based control workflows for quantum measurement tasks such as S21 spectroscopy, Rabi and Ramsey experiments, T1/T2 characterization, DRAG calibration, pulse optimization, power shift analysis, single-shot readout, and 2D spectrum acquisition. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yaqiangsun](https://clawhub.ai/user/yaqiangsun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and laboratory engineers can use this skill to ask an agent for qubit measurement control examples, parameter structures, and workflow guidance for QubitClient and MCP-based experiment tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent-generated experiment workflows may trigger parameter sweeps or measurement tasks against connected lab systems. <br>
Mitigation: Install and use the skill only with a trusted MCP server scoped to approved measurement tasks, and review server-side permissions before execution. <br>
Risk: Incorrect or unreviewed measurement parameters could affect hardware safety controls or produce invalid experiment results. <br>
Mitigation: Review proposed qubits, sweeps, pulse settings, and hardware safety controls with qualified lab personnel before running experiments. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/yaqiangsun/QubitClient/tree/main/skills/qubitclient-control) <br>
- [ClawHub skill page](https://clawhub.ai/yaqiangsun/skills/qubitclient-control) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown with Python code examples and parameter tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are guidance and examples for agent-assisted use; execution depends on the user's trusted QubitClient and MCP environment.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
