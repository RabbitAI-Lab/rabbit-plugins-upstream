## Description: <br>
Develop Noir (.nr) codebases. Use when creating a project or writing code with Noir. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jp4g](https://clawhub.ai/user/jp4g) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to create, validate, and maintain Noir projects, including compilation, witness generation, proving backend selection, proof generation, and verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated project changes or commands may introduce incorrect Noir behavior or misleading proof workflow guidance. <br>
Mitigation: Review generated changes before committing, run `nargo test`, and verify proving and verification steps against official Noir and backend documentation. <br>
Risk: Barretenberg tooling versions can drift from the local Noir toolchain. <br>
Mitigation: Install or update `bbup` and related tooling from official sources, use the toolchain-compatible Barretenberg version, and pin versions when reproducibility matters. <br>


## Reference(s): <br>
- [Noir Documentation](https://noir-lang.org/docs/) <br>
- [Noir GitHub Codespaces Setup](https://noir-lang.org/docs/tooling/devcontainer#using-github-codespaces) <br>
- [Barretenberg Documentation](https://barretenberg.aztec.network/docs/) <br>
- [Barretenberg Reference](references/barretenberg.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Noir source code, project scaffolding commands, test commands, and proving backend setup guidance.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
