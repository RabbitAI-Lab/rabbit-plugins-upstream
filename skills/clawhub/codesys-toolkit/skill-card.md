## Description: <br>
Automates CODESYS/InoProShop PLC project generation, POU export and patching, compilation checks, PLC device enumeration, and error dialog monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and PLC engineers use this skill to automate Windows-based CODESYS/InoProShop workflows, including creating projects from templates, exporting or patching POU/GVL/DUT source, checking compilation, and listing supported device models. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automation can terminate active InoProShop sessions, which may affect unsaved engineering work. <br>
Mitigation: Save or close active sessions before running automation, and use -NoKill when an existing InoProShop session may contain unsaved work. <br>
Risk: Export, patch, generate, and compile-check workflows can overwrite or modify PLC project and workspace files from configurable paths. <br>
Mitigation: Use backed-up or version-controlled project workspaces and verify env.json paths, including workspace_dir, template, and patch_target, before running those workflows. <br>
Risk: Unexpected launcher targets or paths could run unintended automation in a PLC engineering environment. <br>
Mitigation: Prefer fixed launcher aliases over arbitrary script paths and review the selected command before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/codesys-toolkit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline PowerShell, JSON configuration, and Structured Text code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are advisory instructions and command examples for Windows-based CODESYS/InoProShop workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
