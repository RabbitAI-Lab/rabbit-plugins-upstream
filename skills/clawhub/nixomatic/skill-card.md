## Description: <br>
Run software on demand through Nixomatic-generated Nix environments without permanently installing tools on the current system. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ereslibre](https://clawhub.ai/user/ereslibre) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to run missing tools, language runtimes, build utilities, and project workflows through Nix or Docker-backed Nixomatic environments. It can also document a reproducible development environment in a project README after successful use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill directs agents to fetch remote Nix flakes from nixomatic.com and accept flake-provided configuration. <br>
Mitigation: Require explicit approval before running generated Nix or Docker commands in sensitive repositories, production codebases, or environments with secrets. <br>
Risk: The skill may mutate project README.md files to record a Development Environment section. <br>
Mitigation: Review proposed README changes before keeping or publishing them. <br>
Risk: Running tools against the current workspace can expose or modify project files through the selected runtime. <br>
Mitigation: Avoid use in repositories containing secrets unless the workspace has been reviewed and commands are scoped to safe files. <br>


## Reference(s): <br>
- [Nixomatic](https://nixomatic.com) <br>
- [nixpkgs Package Search](https://search.nixos.org/packages) <br>
- [Source Repository](https://github.com/ereslibre/homelab/tree/main/dotfiles/assets/hermes/skills/nixomatic) <br>
- [ClawHub Skill Page](https://clawhub.ai/ereslibre/skills/nixomatic) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, shell commands, configuration, markdown, guidance] <br>
**Output Format:** [Markdown guidance with shell command blocks and optional README content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or update a Development Environment section with a Nixomatic URL after a successful project workflow.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
