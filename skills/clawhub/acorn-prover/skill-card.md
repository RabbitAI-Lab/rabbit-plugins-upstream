## Description: <br>
Verify and write Acorn proof files for mathematical and cryptographic formalization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flyingnobita](https://clawhub.ai/user/flyingnobita) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to set up local Acorn paths, write or edit .ac proof files, run verification and reverification, and generate Acorn training data or documentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided Acorn library and project paths can become shell code when the generated config is sourced. <br>
Mitigation: Use only simple trusted directory paths for ACORN_LIB and ACORN_PROJECT; avoid spaces, dollar signs, backticks, semicolons, and newlines until setup safely quotes config values. <br>


## Reference(s): <br>
- [Acorn Syntax Reference](references/syntax.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/flyingnobita/skills/acorn-prover) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Acorn code snippets and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write a local config.env via setup.sh when the user supplies trusted Acorn paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
