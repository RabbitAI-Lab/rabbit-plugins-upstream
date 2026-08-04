## Description: <br>
Scaffolds new projects with git, CI/CD workflows, pre-commit hooks, and build config. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to initialize or standardize Python, Rust, and TypeScript projects with repository setup, CI/CD workflows, pre-commit hooks, Makefiles, and build configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated files and project configuration can overwrite or change existing local project files. <br>
Mitigation: Review proposed changes before accepting overwrites or committing generated files. <br>
Risk: Generated CI workflows, Makefiles, and pre-commit configuration can alter build, test, and automation behavior. <br>
Mitigation: Inspect generated automation files before enabling them in a repository. <br>
Risk: The referenced attune plugin or script is separate software from this skill artifact. <br>
Mitigation: Inspect the external plugin or script before installing or running it. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-attune-project-init) <br>
- [Attune Plugin Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local project scaffolding guidance and file-generation steps that should be reviewed before accepting overwrites.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
