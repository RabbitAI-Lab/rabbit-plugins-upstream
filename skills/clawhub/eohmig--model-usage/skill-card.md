## Description: <br>
Use CodexBar CLI local cost usage to summarize per-model usage for Codex or Claude, including the current model or a full model breakdown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eohmig](https://clawhub.ai/user/eohmig) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to summarize local CodexBar cost data by model for Codex or Claude, either for the most recent current model or for all models in the supplied usage data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may run the bundled Python script and CodexBar CLI against local Codex or Claude usage logs. <br>
Mitigation: Review the command before execution and prefer passing only CodexBar cost JSON files intended for analysis. <br>
Risk: The model breakdown is cost-only and does not split token counts by model. <br>
Mitigation: Treat the output as a cost summary and verify the source CodexBar JSON when token-level attribution is required. <br>


## Reference(s): <br>
- [CodexBar CLI quick ref](references/codexbar-cli.md) <br>
- [Model Usage on ClawHub](https://clawhub.ai/eohmig/skills/model-usage) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Plain text summaries or JSON objects, often accompanied by shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports cost-only per model; token counts are not split by model in CodexBar output.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
