## Description: <br>
Scaffolds new projects with git, CI/CD workflows, pre-commit hooks, and build configuration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to initialize or update Python, Rust, and TypeScript projects with common development infrastructure, including git setup, CI workflows, pre-commit hooks, Makefile targets, and build configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or update project scaffolding files in the working directory. <br>
Mitigation: Review proposed file changes and overwrite prompts before accepting them. <br>
Risk: The workflow references an external attune plugin script for template rendering. <br>
Mitigation: Verify the plugin script and installation source before running it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-project-init) <br>
- [Attune plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or create project scaffolding files after user review.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
