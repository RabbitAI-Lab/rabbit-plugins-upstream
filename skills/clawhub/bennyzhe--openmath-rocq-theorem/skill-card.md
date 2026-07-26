## Description: <br>
Configures Rocq environments, runs preflight checks, and guides the proving workflow for OpenMath Rocq theorems. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bennyzhe](https://clawhub.ai/user/bennyzhe) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to prepare a Rocq theorem workspace, check local Rocq/dune/opam tooling, complete OpenMath theorem proofs, and verify proofs before submission. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Running dependency or build commands in the wrong workspace can affect an unintended Rocq project. <br>
Mitigation: Run the skill only in the intended OpenMath theorem workspace and confirm the active opam switch before installing dependencies or building. <br>
Risk: Project opam files may introduce unfamiliar dependencies. <br>
Mitigation: Review the project opam file before running dependency installation, and prefer an isolated opam switch for unfamiliar projects. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/bennyzhe/openmath-rocq-theorem) <br>
- [Rocq Companion Skills](references/companions.md) <br>
- [Rocq Language Specification](references/languages.md) <br>
- [OpenMath Rocq Proof Playbook](references/proof_playbook.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides local theorem-workspace checks and proof verification; it does not install bundled companion skills.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter lists v1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
