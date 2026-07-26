## Description: <br>
Use CodexBar CLI local cost usage to summarize per-model usage for Codex or Claude, including the current most recent model or a full model breakdown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to summarize local CodexBar cost logs by model for Codex or Claude, either for the current model or for all models in the available cost history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: CodexBar reads local Codex or Claude session logs to compute costs. <br>
Mitigation: Install and run the skill only where local usage logs may be processed for cost reporting, and review CodexBar separately if local log privacy requirements are strict. <br>
Risk: Model-level values are cost-only because CodexBar output does not split token counts by model. <br>
Mitigation: Use the reported model costs for cost review, and avoid presenting them as per-model token accounting. <br>
Risk: The bundled installation metadata targets macOS with CodexBar available through a Homebrew cask. <br>
Mitigation: Confirm CodexBar CLI availability before use, especially on non-macOS systems. <br>


## Reference(s): <br>
- [CodexBar CLI quick ref](references/codexbar-cli.md) <br>
- [Model Usage skill listing](https://clawhub.ai/steipete/skills/model-usage) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Plain text or JSON summaries, with Markdown guidance and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports cost-only per-model summaries; token counts are not split by model in CodexBar output.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
