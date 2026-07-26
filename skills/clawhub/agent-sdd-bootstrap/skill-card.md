## Description: <br>
Helps developers initialize an OpenSpec/SDD workflow in a project by installing and validating OpenSpec, creating project configuration, capturing project context, and bridging generated SDD files into supported or unsupported agent CLIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nieen](https://clawhub.ai/user/nieen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to bootstrap Spec-Driven Development with OpenSpec in an existing git repository, configure project context, and connect OpenSpec-generated workflows to agent CLI tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can install a global npm package. <br>
Mitigation: Review the install command and package source before execution, and pin or approve the package version when the environment requires controlled dependencies. <br>
Risk: The workflow can overwrite or create project-level OpenSpec and agent configuration files. <br>
Mitigation: Review or commit current changes before running initialization, then inspect the resulting diff before continuing. <br>
Risk: Mirroring generated files into unsupported agent CLIs may require tool-specific format adaptation. <br>
Mitigation: Check the target agent's skill and command schema after copying files and validate the resulting slash commands in the target tool. <br>


## Reference(s): <br>
- [PowerShell command reference](references/powershell.md) <br>
- [OpenSpec GitHub](https://github.com/Fission-AI/OpenSpec) <br>
- [OpenSpec npm package](https://www.npmjs.com/package/@fission-ai/openspec) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline bash, PowerShell, YAML, and Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose global npm installation and project-level OpenSpec or agent CLI configuration changes.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
