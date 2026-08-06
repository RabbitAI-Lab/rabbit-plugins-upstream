## Description: <br>
Generates Makefiles with testing, linting, formatting, and automation targets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create or update standard Makefiles for Python, Rust, or TypeScript projects with common install, lint, format, typecheck, test, build, clean, and publish targets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated Makefile targets such as publish, deploy, clean, or install can change environments, delete files, or publish artifacts if run without review. <br>
Mitigation: Review generated targets before running them and use help or dry-run workflows where available. <br>
Risk: Standard Makefile templates may not fit projects with complex or exclusive alternative build systems. <br>
Mitigation: Use the skill only for Makefile-related changes and adapt generated targets to the project's established build workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-makefile-generation) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Makefile snippets and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated Makefile targets should be reviewed before use, especially publish, deploy, clean, or install targets.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
