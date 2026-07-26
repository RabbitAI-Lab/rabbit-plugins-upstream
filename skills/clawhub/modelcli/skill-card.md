## Description: <br>
ModelCLI uses a local ModelCLI installation to run object detection, OCR, speech recognition, speech synthesis, model management, and diagnostics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[graysilver](https://clawhub.ai/user/graysilver) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to route image, audio, text-to-speech, model-management, and diagnostic requests through ModelCLI and return concise structured results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Normal use can automatically download and run an unpinned remote install script and can download missing models. <br>
Mitigation: Preinstall ModelCLI from a trusted source, set MODELCLI_BIN to that executable, and review any install script before allowing automatic bootstrap. <br>
Risk: Sensitive operations can overwrite outputs, refresh models, remove model data, or deeply load installed models. <br>
Mitigation: Require explicit user confirmation before using --approve-sensitive for overwrite, refresh, removal, cleanup, or deep diagnostic actions. <br>


## Reference(s): <br>
- [ModelCLI skill source](https://github.com/GraySilver/modelcli/tree/main/skills/modelcli) <br>
- [ModelCLI install script](https://raw.githubusercontent.com/GraySilver/modelcli/main/install.sh) <br>
- [ModelCLI command reference](references/commands.md) <br>
- [Agent JSON protocol and error handling](references/protocol.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and summarized JSON results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May report generated file paths, parsed ModelCLI result fields, retryable errors, and confirmation prompts for sensitive actions.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
