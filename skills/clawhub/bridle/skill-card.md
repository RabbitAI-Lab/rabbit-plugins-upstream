## Description: <br>
Bridle is a unified configuration manager for AI coding assistants that manages profiles, installs skills, agents, commands, and MCPs, and switches configurations across Claude Code, OpenCode, Goose, and Amp. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bjesuiter](https://clawhub.ai/user/bjesuiter) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use Bridle to manage AI coding assistant profiles, install assistant components, and switch configurations across supported harnesses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing components from untrusted repositories can change assistant configuration files or install unwanted components. <br>
Mitigation: Use bridle install only with repositories you trust and review components before installing them. <br>
Risk: Force, uninstall, and delete operations can overwrite or remove existing assistant setup. <br>
Mitigation: Review the target profile or component before using --force, uninstall, or delete commands, and keep backups for important configurations. <br>
Risk: Switching profiles changes the active configuration for supported AI coding assistants. <br>
Mitigation: Check bridle status and inspect profile details before switching active profiles. <br>


## Reference(s): <br>
- [Bridle on ClawHub](https://clawhub.ai/bjesuiter/skills/bridle) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may emit human-readable text, JSON, or automatic TTY-aware output.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
